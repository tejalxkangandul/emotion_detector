# Simple Emotion Detector

A beginner-friendly web application that detects the sentiment of your text as **Positive 😊, Negative 😞, or Neutral 😐**.  
Built using Python (Flask), and Bootstrap for quick, beautiful styling.



# Features

- Sleek, mobile-friendly web UI (Bootstrap-powered)
- Enter any sentence; instantly get a sentiment and a polarity score
- Completely open source and super easy to set up



# Technology Stack

- **Python (Flask)** – backend web framework
- **TextBlob** – for basic sentiment analysis
- **HTML, CSS, Bootstrap** – user interface



# Getting Started

 ## 1. Clone This Repository

git clone https://github.com/yourusername/emotion-detector.git
cd emotion-detector


 ## 2. Create and Activate a Virtual Environment

On Windows:
python -m venv venv
venv\Scripts\activate


On macOS/Linux:
python3 -m venv venv
source venv/bin/activate


## 3. Install Dependencies

pip install -r requirements.txt
python -m textblob.download_corpora

## 4. Start the Application

python app.py

## 5. Open Your Browser

Go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  
Type in your sentence and see the magic!



##  Project Structure

emotion_detector/
├── app.py
├── requirements.txt
└── templates/
└── index.html



##  Example Inputs

- I love learning new things!
- This is the worst movie I have ever seen.
- Today is a day.


##  Customization Ideas

- Add more detailed emotion classification (using other NLP libraries)
- Suggest example phrases right on the site
- Personalize the Bootstrap theme for a unique look
