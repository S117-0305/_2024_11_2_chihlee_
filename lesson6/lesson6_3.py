from openpyxl import load_workbook, workbook, worksheet
from pprint import pprint

def get_aqi(excel_name:str)-> list[dict]:
    wb:workbook = load_workbook("aqi.xlsx")
    from pprint import pprint
    sheet:worksheet = wb.worksheets[0]
    sheets:list = []
    column_names:list[str]=[cell.value for cell in list(sheet)[0]]
    for row in list(sheet)[1:]:
        site:dict = {column_names[idx]:cell.value for idx,cell in enumerate(row)}    
        sheets.append(site)

    return sheets

def main():
    data:list[dict] = get_aqi(excel_name="aqi.xlsx")
    pprint(data)

if __name__ == "__main__":
    main()
