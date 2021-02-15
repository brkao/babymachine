package main

import (
	"encoding/json"
	"fmt"
	"github.com/brkao/graw/reddit"
	"github.com/gomodule/redigo/redis"
	"os"
	"sort"
	"time"
)

var timeZone string = "America/Los_Angeles"

func TimeIn(t time.Time, name string) (time.Time, error) {
	loc, err := time.LoadLocation(name)
	if err == nil {
		t = t.In(loc)
	}
	return t, err
}

type RedditBot struct {
	bot             reddit.Bot
	subreddit       []string
	interval        int32
	urlMap          map[string]*PostRecord
	RecordList      []*PostRecord `json:"RecordList"`
	maxRecords      int32
	maxIntervals    int32
	updateCountdown int32
	started         time.Time
	LastUpdate      time.Time `json:"Timestamp"`
	clientId        string
	clientSecret    string
	username        string
	password        string
}

type PostRecord struct {
	Url       string    `json:"url"`
	UpV       []float32 `json:"UpVelocity"`
	DownV     []float32 `json:"DownVelocity"`
	LastUp    int32     `json:"LastUpVote"`
	LastDown  int32     `json:"LastDownVote"`
	LastRatio float32   `json:"LastVoteRatio"`
}

func (p *PostRecord) printout() {
	fmt.Printf("\tURL[%s] LastUp[%d] LastDown[%d] LastRatio[%f]\n",
		p.Url, p.LastUp, p.LastDown, p.LastRatio)
	fmt.Printf("\tUp Velocity:\t")
	for _, val := range p.UpV {
		fmt.Printf("[%f] ", val)
	}
	fmt.Printf("\n")

	fmt.Printf("\tDown Velocity:\t")
	for _, val := range p.DownV {
		fmt.Printf("[%f] ", val)
	}
	fmt.Printf("\n")

}

func (p *PostRecord) MarshalJSON() ([]byte, error) {
	po := *p
	str, _ := json.Marshal(po)
	return str, nil
}

func (r *RedditBot) top() []byte {
	ret, _ := json.Marshal(r.RecordList)
	return ret
}

func (r *RedditBot) storeToRedis() {
	c, err := redis.DialURL(os.Getenv("REDIS_URL"), redis.DialTLSSkipVerify(true))
	if err != nil {
		fmt.Printf("Error connecting to REDIS\n")
		return
	}
	defer c.Close()

	data, _ := json.Marshal(r)
	c.Do("LPUSH", "dd_velocities", data)
	c.Do("LTRIM", "dd_velocities", 0, 99)
	fmt.Printf("Stored to REDIS\n")
}

func (r *RedditBot) topPlain() string {

	var ret string

	loc, err := time.LoadLocation("America/Los_Angeles")
	if err != nil {
		fmt.Println(err)
		return ""
	}

	ret = ret + fmt.Sprintf("<html><body>")
	ret = ret + fmt.Sprintf("List in order of upvote velocity for all the DDs in [%s]<br>",
		r.subreddit)
	ret = ret + fmt.Sprintf("Tracking up to %d newest posts with %d historical velocities at %d seconds intervals<br><br>",
		r.maxRecords, r.maxIntervals, r.interval)
	ret = ret + fmt.Sprintf("Server started on: %s<br>\n", fmt.Sprintf((r.started.In(loc)).String()))
	ret = ret + fmt.Sprintf("Last updated on: %s<br>\n", fmt.Sprintf((r.LastUpdate.In(loc)).String()))
	ret = ret + fmt.Sprintf("Next update in %d seconds<br>", r.updateCountdown)
	for i, p := range r.RecordList {

		ret = ret + fmt.Sprintf("--->  %d <--- <br>", i)
		ret = ret + fmt.Sprintf("<a href=\"http://www.reddit.com%s\">%s</a><br>", p.Url, p.Url)
		ret = ret + fmt.Sprintf("LastUp[%d] LastDown[%d] LastRatio[%f]<br>",
			p.LastUp, p.LastDown, p.LastRatio)
		ret = ret + fmt.Sprintf("\tU Velocity:\t")
		for _, val := range p.UpV {
			ret = ret + fmt.Sprintf("[%f] ", val)
		}
		ret = ret + fmt.Sprintf("<br>")

		ret = ret + fmt.Sprintf("\tD Velocity:\t")
		for _, val := range p.DownV {
			ret = ret + fmt.Sprintf("[%f] ", val)
		}
		ret = ret + fmt.Sprintf("<br><br>")
	}
	ret = ret + fmt.Sprintf("</html></body>")
	return ret
}

