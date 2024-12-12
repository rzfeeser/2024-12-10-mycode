#!/usr/bin/python3
'''write a python script that makes a request to

https://api.spacexdata.com/v3/dragons

it should then display the "name" of both records
they are "Dragon 1" and "Dragon 2"'''

# python3 -m pip install requests
import requests

SPACEX_URL = "https://api.spacexdata.com/v3/dragons"

def main():
    '''runtime code'''
    
    try:
        # send HTTP GET to spacex API
        spacex_response = requests.get(SPACEX_URL + "/fake")

        # raise if 4xx or 5xx
        spacex_response.raise_for_status() # this will BREAK the try condition if a 4xx or 5xx was returned

        # strip off JSON from response
        spacex_json = spacex_response.json()

        # loop across our list
        for record in spacex_json:
            # each record within the list, we want to select the value "name"
            print(record.get("name"))

    # on an error this code executes
    except Exception as err:
        print("Uh oh! Something went wrong with that lookup!")
        print("Dumping the error...")
        print(err)



if __name__ == "__main__":
    main()
