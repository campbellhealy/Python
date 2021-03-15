# -*- coding: utf-8 -*-
import requests
import pprint
import unittest
import json
from ast import literal_eval
from pathlib import Path

from locator_builds import location1, location2, location3

class reverse_geocoding(unittest.TestCase):
    def test_location_one(self):
        loc = location1
            
        # GET Request
        r = requests.get(url = loc) 

        # extracting data in json format 
        data = r.json() 
        #  Creating Nested Dictionary
        locale = json.dumps(data)
        python_dict = literal_eval(locale)

        # Create List from required Nested Dictionary
        access_address = python_dict['address']
        print (loc)
        print (" Street: %s " % access_address.get('road'))
        print (" Postal: %s " % access_address.get('postcode'))
        print (" City: %s " % access_address.get('city'))
        print (" Provence: %s " % access_address.get('country_code'))
        print (" Country: %s " % access_address.get('country'))
        print ()
        

if __name__ == "__main__":
    unittest.main()
