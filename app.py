from flask import Flask, render_template
from azure.storage.queue import QueueServiceClient
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

connect_str = "DefaultEndpointsProtocol=https;AccountName=storageaccounttrace8774;AccountKey=TApeXC/1SCYVXPYZRywFqleViIkAGMpWV1G51D1cVTyjJutNcgjlDSCSW2MzBW6guPS6FUtzD4Y7Yo9c37WZ2w==;EndpointSuffix=core.windows.net"
app = Flask(__name__)

app.config['SECRET_KEY'] = '7b040a256ba53639fe34e81ccba6bb41'

@app.route("/", methods = ['GET','POST'])
def home_page():
        form = ReviewForm()
        if form.validate_on_submit():
                sample = ReviewQueue()
                sample.add_to_queue()
        return render_template('home.html', form=form)

class ReviewForm(FlaskForm):
    review = StringField(label='Write a review: ')
    submit = SubmitField(label='Check Sentiment')
    

class ReviewQueue(object):
        def add_to_queue():
                service = QueueServiceClient.from_connection_string(conn_str=connect_str)
                reviewqueue = service.get_queue_client(queue="new-feedback-q")
                r1 = ReviewForm()
                reviewqueue.send_message(r1.review)


if __name__ == '__main__':
    app.debug = True
    app.run()