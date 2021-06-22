# from azure.storage.queue import (
#         QueueService,
#         QueueMessageFormat
# )
# import os, uuid

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home_page(): 
        return render_template('home.html') 
      
  
  

# message = u"Hello, World"
# print("Adding message: " + message)
# QueueService.put_message(new-feedback-q, message)