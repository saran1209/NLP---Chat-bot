import sys
sys.path.insert(0, '/flask_app')

#import libraries
import nltk
import torch
import pandas as pd
import random
import sys
# Load pretrained Model
from models import InferSent
from scipy.spatial.distance import cosine
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from code import file
from chatbot import chatty

from tf_idf  import *
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='saran', password='saran'))




app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

#Setting up Greetings and Response
Greetings = ("hello", "hi" , "What's up ?" , "hey",'Hi there' ,'Hello everyone !',"anyone here !")
Greet_Response = ["hi","Hello" , "Hi what's up ?","hi , welcome How can i help ?" ]

def  Greet(Input):
    for word in Input.split():
        if word.lower() in Greetings:
            return random.choice(Greet_Response)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('welcome'))

        return redirect(url_for('accept'))

    return render_template('login.html')
@app.route('/welcome')
def welcome():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('welcome.html')


@app.route('/encode_infersent')
def encode_infersent():
    # NLTK Tokenizer
    nltk.download('punkt')
    # encoding sentences using infersent
    V = 2
    MODEL_PATH = 'encoder/infersent1.pkl'
    params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                    'pool_type': 'max', 'dpout_model': 0.0, 'version': V}
    infersent = InferSent(params_model)
    infersent.load_state_dict(torch.load(MODEL_PATH))

    # Set word vector path for the model

    W2V_PATH = 'fastText/crawl-300d-2M.vec'
    infersent.set_w2v_path(W2V_PATH)

    # Load our sentences
    sentences = []
    data = pd.read_csv('scraptext.csv')
    # Build the vocabulary of word vectors

    for sent in data.text:
        sentences.append(sent)

    infersent.build_vocab(sentences, tokenize=True)
    embeddings_sent = infersent.encode(sentences, tokenize=True)
    return render_template('infersent.html')

@app.route('/Webscrapper',methods=['POST','GET'])
def Web_scrapper():
    if request.method=='POST':
        link = request.form['link']
        return redirect(url_for('scrap_catalog',page=link))
    return render_template('Webscrapper.html')

from werkzeug.utils import secure_filename


@app.route('/upload')
def upload():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return render_template('uploaddone.html')

@app.route('/scrap_catalog')
def scrap_catalog():
    # Loading Libraries for scrapping
    link=request.args['page']
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import requests
    import re
    import pandas as pd
    # configure web driver to use chrome Browser
    from webdriver_manager.chrome import ChromeDriverManager
    page = requests.get(url=link)

    soup = BeautifulSoup(page.content, 'html.parser')

    p = soup.find_all('p')
    ul = soup.find_all('ul')

    MS = {"Overview": None, "Career Paths": None, "Lab Facilities": None, "Pre-Requisite Courses and Background": None,
          "Program Requirements": None, "Area Courses": None, "Degree Requirements": None}

    # clean text from html tags
    def cleanhtml(raw_html):
        cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        cleantext = re.sub(cleanr, '', raw_html)

        return (cleantext)

    # Overview Text
    overview = ""
    for i in range(6):
        overview += cleanhtml(str(p[i]))

    MS['Overview'] = overview

    # Career Paths
    MS['Career Paths'] = cleanhtml(str(p[5]))

    # Lab Facilities
    lab = ""
    for i in range(7, 13):
        lab += cleanhtml(str(p[i]))

    MS['Lab Facilities'] = lab

    # Pre-requisite Courses and Background

    pre = cleanhtml(str(p[13])) + cleanhtml(str(ul[0])) + cleanhtml(str(p[14]))
    MS['Pre-Requisite Courses and Background'] = pre

    # Program Requirements

    prog = cleanhtml(str(p[15]))
    MS['Program Requirements'] = prog

    # Area Courses
    area = ""
    area += cleanhtml(str(p[16])) + cleanhtml(str(p[17])) + cleanhtml(str(ul[1])) + cleanhtml(str(p[18])) + cleanhtml(
        str(ul[2])) + cleanhtml(str(p[19])) + cleanhtml(str(ul[3])) + cleanhtml(str(p[20])) + cleanhtml(str(ul[4]))

    for i in range(21, 26):
        area += cleanhtml(str(p[i]))
    MS["Area Courses"] = area

    # Degree Requirements
    MS['Degree Requirements'] = cleanhtml(str(ul[5]))

    # Save it in csv file
    import csv

    with open('scraptextt.csv', 'w') as f:
        for key in MS.keys():
            f.write("%s,%s" % (key, MS[key]) + "\n")

    return render_template('scrap.html')

