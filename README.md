# Unsubscribe Link Finder

A Python script that automatically finds and clicks unsubscribe links in your email inbox. It scans your Gmail inbox for emails containing unsubscribe links and attempts to visit them to help you unsubscribe from unwanted mailing lists.

---

## Features

- **IMAP Access**: Connects to Gmail using IMAP to search for emails containing the word "unsubscribe" in the body.
- **HTML Parsing**: Extracts all unsubscribe links from the HTML content of emails.
- **Link Interaction**: Attempts to visit each unsubscribe link to unsubscribe from unwanted mailing lists.
- **Link Storage**: Saves all found unsubscribe links into a text file (`links.txt`) for later reference.

---

## Requirements

Before running the script, make sure you have the following Python libraries installed:

- `imaplib` (for email access)
- `email` (for parsing emails)
- `requests` (for making HTTP requests)
- `beautifulsoup4` (for extracting links from HTML)
- `python-dotenv` (for loading environment variables)

You can install these dependencies using `pip`:

```bash
pip install requests beautifulsoup4 python-dotenv

