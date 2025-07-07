# Haram Library Chatbot 🤖📚

A smart bilingual chatbot for the Haram Library, built using [Rasa](https://rasa.com/) and [FastAPI].  
This project allows users to ask questions in Arabic or English and get instant responses about the library's services.

---

## 📌 Features

- Supports **Arabic and English**
- Answers real **library FAQs** (28 questions)
- Simple **web interface** with instant messaging
- Built with open-source tools
- Easy to test, use, and expand

---

## 🛠 Technologies Used

- Rasa 3.6.21
- FastAPI
- Python 3.10.18
- SpaCy (`xx_ent_wiki_sm`)
- aiohttp
- uvicorn

---

## ⚙ Requirements

Install these Python packages:

```bash
pip install fastapi aiohttp uvicorn rasa==3.6.21 spacy
```

Download the spaCy multi-language model:

```bash
python -m spacy download xx_ent_wiki_sm
```

---

## 🚀 How to Run

1. **Train the Rasa model**:

```bash
rasa train
```

2. **Run Rasa server**:

```bash
rasa run
```

3. **Run the FastAPI web server**:

```bash
uvicorn app:app --reload
```

4. Open your browser and go to:  
`http://localhost:8000`

---

## 📁 Project Structure

```
haram-library-chatbot/
├── actions/
│   └── actions.py                  # Custom actions 
├── app.py                          # FastAPI web interface
├── config.yml                      # Rasa pipeline configuration
├── credentials.yml                 # Rasa channels configuration
├── domain.yml                      # Intents, actions
├── endpoints.yml                   # Action server and tracker settings
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python version
├── .gitignore                      # Git ignore file
├── static/
│   ├── logo.jpg                    # Library logo
│   └── notification.mp3           # Notification sound
├── models/                         # Trained Rasa models
├── tests/                          # Test files (if any)
├── __pycache__/                    # Python cache
├── data/
│   ├── nlu.yml                     # Intents and examples
│   ├── rules.yml                   # Rasa rules
│   └── stories.yml                 # Conversation stories
└── README.md                       # Project documentation
```

---

## 📣 Authors

- **Renad Alshamrani**  
- **Sarah Alshamrani**

---

## 🙏 Special Thanks

Thanks to **Haram Library** for their support, guidance, and real-world data that helped shape this project.
