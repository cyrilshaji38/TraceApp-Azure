from flask import Flask, render_template
from azure.storage.queue import QueueServiceClient

connect_str = "DefaultEndpointsProtocol=https;AccountName=storageaccounttrace8774;AccountKey=TApeXC/1SCYVXPYZRywFqleViIkAGMpWV1G51D1cVTyjJutNcgjlDSCSW2MzBW6guPS6FUtzD4Y7Yo9c37WZ2w==;EndpointSuffix=core.windows.net"
app = Flask(__name__)

@app.route("/")
def home_page(): 
        return render_template('home.html') 

class ReviewQueue(object):
        def add_to_queue():
                service = QueueServiceClient.from_connection_string(conn_str=connect_str)
                reviewqueue = service.get_queue_client(queue="new-feedback-q")
                reviewqueue.send_message("very nice food!")

if __name__ == '__main__':
        sample = ReviewQueue()
        sample.add_to_queue()