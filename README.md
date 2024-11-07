Unsubscribe Link Finder
This Python script helps you automatically find and click unsubscribe links in your email inbox. It scans your inbox for emails containing unsubscribe links and attempts to visit them to unsubscribe from unwanted mailing lists.

Features:
Connects to Gmail using IMAP to search for emails with the word "unsubscribe" in the body.
Extracts all unsubscribe links from HTML content of those emails.
Attempts to visit each link to help you unsubscribe.
Saves all found unsubscribe links into a text file for later reference.
Requirements
Before you start using this script, you'll need to install the following Python libraries:

imaplib (for email access)
email (for parsing emails)
requests (for making HTTP requests)
beautifulsoup4 (for extracting links from HTML)
python-dotenv (for loading environment variables)
You can install them using pip:

bash
Copy code
pip install requests beautifulsoup4 python-dotenv
Additionally, you need to have a .env file in the project directory that contains your Gmail login credentials.

Example .env file:
env
Copy code
EMAIL=your_email@gmail.com
PASSWORD=your_email_password
How It Works
Login to Gmail: The script logs into your Gmail account using the credentials from your .env file.
Search for Unsubscribe Emails: It searches for emails that contain the word "unsubscribe" in their body.
Extract Links: It finds all unsubscribe links from the emails.
Visit Links: The script tries to visit each unsubscribe link to unsubscribe you from those lists.
Save Links: All found unsubscribe links are saved to a file called links.txt.
Usage
Clone the repository or download the script to your local machine.
Set up your Gmail credentials in the .env file.
Run the script.
bash
Copy code
python unsubscribe_finder.py
Output
The script will print all found unsubscribe links in the terminal.
It will also save these links in a file called links.txt for later reference.
Example Output
bash
Copy code
Successfully visited https://unsubscribe-link1.com
Failed to visit https://unsubscribe-link2.com error code 404
Successfully visited https://unsubscribe-link3.com
Links saved to links.txt
Notes
Make sure to enable "Less Secure Apps" or use an "App Password" if you have two-factor authentication enabled on your Gmail account.
The script currently works with Gmail but can be adapted for other email providers by modifying the IMAP server settings.
The script assumes that the unsubscribe links are in the body of the email, typically in the HTML content.
