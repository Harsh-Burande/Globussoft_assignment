# Face Authentication API & Amazon Product Scraper

## Overview

This repository contains solutions for two tasks:

### Task 1: Face Authentication API

A FastAPI-based application that compares two face images and determines whether they belong to the same person.

#### Features

* Upload two face images
* Face detection and embedding extraction using InsightFace
* Face similarity comparison using cosine similarity
* Returns whether the faces belong to the same person
* REST API built with FastAPI

---

### Task 2: Amazon Product Scraper

A Selenium-based web scraper that extracts product information from Amazon search results.

#### Extracted Information

* Product Name
* Price
* Rating
* Product Image URL

The scraped data is stored in CSV format for further analysis.

---

## Project Structure

```text
Globussoft/
│
├── face_recognition/
│   ├── images/
│
├── web_scraping/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Harsh-Burande/Globussoft_Assignment.git
cd Globussoft
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Task 1 - Face Authentication API

Navigate to the Face Authentication project folder:

```bash
cd face_recognition
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

Use the Swagger UI to test the face comparison endpoint.

---

## Running Task 2 - Amazon Product Scraper

Navigate to the scraper folder:

```bash
cd web_scraping
```

Run the scraper:

```bash
python amazon_test.py
```

The extracted product information will be saved as a CSV file.

---

## Sample Images

Sample images for testing the Face Authentication API are available in:

```text
face_recognition/images/
```

These images can be used to test both matching and non-matching face comparisons.

---

## Technologies Used

* Python
* FastAPI
* InsightFace
* OpenCV
* Scikit-Learn
* Selenium
* Pandas

---

## Notes

* Install all required dependencies using the provided `requirements.txt` file.
* Ensure Chrome browser is installed for the Amazon scraper.
* Sample images are included for testing the Face Authentication API.
