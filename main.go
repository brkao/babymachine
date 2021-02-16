package main

import (
	"fmt"
	"os"
	"sync"
)

var serverPort string
var clientId string
var clientSecret string
var username string
var password string

var subreddits = [...]string{"/r/WallStreetBets/hot"}

func doConfig() {
	cId, ok := os.LookupEnv("CLIENT_ID")
	if !ok {
		fmt.Printf("Error No Client ID")
		os.Exit(1)
	}
	clientId = cId

	cSecret, ok := os.LookupEnv("CLIENT_SECRET")
	if !ok {
		fmt.Printf("Error No Client SECRET")
		os.Exit(1)
	}
	clientSecret = cSecret

	uname, ok := os.LookupEnv("USERNAME")
	if !ok {
		fmt.Printf("Error No USERNAME")
		os.Exit(1)
	}
	username = uname

	pwd, ok := os.LookupEnv("PASSWORD")
	if !ok {
		fmt.Printf("Error No PASSWORD")
		os.Exit(1)
	}
	password = pwd

	f, err := os.OpenFile(".prof", os.O_RDWR|os.O_CREATE, 0755)
	if err != nil {
		os.Exit(1)
	}
	f.Write([]byte("user_agent: \"rBot\"\n"))
	f.Write([]byte(string("client_id: \"" + clientId + "\"\n")))
	f.Write([]byte(string("client_secret: \"" + clientSecret + "\"\n")))
	f.Write([]byte(string("username: \"" + username + "\"\n")))
	f.Write([]byte(string("password: \"" + password + "\"\n")))
	if err := f.Close(); err != nil {
		os.Exit(1)
	}
}

func main() {
	doConfig()

	var rbot RedditBot
	//this is in seconds
	rbot.interval = 20 * 60
	//how many velocity history to keep
	rbot.maxIntervals = 8
	//max number of links to track
	rbot.maxRecords = 100
	rbot.clientId = clientId
	rbot.clientSecret = clientSecret
	rbot.username = username
	rbot.password = password

	//ths subreddit
	for _, name := range subreddits {
		rbot.subreddit = append(rbot.subreddit, name)
	}

	var wg sync.WaitGroup
	fmt.Println("Main: starting Velocity redditBot")
	wg.Add(1)
	go (&rbot).start()

	fmt.Println("Main: Waiting for rbot & server to finish")
	wg.Wait()

	fmt.Println("Main: Completed, exit")
}
