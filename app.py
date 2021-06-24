from flask import Flask, render_template
from azure.storage.queue import (
        QueueClient,
        TextBase64EncodePolicy
)
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

connect_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
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
        def add_to_queue(self):
                reviewqueue = QueueClient.from_connection_string(
                        conn_str=connect_str, 
                        queue_name = "new-feedback-q", 
                        message_encode_policy = TextBase64EncodePolicy()
                )
                r1 = ReviewForm()
                reviewqueue.send_message(r1.review.data)


if __name__ == '__main__':
    app.debug = True
    app.run()