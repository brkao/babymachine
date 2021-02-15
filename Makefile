run: bin/babymachine
	@PATH="$(PWD)/bin:$(PATH)" heroku local

bin/babymachine: main.go reddit.go
	go build -o bin/babymachine main.go reddit.go

clean:
	rm -rf bin

