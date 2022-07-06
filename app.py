from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys
import os

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing the custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing the logging module")
    return "CI CD pipeline has been established "


if __name__=="__main__":
    app.run(debug= True)