# NLTK Tokenizer
nltk.download('punkt')
# encoding sentences using infersent
V = 2
MODEL_PATH = 'encoder/infersent1.pkl'
params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                'pool_type': 'max', 'dpout_model': 0.0, 'version': V}
infersent = InferSent(params_model)
infersent.load_state_dict(torch.load(MODEL_PATH))

# Set word vector path for the model

W2V_PATH = 'fastText/crawl-300d-2M.vec'
infersent.set_w2v_path(W2V_PATH)

# Load our sentences
sentences = []
data = pd.read_csv('scraptext.csv')
# Build the vocabulary of word vectors

for sent in data.text:
    sentences.append(sent)

infersent.build_vocab(sentences, tokenize=True)
embeddings_sent = infersent.encode(sentences, tokenize=True)

# Encode any sentence using infersent
def encode_infersent(sentence):
    V = 2
    MODEL_PATH = 'encoder/infersent1.pkl'
    params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                    'pool_type': 'max', 'dpout_model': 0.0, 'version': V}
    infersent = InferSent(params_model)
    infersent.load_state_dict(torch.load(MODEL_PATH))
    # Set word vector path for the model

    W2V_PATH = 'fastText/crawl-300d-2M.vec'
    infersent.set_w2v_path(W2V_PATH)
    infersent.build_vocab(sentence, tokenize=True)
    embedding = infersent.encode(sentence, tokenize=True)
    return(embedding)


# term-frequency
# create the term frequency array

def frequency_words(text):

    stopWords = set(stopwords.words("english"))

    words = word_tokenize(text)

    ps = PorterStemmer()

    freqwords = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqwords:
            freqwords[word] += 1
        else:
            freqwords[word] = 1

    return(freqwords)




#  we need to score each sentence : i.e how much each sentence is important in the paragraph
def score_sentences(sentences, array_freq):

    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for wordValue in array_freq:
            if wordValue in sentence.lower():
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += array_freq[wordValue]
                else:
                    sentenceValue[sentence[:10]] = array_freq[wordValue]

        sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] # word_count_in_sentence

    return(sentenceValue)



# find the threshold

def find_score(sentenceValue):

    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))

    return(average)





# final step  is to generate the summary
def generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] > (threshold):
            summary += " " + sentence
            sentence_count += 1

    return(summary)

text_summarize = []

for text in data.text:
    array_freq = frequency_words(text)
    # tokenize the sentences : we need to split paragraph into sentences using sent_tokenize method
    text = text.replace('\n', '.')
    sentences = sent_tokenize(text)
    sentences_scores = score_sentences(sentences, array_freq)
    threshold = find_score(sentences_scores)

    summary = generate_summary(sentences, sentences_scores, 0.4 * threshold)
    text_summarize.append(summary)
# Reading the Summary File
sumr= open('Summary.txt','w')
for text in text_summarize:
	sumr.write(text)
from csv import writer
from emoji import emojize
def Questionstorer(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
import csv
# local hosting 
@app.route("/")
def home():
    return render_template("index.html",title='Home')
@app.route('/get')
def getbotresponse():
    userText = request.args.get('msg')
    Questionstore = []
    if len(userText)>7:
        Questionstore.append(userText)
    if len(Questionstore)>0:
        Questionstorer("Questionstore.csv",Questionstore)
    chat= chatty(userText)
    if chat is not None:
        return chat
    else:
        if (userText.lower()!= 'bye'):
            if (userText== 'thanks' or userText== 'thank you'):
                sent="You are welcome.."
            else:
                if (Greet(userText) != None):
                    sent=Greet(userText)
                else:
                    sent = response(userText)
                    sent_tokens.remove(userText)
                    return sent
        else:
            sent="Bye! take care.." + emojize(":thumbs_up:")
            return sent
