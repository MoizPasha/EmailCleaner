# Teams Email Reminder Scraper

This repository provides a Python-based scraper that extracts the **title** and **main message body** from **Microsoft Teams message reminder emails** using `inline CSS attributes`. It is designed to work on a dataset of HTML pages previously scraped from an email mailbox.

## 🧾 Features

- Extracts Message:
  - **title**
  - **content**
- Processes datasets of raw HTML email content

## 📁 Dataset Format

The input dataset should consist of HTML files representing different email pages (e.g., exported or scraped from a mailbox). Each file should follow the format of a Microsoft Teams meeting reminder email.

## 🚀 Getting Started

### Prerequisites


Install the required Python packages using:

- Python 3.7+
```bash
pip install beautifulsoup4
