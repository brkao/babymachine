run: babymachine
	@PATH="$(PWD):$(PATH)" heroku local

babymachine: main.go reddit.go
	go build -o babymachine main.go reddit.go

clean:
	rm -rf bin

