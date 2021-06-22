from flask import Flask, render_template
app = Flask(__name__)

from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

import os, uuid

@app.route("/")
def home_page(): 
        return render_template('home.html') 


connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
q_name = "new" + str(uuid.uuid4())
print("Creating queue: " + q_name)
queue_client = QueueClient.from_connection_string(connect_str, q_name)
queue_client.create_queue()

message = u"Nice food"
print("Adding message: " + message)
queue_client.send_message(message)