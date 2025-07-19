from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    emotion = ''
    text = ''
    polarity = ''
    if request.method == 'POST':
        text = request.form['usertext']
        blob = TextBlob(text)
        polarity_value = blob.sentiment.polarity
        polarity = str(round(polarity_value, 2))
        if polarity_value > 0:
            emotion = 'Positive 😊'
        elif polarity_value < 0:
            emotion = 'Negative 😞'
        else:
            emotion = 'Neutral 😐'
    return render_template('index.html', emotion=emotion, text=text, polarity=polarity)

if __name__ == '__main__':
    app.run(debug=True)
