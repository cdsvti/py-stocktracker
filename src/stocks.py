import requests
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from excel import save_to_excel
from func import *
from logconfig import logger  # Import the logger from logconfig.py

def extract_ticker(response_text):
    pattern_name = r'<span itemprop="name">([^<]+)</span>'
    matches_name = re.findall(pattern_name, response_text)

    if matches_name and len(matches_name) >= 3:
        # Accessing the value from the 3rd occurrence
        return matches_name[2].strip()
    else:
        return None

def extract_data_values(response_text):
    # Use regex to extract all values inside <strong class="value">
    pattern1 = r'<strong class="value">\s*([^<]+)\s*</strong>'
    pattern2 = r'<strong class="value d-block lh-4 fs-4 fw-700">\s*([^<]+)\s*</strong>'

    matches1 = re.findall(pattern1, response_text)
    matches2 = re.findall(pattern2, response_text)
    #print("matches1: ",matches1)
    if matches1 and matches2:
        return [matches1[0].strip(), matches1[1].strip(), matches1[2].strip(), matches1[3].strip(), matches1[4].strip(), matches2[0].strip(), matches2[1].strip(), matches2[3].strip(),matches1[25].strip()]
    else:
        return None
       
def process_ticker(ticker):
    url = f'https://statusinvest.com.br/acoes/{ticker}'
    site_name = re.search(r'https://(.*?)/', url).group(1)
    response_text = get_webpage_data(site_name,url)
    
    if response_text:
        ticker_name = extract_ticker(response_text)
        if ticker_name:
            data_values = extract_data_values(response_text)
            if data_values:
                return [ticker_name, *data_values]
            else:
                logger.warning(f"No values found for {ticker_name} on the webpage.")
        else:
            logger.warning(f"Not enough occurrences of <span itemprop='name'></span> found for {ticker} on the webpage.")            
    else:
        logger.warning(f"Failed to fetch the ticker: {ticker}")
    return None
    
if __name__ == "__main__":
    # Set the locale for Brazilian Portuguese
    logger.info(f"Processing start.")
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    category = "stocks"
    tickers = read_tickers_from_file(category + '.txt')
    logger.info(f"Fetching stocks: {tickers}")
    
    data_list = [["TICKER", "VALOR ATUAL", "MIN. 52 SEMANAS", "MÁX. 52 SEMANAS", "DIVIDEND YIELD", "VALORIZAÇÃO (12M)", "D.Y.", "P/L", "P/VP","SEGMENTO DE ATUACAO"]]

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_ticker, ticker) for ticker in tickers]
        for future in as_completed(futures):
            result = future.result()
            if result:
                data_list.append(result)

    if len(data_list) > 1:  # Check if any data was collected
        save_to_excel(category,data_list)

    else:
        logger.warning(f"No data collected. Excel file not generated.")


    end_time = time.time()
    processing_time = end_time - start_time
    logger.info(f"Processing time: {processing_time:.2f} seconds")