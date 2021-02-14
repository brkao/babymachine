run: velocity
	@PATH="$(PWD):$(PATH)" heroku local

velocity: main.go reddit.go
	go build -o velocity main.go reddit.go

clean:
	rm -rf bin

