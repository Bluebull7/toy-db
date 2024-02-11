import json
import os

class Foobar(object):
    # Define main class
    def __init__(self, location):
    # replace ~ or ~user with $HOME dir
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        #check if db exists
        if os.path.exists(location):
            self._load()
        #create empty json object
        else:
            self.db = {}
        return True


    def _load(self):
        # transform file into JSON obj and load to self.db
        self.db = json.load(open(self.location , "r"))

    def dumpdb(self):
        # takes JSON obj from self.db and saves to db
        try:   
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False
        
    def set(self , key, value):
        # convert value to key and add to DB
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False
    
    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key))
            return False
    
    def delete(self, key):
        # not in DB
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True
    

