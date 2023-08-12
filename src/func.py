import locale
import os
import requests
from html import unescape

def convert_to_decimal(value):
    try:
        if "%" in value:
            value = value.replace("%", "").strip()
            return locale.atof(value) / 100
        else:
            return locale.atof(value)
    except Exception as e:
        return value
    
def read_tickers_from_file(filename):
    tickers = []
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            tickers.append(line.strip())
    return tickers

def get_webpage_data(site_name,url):
    payload = ""
    headers = {
        'authority': site_name,
        'cache-control': "max-age=0",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'sec-fetch-site': "none",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    if response.status_code == 200:
        response_text = response.content.decode('utf-8')  # Decode the content as UTF-8
        return unescape(response_text)  # Decode HTML entities
    else:
        return None
