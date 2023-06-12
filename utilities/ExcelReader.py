import openpyxl


def get_excel_file_sheet_object(file_path, sheet_name):
    wb_obj = openpyxl.load_workbook(file_path)
    return wb_obj[sheet_name]


def read_excel_data(file_path, sheet_name, col_row):
    sheet_obj = get_excel_file_sheet_object(file_path, sheet_name)
    value = sheet_obj[col_row.upper()].value
    if value is None:
        return ""
    else:
        return value


def write_excel_data(file_path, sheet_name, col_row, data):
    wb_obj = openpyxl.load_workbook(file_path)
    sheet_obj = wb_obj[sheet_name]
    sheet_obj[col_row.upper()] = data
    wb_obj.save(file_path)
