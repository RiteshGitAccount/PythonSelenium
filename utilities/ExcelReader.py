import openpyxl


def get_excel_file_sheet_object(file_path, sheet_name):
    """
    This will read the Excel file from provided path
    and return requested sheet details as object
    :param file_path:
    :param sheet_name:
    :return:
    """
    wb_obj = openpyxl.load_workbook(file_path)
    return wb_obj[sheet_name]


def read_excel_data(file_path, sheet_name, col_row):
    """
    This will read the Excel file from provided file path
    and will return the requested cell value from provided sheet
    :param file_path:
    :param sheet_name:
    :param col_row:
    :return:
    """
    sheet_obj = get_excel_file_sheet_object(file_path, sheet_name)
    value = sheet_obj[col_row.upper()].value
    if value is None:
        return ""
    else:
        return value


def write_excel_data(file_path, sheet_name, col_row, data):
    """
    This will write the data in requested cell of the provided Excel file in provided sheet
    :param file_path:
    :param sheet_name:
    :param col_row:
    :param data:
    :return:
    """
    wb_obj = openpyxl.load_workbook(file_path)
    sheet_obj = wb_obj[sheet_name]
    sheet_obj[col_row.upper()] = data
    wb_obj.save(file_path)
