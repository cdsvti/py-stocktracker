# py-stocktracker

Welcome to py-stocktracker, a Python-based project for studying and analyzing stock data. Please note that this project is designed for educational and research purposes only. It does not provide investment recommendations or financial advice. The stock market is complex and subject to various factors that can influence stock prices and performance.

## Project Overview

The py-stocktracker project is aimed at providing users with tools to retrieve, analyze, and visualize daily stock parameters. The main components of the project include:

- `data/`: This directory is intended to store any data files related to stock,fiis and fiagro information.

- `src/`: The source code directory contains the main Python script `main.py`, which will serve as the entry point for the stock analysis functionality.

- `tests/`: This directory is dedicated to unit tests. You'll find the testing script `test_main.py` here.

- `stocks.txt,fiis.txt,fiagro.txt`: This contain tickers with brazilian B3 stocks.

- `stocks.py`: Stocks.

- `fiis.py`: FIIs - Real estate.

- `fiagro.py`: FIAGROS - Agribusiness investment.


## Disclaimer

It's important to emphasize that py-stocktracker is not a substitute for professional financial advice. The analysis and information provided by this project should not be considered as recommendations for making investment decisions. The stock market involves inherent risks and uncertainties that can lead to significant financial losses. Always conduct thorough research and consider consulting with a qualified financial advisor before making any investment choices.

## Usage

To use this project, you can follow these steps:

1. Clone or download this repository to your local machine.

2. Install any required dependencies by running:  

## Stocks:
Stocks, also known as shares or equities, represent ownership in a company. When you own a stock in a company, you become a shareholder and have a claim to a portion of the company's assets and profits. The value of stocks can fluctuate based on market conditions, company performance, economic factors, and investor sentiment. Investors buy and sell stocks on stock exchanges like B3, aiming to profit from price movements or to gain a stake in the company's growth.

## FIIs (Fundo de Investimento Imobiliário):
FIIs are Real Estate Investment Funds in Brazil. They operate as investment vehicles that pool money from multiple investors to invest in a diversified portfolio of income-generating real estate assets, such as commercial properties, shopping malls, office buildings, and residential properties. Investors in FIIs own units in the fund rather than direct ownership of the underlying properties. FIIs provide an avenue for individuals to invest in real estate without the need to purchase and manage physical properties.

## FIAGROS (Fundo de Investimento do Agronegócio):
FIAGROS is a type of Brazilian investment fund focused on the agribusiness sector. These funds invest in various agribusiness-related assets, such as agricultural production, processing, distribution, and trading activities. Similar to FIIs, FIAGROS allow investors to pool their capital to access the potential benefits of the agribusiness sector without the need for direct involvement in the operations.

It's important to note that the definitions provided here are general explanations. The specific terms and regulations related to stocks, FIIs, and investment funds may vary based on local laws and market conditions in Brazil. If you're considering investing in these areas, it's recommended to seek advice from financial professionals and conduct thorough research to understand the specifics of each investment type.

# Stock Tracker

This is a Python script for tracking stock data. It retrieves data about stock tickers from a specific website and saves the data to an Excel spreadsheet.

## Disclaimer

Please note that investing in stocks and financial instruments carries inherent risks. The information provided by this script is for informational purposes only and should not be considered financial advice. Before making any investment decisions, it's recommended to consult with a qualified financial professional and perform thorough research.

## Requirements

- Python 3.x
- Required Python packages: `requests`, `re`, `time`, `concurrent.futures`, `openpyxl`
- External modules: `excel.py`, `func.py`, `logconfig.py`

## Usage

1. Install the required Python packages using `pip`:
   ```
   pip install requests openpyxl
    ```

## Configuration
You can modify the test_main.py script to change the category of stocks being tracked or adjust other settings.

## License
This script is provided under the MIT License.

Feel free to customize the content and structure of the `README.md` file to better suit your project's needs. Additionally, make sure to adjust the filenames and directory paths as necessary to match your project's structure.