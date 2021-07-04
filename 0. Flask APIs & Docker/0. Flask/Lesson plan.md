# Your own API

## Recap APIs
- Ask what is an API?
- Explain an API is just a computer running somewhere that knows how to process and respond to certain messages sent to it

## Let's make our own API
- Introduce Flask
- Hello world GET route example
- Show response in browser

## Make a predict route
- make a new route
- show how to make it accept POST requests
- import requests from flask and show how it's used
- make post request in client.py
- get data in route using request.get_data()

## Cleanup
- add a ```content-type``` header to the post request and set it's value to ```application/json```
- switch get_data to get_json