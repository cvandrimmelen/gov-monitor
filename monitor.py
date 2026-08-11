# monitor.py

import json
import os
import requests
import smtplib

from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SEEN_FILE = "data/seen_links.json"
  
SITES = {  
"City of Albany": "https://albanyoregon.gov/calendar",
  "Linn County": "https://linncountyor.gov/meetings",
  "GAPS": https://meetings.boardbook.org/Public/Organization/2005"
}

with open(SEEN_FILE, "r") as f:
  seen = set(json.load(f))

new_links = []

for source, url in SITES.items():

  html = requests.get(url, timeout=30).text

  soup = BeautifulSoup(html, html.parser")

for link in soup.find_all("a", href=True):

  href=link["href"]

if (
  ".pdf" in href.lower()
  or "agenda" in href.lower()
  or "meeting" in href.lower()
):
  
  if href not in seen:
    new_links.append(
      {
"source": source,
        "url": href
      }
    )
    seen.add(href)

with open(SEEN_FILE, "w") as f:
  json.dump(list(seen), f, indent=2)

print(f"Found {len(new_links)} new items")

for item in new_links:
  print(item)
