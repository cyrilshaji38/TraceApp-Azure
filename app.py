from flask import Flask, render_template
import os

app = Flask(__name__)
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

@app.route("/")
def home_page(): 
        return render_template('home.html') 

from azure.storage.queue import QueueServiceClient
service = QueueServiceClient.from_connection_string(conn_str=connect_str)

from azure.storage.queue import QueueClient
queue = QueueClient.from_connection_string(conn_str=connect_str, queue_name="new-feedback-q")
queue.send_message("very nice food!")
