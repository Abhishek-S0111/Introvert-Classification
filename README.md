# 🧠 Introvert Classification – Are You a Ghost or a Party Animal?

Welcome to the most unnecessarily accurate model you've ever seen — one that tries to decide whether you're an **introvert** or **extrovert** based on a few simple questions.

We used machine learning (because obviously) and wrapped it up in a clean Streamlit app so you can get judged in real-time.

## 🔍 What It Does

You answer a short set of personality-related questions, and our model tells you:

> "Yep, you're a certified introvert."  
> or  
> "You probably talk to strangers at bus stops."

## 🛠 Tech Stack

- 🐍 Python  
- 🤖 Scikit-learn and XGBoost (model building)  
- 📊 Pandas & NumPy (data wrangling)  
- 🎯 Streamlit (app deployment)  
- 🎨 Sarcasm (a constant throughout)

## 🚀 Try It Out

🔗 [Streamlit App Link](https://introvert-classification.streamlit.app/)  

Or run it locally:

```bash
git clone https://github.com/Abhishek-S0111/Introvert-Classification.git
cd Introvert-Classification
pip install -r requirements.txt
streamlit run app.py
```

## 📂 Project Structure

```
📦Introvert-Classification
├── code/i-wonder-what-i-am.ipynb                # Kaggle notebook containing ML pipeline
├── app.py                                       # Streamlit app(local)
├── model/introvert_classifier_model.pkl         # Trained classification model
├── data/train.csv                               # Training Data
  ─ data/test.csv                                # Testing Data(Validation Set)
├── requirements.txt                             # Required packages
├── streamlit-deployement/App.py                 # Streamlit app (global)
  ─ streamlit-deployement/requirements.txt  
└── README.md                                    # Whatever you're looking at

```