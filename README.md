# 📝 Text Summarizer App (LangChain + Hugging Face + Streamlit)

This is a web application built using **Streamlit**, **LangChain**, and **Hugging Face Hub**, designed to summarize long blocks of text clearly and concisely. It handles large input using LangChain’s chunking logic and generates meaningful summaries via a Hugging Face language model.

---

## 🔧 Features

- 🧠 Uses **LangChain LLMChain** to generate summaries
- 🤖 Powered by Hugging Face models like `google/flan-t5-small`
- 📚 Splits large text into smaller chunks for better results
- 🌐 Clean and simple **Streamlit UI**
- 🔐 Supports `.env` file for managing API keys
- ⚡ Fast and free to deploy using **Streamlit Cloud**

---

## ⚙️ Technologies Used

- **Python**
- **Streamlit**
- **LangChain**
- **Hugging Face Hub**
- **dotenv**

---

## 🧠 How LangChain is Used

- `LangChain` is used to create an LLMChain pipeline.
- It wraps a prompt template and a HuggingFace model (`flan-t5-small`) for summarization.
- Large input is split using LangChain’s `RecursiveCharacterTextSplitter`.

---

## 📦 Installation & Setup (Run Locally)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/text-summarizer-app.git
cd text-summarizer-app
