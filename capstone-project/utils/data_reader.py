"""
Data-driven testing helpers.
Step 8 of the business flow: Read test data from Excel/JSON.
"""
import json
import uuid

import openpyxl

from config import config


def read_json_data(path: str = None) -> dict:
    """Load structured test data (account/user info, product list) from JSON."""
    path = path or config.JSON_DATA_FILE
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Emails must be unique per run on automationexercise.com, otherwise
    # signup fails with "Email Address already exist!". We generate a
    # fresh one each run but keep the rest of the JSON data intact.
    unique_suffix = uuid.uuid4().hex[:8]
    data["account"]["email"] = f"pratik.qa.{unique_suffix}@example.com"
    return data


def read_excel_data(path: str = None, sheet_name: str = "SearchData") -> list:
    """
    Read row-wise test data (search terms / expected quantities) from an
    Excel sheet and return it as a list of dicts, e.g.:
    [{'TestCaseID': 'TC01', 'SearchTerm': 'Dress', 'ExpectedQuantity': 3}, ...]
    """
    path = path or config.EXCEL_DATA_FILE
    workbook = openpyxl.load_workbook(path, data_only=True)
    sheet = workbook[sheet_name]

    rows = list(sheet.iter_rows(values_only=True))
    headers, records = rows[0], rows[1:]

    return [dict(zip(headers, row)) for row in records if any(row)]
