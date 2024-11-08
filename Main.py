import os
import imaplib
import email
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


def click_link(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print("Succesfully visited", link)
        else:
            print("Failed to visit", "error code", response.status_code)
    except Exception as e:
        print("Error with", link, str(e))


def conect_to_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    return mail

def extract_link_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    links = [link["href"] for link in soup.find_all("a", href=True) if "unsubscribe" in link["href"].lower()]
    return links


def search_for_email():
    mail = conect_to_mail()
    _, search_data = mail.search(None, '(BODY "unsubscribe")')
    data = search_data[0].split()

    links = []
    
    
    for num in data:
        _, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    html_content = part.get_payload(decode=True).decode(errors="ignore")
                    links.extend(extract_link_from_html(html_content))
        else:
            content_type = msg.get_content_type()
            content = msg.get_payload(decode=True).decode(errors="ignore")
            if content_type == "text/html":
                links.extend(extract_link_from_html(content))


    mail.logout()

    return links 

def saved_links(links):
    with open("links.txt", "w") as f:
        f.write("\n".join(links))

               
links = search_for_email()

print(links)
for link in links:
    click_link(link)

saved_links(links)

