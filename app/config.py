import os


class Config():
    #Flask Key
    SECRET_KEY = os.environ.get('FLASK_SERVERMONITOR') #TODO: Get own SecretKey
    