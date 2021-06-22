from azure.storage.queue import (
        QueueService,
        QueueMessageFormat
)
import os, uuid

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1>Welcome to the Trace App! We will help you sort out your product reviews.</h1><br><br><label for="fname">Write a review: </label><input type="text" id="fname" name="fname"><br><br><input type="submit" value="Check Sentiment">'
      
  
  

# message = u"Hello, World"
# print("Adding message: " + message)
# QueueService.put_message(new-feedback-q, message)