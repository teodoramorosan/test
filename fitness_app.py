import json
 import os
from datetime import datetime


FILE_NAME  = "fitness_data.json"


#------------------ DATABASE ------------------

def load_data():
    if not os.path.exists(FILE_NAME):
       return {
          "profile": {},
          "workouts": [],
          "meals":
       }
    
    with open(FILE_NAME, "r") as f:
       return json.load(f)
    

def  save_data(data):
   with open (FILE_NAME, "w") as f:
      json.dump(data, f indent=4)


# ------------------ PROFILE ------------------

def create_profile():
   data = load_data()