func (r *RedditBot) getFreeRecord() *PostRecord {
	if len(r.RecordList) >= int(r.maxRecords) {
		//fmt.Printf("Max record numbers, deleting one\n")
		r.RecordList = r.RecordList[:len(r.RecordList)-1]
	}
	var ret PostRecord
	ret.UpV = make([]float32, r.maxIntervals)
	ret.DownV = make([]float32, r.maxIntervals)
	return &ret
}

func (r *RedditBot) addNewRecord(po *PostRecord) {
	r.urlMap[po.Url] = po
	for i, record := range r.RecordList {
		if record.UpV[0] <= po.UpV[0] {
			r.RecordList = append(r.RecordList, nil)
			copy(r.RecordList[i+1:], r.RecordList[i:])
			r.RecordList[i] = po
			//fmt.Printf("Added record, len %d\n", len(r.RecordList))
			return
		} else {
			//fmt.Printf("Record in array[%d] has higher velocity\n", i)
		}
	}
	r.RecordList = append(r.RecordList, po)
	//fmt.Printf("Adding record to tail, len %d\n", len(r.RecordList))
}

func (r *RedditBot) start() {
	t, err := TimeIn(time.Now(), timeZone)
	if err != nil {
		t = time.Now()
	}
	r.started = t

	b, err := reddit.NewBotFromAgentFile(".prof", 0)
	if err != nil {
		fmt.Println("Failed to create bot handle:  ", err)
		return
	}
	r.bot = b
	r.urlMap = make(map[string]*PostRecord)

	fmt.Printf("Bot Start: maxIntervals %d interval %d maxRecords %d\n",
		r.maxIntervals, r.interval, r.maxRecords)

	r.LastUpdate = r.started
	r.harvest()
	fmt.Println("Initial Harvest done")
	r.storeToRedis()

	ticker := time.NewTicker(time.Duration(r.interval) * time.Second)
	countdownTicker := time.NewTicker(10 * time.Second)
	for {
		select {
		case <-ticker.C:
			fmt.Println("Timer, harvesting")

			t, err = TimeIn(time.Now(), timeZone)
			if err != nil {
				t = time.Now()
			}
			r.LastUpdate = t

			r.harvest()
			fmt.Println("Harvest done")
			/*
				for _, val := range r.RecordList {
					val.printout()
				}
			*/
			r.storeToRedis()
			fmt.Println("\n")
		case <-countdownTicker.C:
			r.updateCountdown = r.updateCountdown - 10
		}
	}
}

func (r *RedditBot) harvest() {
	var params map[string]string
	params = make(map[string]string)
	//params["sort"] = "new"

	//reset the countdown timer
	r.updateCountdown = r.interval

	for _, subr := range r.subreddit {
		fmt.Printf("Harvesting %s\n", subr)
		harvest, err := r.bot.ListingWithParams(subr, params)
		if err != nil {
			fmt.Println("Failed to fetch ", err)
			return
		}

		for _, post := range harvest.Posts {
			if post.LinkFlairText != "DD" {
				continue
			}

			var down int32
			var up int32
			down = post.Score - int32(float64(post.Score)*float64(post.UpvoteRatio))
			up = int32(float64(post.Score) * float64(post.UpvoteRatio))
			//fmt.Printf("Permalink[%s] Score[%d] Ratio [%f] Ups[%d] Downs[%d]\n",
			//	post.Permalink, post.Score, post.UpvoteRatio, up, down)

			if val, ok := r.urlMap[post.Permalink]; ok {
				UpV := float32((up - val.LastUp))
				if UpV < 0 {
					UpV = 0
				} else {
					UpV = UpV / float32(r.interval)
				}

				DownV := float32((down - val.LastDown))
				if DownV <= 0 {
					DownV = 0
				} else {
					DownV = DownV / float32(r.interval)
				}

				//	fmt.Printf("Found Permalink in map UpV[%f] DownV[%f] LastRatio[%f]\n",
				//			UpV, DownV, post.UpvoteRatio)
				val.LastRatio = post.UpvoteRatio
				val.LastDown = down
				val.LastUp = up

				copy(val.UpV[1:], val.UpV[0:len(val.UpV)-1])
				copy(val.DownV[1:], val.DownV[0:len(val.DownV)-1])

				val.UpV[0] = UpV
				val.DownV[0] = DownV

				sort.Slice(r.RecordList[:], func(i, j int) bool {
					return r.RecordList[i].UpV[0] >= r.RecordList[j].UpV[0]
				})

			} else {
				po := r.getFreeRecord()
				po.Url = post.Permalink
				po.LastUp = up
				po.LastDown = down
				po.LastRatio = post.UpvoteRatio

				r.addNewRecord(po)
			}
		}
	}
}
