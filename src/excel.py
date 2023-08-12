import time
import os
import openpyxl
from func import convert_to_decimal
from logconfig import logger

    
def save_to_excel(category,data_list):
    current_date = time.strftime("%Y%m%d%H")
    data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))
    excel_filename = f"{category}-{current_date}.xlsx"
    excel_filepath = os.path.join(data_folder, excel_filename)
    
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    wb = openpyxl.Workbook()
    ws = wb.active

    # Separate the header row from the data
    header_row = data_list[0]
    data_rows = data_list[1:]

    # Sort data_rows by the "TICKER" column (first column)
    sorted_data = sorted(data_rows, key=lambda row: row[0])

    # Append the header row and sorted rows to the worksheet
    ws.append(header_row)
    for row_data in sorted_data:
        ws.append([convert_to_decimal(value) for value in row_data])
    wb.save(excel_filepath)
    logger.info(f"Saving data in: {excel_filepath}")