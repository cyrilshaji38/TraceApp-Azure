from flask import Flask, render_template
import os

app = Flask(__name__)
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

@app.route("/")
def home_page(): 
        return render_template('home.html') 

def create_client_with_connection_string(self):
        from azure.storage.queue import QueueServiceClient
        queue_service = QueueServiceClient.from_connection_string(conn_str=self.connection_string)
# queue_client.create_queue()
# queue_client.send_message(u"Nice food")