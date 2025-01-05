import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt_tab')
nltk.download('stopwords')


ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():  # is aplha numeric
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return ' '.join(y)

cv = pickle.load(open('cv.pkl', 'rb'))
model = pickle.load(open('BEST_MODEL.pkl', 'rb'))

st.title("SMS SPAM CLASSIFIER")

input_sms = st.text_input("Enter your message")

if st.button("Predict"):

# Preprocess
    transformed_sms  = transform_text(input_sms)

# Vectorize
    vector_input = cv.transform([transformed_sms]).toarray()

# Predict
    result = model.predict(vector_input)[0]

# Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")