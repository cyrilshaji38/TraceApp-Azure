from azure.storage import queue
from flask import Flask, render_template
import os

app = Flask(__name__)
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

@app.route("/")
def home_page(): 
        return render_template('home.html') 

def add_to_queue():
        from azure.storage.queue import QueueServiceClient
        service = QueueServiceClient.from_connection_string(conn_str=connect_str)
        queue = service.get_queue_client(queue="new-feedback-q")
        # from azure.storage.queue import QueueClient
        # # queue = QueueClient.from_connection_string(conn_str=connect_str, queue_name="new-feedback-q")
        queue.send_message("very nice food!")

if __name__ == '__main__':
        add_to_queue()