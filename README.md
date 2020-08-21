# NLP---Chat-bot
Masters Project - NLP Chat bot for college Enquiry.
# DEMO
<img src="demo.gif" alt="">
<h1> ABSTRACT </h1>
<p> This project focuses on Creating Virtual Query answering system for Colleges. This
System is a Web Application which solves user’s queries from Documents provided by the
admin. Natural language processing which is a branch of Artificial Intelligence has played
major role in this system which helps the computer to understand user’s query. A Chat
bot should be easy to use,fast and accurate to enhance user experience.Reading a catalog
or Searching the website for a small query would waste user’s time where as this Virtual
Assistant would be able to solve the query in seconds. Updating the chat bot will be easy
compared to updating on web page or catalog. Admin would be able to update the document
without any programming knowledge. This project will improve the user experience and will
be available 24/7 to solve queries. </p>
<h1> Requirments </h1>
This code is written in python. Dependencies include:
<ol>
<li> Python 3 </li>
<li> Pytorch (recent version)</li>
<li> NLTK >= 3</li>
</ol>

Other requirments : 
<ol>
<li> Click==7.0</li>
<li>Flask==1.1.1</li>
<li>itsdangerous==1.1.0</li>
<li>Jinja2==2.11.1</li>
<li>MarkupSafe==1.1.1</li></li>
<li>Werkzeug==1.0.0</li>
</ol>
<h1>Downloads </h1>
Download word vectors
<pre><h3>Download GloVe (V1) or fastText (V2) vectors:</h3>
mkdir GloVe
curl -Lo GloVe/glove.840B.300d.zip http://nlp.stanford.edu/data/glove.840B.300d.zip
unzip GloVe/glove.840B.300d.zip -d GloVe/

mkdir fastText
curl -Lo fastText/crawl-300d-2M.vec.zip https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M.vec.zip
unzip fastText/crawl-300d-2M.vec.zip -d fastText/</pre>
        
<h1>Installation and Importing </h1>
<p>Natural language Tool Kit</p>
<ul>
<li>Download the latest version of Python for Windows from below link https://www.python.org/downloads</li>
<li>Install NLTK - Python download</li>
<li>Go to Command prompt and type pip install nltk and press enter</li>
<li>Go to Command prompt and type conda install pytorch torchvision cudatoolkit=10.2-c pytorch</li>
<li>Go to Command prompt and type pip install flask</li>
 </ul>
<h1>File Details </h1>
<ul>
        <li>app.py - Includes Code for scarpping, Summarization and Vectorization. </li>
<li>Models.py - Facebook infersent encoder files ( please check with https://github.com/facebookresearch/InferSent  to see if they have updates Models.py file)</li>
        <li>Tfidf.py - Finds the relevant sentences to respond </li>
        </ul>
<h1> References </h1>
<li>Denny Britz. Deep learning for chatbots. WildML Artificial Intelligence,
Deep Learning, and NLP http://www.wildml.com/2016/04/
deep-learning-for-chatbots-part-1-introduction/. </li>
<li>Alexis Conneau, Douwe Kiela, Holger Schwenk, Loïc Barrault, and Antoine Bordes. Supervised
learning of universal sentence representations from natural language inference
data. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language
Processing, pages 670–680, Copenhagen, Denmark, September 2017. Association
for Computational Linguistics. </li>
<li>Menal Dahiya. A tool of conversation: Chatbot. INTERNATIONAL JOURNAL OF
COMPUTER SCIENCES AND ENGINEERING, 5, 2017. </li>
<li>G. A. Dalaorao, A. M. Sison, and R. P. Medina. Integrating collocation as tf-idf enhancement
to improve classification accuracy. In 2019 IEEE 13th International Conference on
Telecommunication Systems, Services, and Applications (TSSA), pages 282–285, 2019. </li>
<li> Armand Joulin, Edouard Grave, Piotr Bojanowski, Matthijs Douze, Hérve Jégou, and
Tomas Mikolov. Fasttext.zip: Compressing text classification models. arXiv preprint
arXiv:1612.03651, 2016. </li>
<li>Caglar Gulcehre Dzmitry Bahdanau Fethi Bougares Holger Schwenk Yoshua Bengio
Kyunghyun Cho, Bart van Merrienboer. Learning phrase representations using rnn
encoder-decoder for statistical machine translation. arXiv:1406.1078 https://arxiv.
org/abs/1406.1078, 2006. </li>
<li>A. R. Lahitani, A. E. Permanasari, and N. A. Setiawan. Cosine similarity to determine
similarity measure: Study case in online essay assessment. In 2016 4th International
Conference on Cyber and IT Service Management, pages 1–6, 2016. </li>
<li> Ojas Wankhade Pradnya Mehta Sagar Pawar, Omkar Rane. A web based college enquiry
chatbot with results. International Journal of Innovative Research in Science,
Engineering and Technology, 7, 2018.</li>
<li>JosephWeizenbaum. Computer power and human reason: From judgment to calculation.
pages 367–375, 1976. </li>
