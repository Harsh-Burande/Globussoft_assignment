# Face Authentication API & Amazon Product Scraper

## Overview

This repository contains solutions for two tasks:

### Task 1: Face Authentication API

A FastAPI-based application that compares two face images and determines whether they belong to the same person.

#### Features

* Upload two face images
* Face detection and embedding extraction using InsightFace
* Face similarity comparison using cosine similarity
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
Assignment-Submission/
│
├── task1_face_authentication/
│
├── task2_amazon_scraper/
│
├── sample_images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Assignment-Submission
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Task 1 - Face Authentication API

Navigate to the Face Authentication project folder:

```bash
cd task1_face_authentication
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
cd task2_amazon_scraper
```

Run the scraper:

```bash
python amazon_test.py
```

The extracted product information will be saved as a CSV file.

---

## Sample Images

Sample images for testing the Face Authentication API are included in the `sample_images` folder.

---

## Technologies Used

* Python
* FastAPI
* InsightFace
* OpenCV
* Scikit-Learn
* Selenium
* Pandas
