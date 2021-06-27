from flask import Flask, render_template, redirect, url_for
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
# from amazon-reviews import get_review

subscription_key = os.environ["TEXT_ANALYTICS_SUBSCRIPTION_KEY"]
endpoint = os.environ["TEXT_ANALYTICS_ENDPOINT"]

def authenticate_client():
    ta_credential = AzureKeyCredential(subscription_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def sentiment_analysis_example(client):
    r1 = ReviewForm()
    documents = [r1.review.data]
    response = client.analyze_sentiment(documents=documents)[0]
    r2.sentimental_analysis = response.sentiment
    print("Document Sentiment: {}".format(response.sentiment))

def key_phrase_extraction_example(client):
    r1 = ReviewForm()
     
    try:
        documents = [r1.review.data]
        response = client.extract_key_phrases(documents = documents)[0]
        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                r2.key_phrases.append(phrase)
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))


app = Flask(__name__)

app.config['SECRET_KEY'] = '7b040a256ba53639fe34e81ccba6bb41'

@app.route("/", methods = ['GET','POST'])
def home_page():
    form = ReviewForm()
    if form.validate_on_submit():
        sentiment_analysis_example(client)
        key_phrase_extraction_example(client)
        r2.user_review = form.review.data
        return redirect(url_for('result_page'))
    return render_template('home.html', form=form)

@app.route("/results")
def result_page():
    return render_template('results.html', d1 = r2.user_review, d2 = r2.sentimental_analysis, d3 = r2.key_phrases)


class ReviewForm(FlaskForm):
    review = StringField(label='Write a review: ')
    submit = SubmitField(label='Check Sentiment')   

class Results():
    user_review = ""
    sentimental_analysis = "" 
    key_phrases = []
    
r2 = Results()


if __name__ == '__main__':
    app.debug = True
    app.run()
