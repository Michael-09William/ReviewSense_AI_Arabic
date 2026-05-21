# 🧠 ReviewSense AI - Arabic Sentiment Analysis Suite

ReviewSense AI هو نظام متكامل لتحليل مشاعر النصوص العربية والمراجعات (بالفصحى والعامية المصرية). يمثل هذا المشروع رحلة تطوير وتطور تبدأ من النماذج الإحصائية التقليدية وصولاً إلى النماذج اللغوية الكبيرة (LLMs)، مع واجهة مستخدم تفاعلية ومحلية بالكامل.

ReviewSense AI is a comprehensive Arabic Sentiment Analysis suite capable of processing both Modern Standard Arabic (MSA) and Egyptian Colloquial Arabic (ECA). This project showcases an engineering evolution from traditional statistical baselines to deep learning architectures and state-of-the-art Transformers, integrated into a fully local web application.

---

## 🌎 Language Selection / اختيار اللغة
- [English Version](#english-documentation)

---

# English Documentation

## 🚀 Project Overview & Evolution
The project didn't just stop at one model. It was engineered to test, benchmark, and compare three different eras of Machine Learning to see how they handle the complexities of the Arabic language:
1. **Logistic Regression (Baseline):** A fast, statistical approach using TF-IDF vectors.
2. **LSTM (Deep Learning):** A sequential neural network architecture implemented via TensorFlow/Keras to capture text dependencies.
3. **AraBERT v2 (State-of-the-Art Transformers):** Fine-tuned using PyTorch and Hugging Face, leveraging self-attention mechanisms to master context, sarcasm, and negation.

Initially trained and prototyped inside **Google Colab**, the pipeline was completely migrated to a structured local development environment using **VS Code** to build a robust, production-ready inference structure.

---

## 📁 Project Structure
```text
ReviewSense_AI/
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py  # Text cleaning & standardization functions
│   └── inference.py      # AraBERT runtime load & prediction engine
│
├── models/               # [Ignored in Git] Holds local model weights (.h5 & Transformer bins)
│
├── app.py                # Streamlit Premium UI (RTL & Dark Mode)
└── README.md             # Project Documentation

---

## 🛠️Tech Stack

-Core: Python 3.10+

-Transformers Engine: Hugging Face Transformers (aubmindlab/bert-base-arabertv02), PyTorch.

-Deep Learning Baseline: TensorFlow & Keras (LSTM Architecture).

-Machine Learning Baseline: Scikit-learn (Logistic Regression, TF-IDF Vectorization).

-Data Manipulation: Pandas, NumPy.

-Deployment & UI: Streamlit (Custom RTL HTML/CSS Injection).

---

##⚡ Challenges & Engineering Insights (Crucial Learnings)

### 1. The Data Imbalance Strategy

Challenge: Initial training phases suffered from class imbalance, which biased predictions toward the majority class.

Solution: Adjusted the data pipeline strategy to enforce a strict equal balance between positive and negative labels, ensuring unbiased training.


###2. The Binary vs. Neutral Class Oversight
Challenge: Designing the system strictly as a binary classifier (Positive/Negative) introduced an architectural oversight. Ambiguous or completely neutral statements forced the models to pick a side with false high confidence.

Insight: For future iterations, introducing a dedicated "Neutral" class is essential to map realistic human expressions.


### 3. Preprocessing Engineering & Custom Stopwords Challenge
* **Challenge:** Arabic text cleaning is highly nuanced. Standard NLP preprocessors often strip too much out of colloquial Egyptian text, while 
relying blindly on AraBERT's native `ArabertPreprocessor` didn't yield the absolute best results for our specific data distribution. Building an optimal custom cleaning function required handling specific challenges like manually curating a custom Arabic stop-words list to prevent dropping words that carry crucial emotional weights or regional context.

* **The Breakthrough (Defying Expectations):** While baseline benchmarks usually dictate using the native AraBERT preprocessor, our rigorous testing showed otherwise. The **Custom Preprocessing Function** we engineered achieved a **significantly higher accuracy** on our dataset compared to AraBERT's default preprocessor. This proved that tailored linguistic cleaning for local Egyptian dialects can outperform generic preprocessors even when dealing with large Transformer architectures.

---

### How to Run Locally

## 1.Clone and activate the Virtual Environment:   
    cd ReviewSense_AI
    # Activate environment (Windows)
    .\RevSen\Scripts\activate


## 2.Run Module Inference Test:
    python -m src.inference


## 3.Launch the Web App:
    streamlit run app.py

---
## EValuation

Image1: (RevSense.png)
Image2: (RS1.png)
Image3: (RS2.png)
Image4: (RS3.png)
Image5: (RS5.png)




