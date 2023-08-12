import requests
import re
import time
import os
import openpyxl
from concurrent.futures import ThreadPoolExecutor
import locale
from html import unescape
import logging

# Configure logging
current_date = time.strftime("%Y%m%d")
log_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../log"))
log_filename = f"stocks-{current_date}.log"
log_filepath = os.path.join(log_folder, log_filename)
    
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
        
logging.basicConfig(filename=log_filepath, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

HEADERS = {
    'User-Agent': "Your User-Agent String",
    'Accept': "Your Accept String",
    'Accept-Language': "Your Accept-Language String"
}

def convert_to_decimal(value):
    try:
        if "%" in value:
            value = value.replace("%", "").strip()
            return locale.atof(value) / 100
        else:
            return locale.atof(value)
    except Exception as e:
        return value
    
def get_webpage_data(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        response_text = response.content.decode('utf-8')
        return unescape(response_text)
    else:
        return None

def extract_data_values(response_text):
    pattern1 = re.compile(r'<strong class="value">\s*([^<]+)\s*</strong>')
    pattern2 = re.compile(r'<strong class="value d-block lh-4 fs-4 fw-700">\s*([^<]+)\s*</strong>')

    matches1 = pattern1.findall(response_text)
    matches2 = pattern2.findall(response_text)
    print("matches1: ",matches1)
    if matches1 and matches2:
        return [value.strip() for value in matches1[:5]] + [value.strip() for value in matches2[:3]] + [matches1[25].strip()]
    else:
        return None

def extract_ticker(response_text):
    pattern_name = r'<span itemprop="name">([^<]+)</span>'
    matches_name = re.findall(pattern_name, response_text)

    if matches_name and len(matches_name) >= 3:
        # Accessing the value from the 3rd occurrence
        return matches_name[2].strip()
    else:
        return None

def process_ticker(ticker):
    url = f'https://statusinvest.com.br/acoes/{ticker}'
    response_text = get_webpage_data(url)
    
    if response_text:
        ticker_name = extract_ticker(response_text)
        if ticker_name:
            data_values = extract_data_values(response_text)
            if data_values:
                return [ticker_name, *data_values]
            else:
                logging.warning(f"No values found for {ticker_name} on the webpage.")
        else:
            logging.warning(f"Not enough occurrences of <span itemprop='name'></span> found for {ticker} on the webpage.")
    else:
        logging.error(f"Failed to fetch the webpage for {ticker}.")
    return None

def read_tickers_from_file(filename):
    tickers = []
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            tickers.append(line.strip())
    return tickers

if __name__ == "__main__":
    start_time = time.time()
    tickers = read_tickers_from_file("stocks.txt")
    data_list = [["TICKER", "VALOR ATUAL", "MIN. 52 SEMANAS", "MÁX. 52 SEMANAS", "DIVIDEND YIELD", "VALORIZAÇÃO (12M)", "D.Y.", "P/L", "P/VP", "SEGMENTO DE ATUACAO"]]

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_ticker, tickers))
        data_list.extend(result for result in results if result)

    if len(data_list) > 1:
        current_date = time.strftime("%Y%m%d")
        excel_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))
        excel_filename = f"stocks-{current_date}.xlsx"
        excel_filepath = os.path.join(excel_folder, excel_filename)

        if not os.path.exists(excel_folder):
            os.makedirs(excel_folder)

        wb = openpyxl.Workbook()
        ws = wb.active

        header_row = ["TICKER", "VALOR ATUAL", "MIN. 52 SEMANAS", "MÁX. 52 SEMANAS", "DIVIDEND YIELD", "VALORIZAÇÃO (12M)", "D.Y.", "P/L", "P/VP", "SEGMENTO DE ATUACAO"]
        ws.append(header_row)

        for row_data in data_list[1:]:
            ws.append([convert_to_decimal(value) for value in row_data])

        wb.save(excel_filepath)
        logging.info(f"Data saved to {excel_filepath}.")
    else:
        logging.warning("No data collected. Excel file and instructions document not generated.")

    end_time = time.time()
    processing_time = end_time - start_time
    print(f"Processing time: {processing_time:.2f} seconds")