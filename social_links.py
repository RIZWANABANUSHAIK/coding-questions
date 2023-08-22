import re
import requests
from bs4 import BeautifulSoup

def get_social_links(soup, base_url):
    social_links = []
    social_tags = soup.find_all("a", href=re.compile(r"(facebook|linkedin|twitter|instagram|youtube)\.com"))
    for tag in social_tags:
        link = tag['href']
        # If the link is relative, construct the absolute URL
        if not link.startswith("http"):
            link = base_url + link
        social_links.append(link)
    return social_links

def get_emails(soup):
    emails = []
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    for tag in soup.find_all(string=re.compile(email_pattern)):
        email = re.search(email_pattern, tag)
        if email:
            emails.append(email.group())
    return emails

def get_contact_numbers(soup):
    contact_numbers = []
    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    for tag in soup.find_all(string=re.compile(phone_pattern)):
        phone = re.search(phone_pattern, tag)
        if phone:
            contact_numbers.append(phone.group())
    return contact_numbers

def main():
    website_url = input("Enter the website URL: ")
    response = requests.get(website_url)
    
    if response.status_code == 200:
        base_url = website_url
        if '/' in website_url:
            base_url = website_url[:website_url.index('/', 8) + 1]  # Find and include the domain part
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        social_links = get_social_links(soup, base_url)
        print("Social links -")
        for link in social_links:
            print(link)
        
        emails = get_emails(soup)
        print("Emails -")
        for email in emails:
            print(email)
        
        contact_numbers = get_contact_numbers(soup)
        print("Contact:")
        for number in contact_numbers:
            print(number)
    else:
        print("Failed to fetch the website content.")

if __name__ == "__main__":
    main()
