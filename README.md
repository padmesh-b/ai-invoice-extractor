# AI Invoice Extractor

A simple web application that uses Google Gemini AI to analyze invoice images and answer user queries. The app allows users to upload an invoice and interact with it through natural language.

---

## Overview

This project demonstrates how generative AI can be applied to real-world documents like invoices.
Users can upload an image and ask questions such as total amount, date, or vendor details, and the system responds based on the content of the invoice.

---

## Features

* Upload invoice images (JPG, PNG)
* Ask questions about invoice data
* AI-powered responses using Gemini
* Clean and interactive interface with Streamlit

---

## Tech Stack

* Python
* Streamlit
* Google Gemini API
* Pillow
* python-dotenv

---

## Project Structure

```
ai-invoice-extractor/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Running the Project Locally

1. Clone the repository:

```
git clone https://github.com/your-username/ai-invoice-extractor.git
cd ai-invoice-extractor
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Add your API key in a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

4. Run the app:

```
streamlit run app.py
```

---

## Deployment

The application can be deployed using Streamlit Community Cloud by connecting the GitHub repository and adding the API key as an environment variable.

---

## Future Improvements

* Extract structured fields (invoice number, date, total)
* Add download option (CSV/Excel)
* Improve UI design
* Support multiple document formats

---


