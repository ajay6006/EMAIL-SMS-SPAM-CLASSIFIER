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
| Model                      | Accuracy | Precision | Recall | F1-Score |
|---------------------------|----------|------------|--------|---------|
| Naïve Bayes                | **98.2%**  | **97.6%**   | **96.8%** | **97.2%** |
| Logistic Regression (Tuned) | **98.2%**  | **99.2%**   | **87.0%** | **92.5%** |

## 📌 Key Findings  
✔️ **Spam messages are usually longer**, containing promotional words and links.
✔️ **Naive Bayes performed well** due to its efficiency in text classification.
✔️ **But after Hyperparameter tuning improved Logistic Regression**, increasing accuracy to **98.2%** and precision increased to **99.2%** which helps us in not lossing any important messages. 


