from flask import Flask, render_template
import os
app = Flask(__name__)
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
@app.route("/")
def home_page(): 
        return connect_str
        # render_template('home.html') 

# from azure.storage.queue import QueueClient

# queue_client = QueueClient.from_connection_string(connect_str, "new_queue")
# queue_client.create_queue()
# queue_client.send_message(u"Nice food")