# 📧📱 Email & SMS Spam Detection  

## 🔍 Project Overview  
This project focuses on detecting **spam messages** in **emails and SMS** using **Natural Language Processing (NLP) and Machine Learning**. The model effectively classifies messages as **spam or ham (not spam)** using text-processing techniques and classification algorithms.  

## 🌐 Live Streamlit App  
Try the **live spam detection app** here:  
👉 **[Email & SMS Spam Classifier](https://sms-spam-classifier-aj.streamlit.app/)**  

## 📂 Dataset  
The dataset includes:  
- **Message text** (input)  
- **Spam/Ham label** (output)  

## ⚙️ Technologies Used  
- **Python** 🐍  
- **Pandas & NumPy** (Data Preprocessing)  
- **NLTK** (Text Processing)  
- **Scikit-learn** (Machine Learning)  
- **Matplotlib & Seaborn** (Data Visualization)  
- **Jupyter Notebook** (Development Environment)  
- **Streamlit** (Deployment)  

## 🔄 Workflow  
1️⃣ **Data Cleaning**: Removing duplicates, unnecessary columns, and renaming attributes.  
2️⃣ **Text Preprocessing**: Tokenization, stopword removal, stemming, and TF-IDF vectorization.  
3️⃣ **Feature Engineering**: Converting text data into numerical format for model training.  
4️⃣ **Model Training**: Implemented **Naïve Bayes, Logistic Regression, and Random Forest**.  
5️⃣ **Evaluation**: Assessed models using **accuracy, precision, recall, and F1-score**.  
6️⃣ **Deployment**: Hosted the model on **Streamlit** for real-time spam detection.  

## 📊 Model Performance  
| Model              | Accuracy | Precision | Recall | F1-Score |
|-------------------|----------|------------|--------|---------|
| Naïve Bayes        | **98.2%**  | **97.6%**   | **96.8%** | **97.2%** |
| Logistic Regression | **96.4%**  | **95.1%**   | **92.3%** | **93.6%** |

## 📌 Key Findings  
✔️ **Naïve Bayes performed best** due to its efficiency in text classification.  
✔️ **Naïve Bayes is the most suitable for real-time spam filtering due to speed & accuracy.**  

