# Unsubscribe Link Finder 📧

This Python script helps you **automatically find and click unsubscribe links** in your email inbox. It scans your inbox for emails containing unsubscribe links and attempts to visit them to unsubscribe from unwanted mailing lists.

## Features 🌟

- Connects to **Gmail** using IMAP to search for emails with the word "unsubscribe" in the body.
- Extracts all unsubscribe links from the **HTML content** of those emails.
- Attempts to visit each link to help you unsubscribe. 🚪
- Saves all found unsubscribe links into a **text file** 📝 for later reference.

## Requirements

Before you start using this script, you’ll need to install the following Python libraries:

- `imaplib` (for email access)
- `email` (for parsing emails)
- `requests` (for making HTTP requests)
- `beautifulsoup4` (for extracting links from HTML)
- `python-dotenv` (for loading environment variables)

You can install the required libraries using `pip`:

```
pip install requests beautifulsoup4 python-dotenv
```
Additionally, you'll need to have a .env file in the project directory containing your Gmail login credentials. 🔑

Example .env file:
```
EMAIL=your_email@gmail.com
PASSWORD=your_email_password
```
## How It Works 🛠️

- Login to Gmail: The script logs into your Gmail account using the credentials from your .env file. 🔒
- Search for Unsubscribe Emails: It searches for emails that contain the word "unsubscribe" in the body. 🔍
- Extract Links: The script extracts all unsubscribe links from the email's HTML content. 
- Visit Links: It tries to visit each unsubscribe link to help you unsubscribe from those lists. 
- Save Links: All found unsubscribe links are saved to a file called links.txt. 📂

## Usage 🚀
- Clone the repository or download the script to your local machine. 💻
- Set up your Gmail credentials in the .env file.
- Run the script:
```
python unsubscribe_finder.py
```
## Output 📊
- The script will print all found unsubscribe links in the terminal.
- It will also save these links in a file called links.txt for later reference.
## Example Output:
```
Successfully visited https://unsubscribe-link1.com ✅
Failed to visit https://unsubscribe-link2.com - error code 404 ❌
Successfully visited https://unsubscribe-link3.com ✅
Links saved to links.txt 📑

```
## Notes 📌

- Gmail "Less Secure Apps": If you are using a standard Gmail account, ensure you’ve enabled access for less secure apps, or if you use two-factor authentication, create and use an app password instead.
- Other Email Providers: The script currently works with Gmail but can be adapted for other email providers by modifying the IMAP server settings.
- Unsubscribe Links Location: The script assumes that unsubscribe links are embedded in the HTML content of the email body.


