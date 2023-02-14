import requests
import json
def compile():
    abv = ["ca", "ut", "il", "az", "tx"]
    dict_states = {"ca": "California", "ut": "Utah", "il": "Illinois", "az": "Arizona", "tx": "Texas"}
    #The above creates a dictionary for the 5 states.
    
    for state in abv:
    #state = 'ut'
        url = 'https://api.covidtracking.com/v1/states/' + state + '/daily.json'
        #the line above ensures that the correct state is used.
        req = requests.get(url)
        req_dict = json.loads(req.text)
        json.dump(req_dict, open("/home/ubuntu/environment/hw3/" + state + ".json", "w"))
        #The above code gets the data and dumps into their respective json files.
