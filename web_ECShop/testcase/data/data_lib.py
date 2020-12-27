


def read_text(file_name = "./users.txt"):
    with open(file_name,'r+',encoding='utf-8') as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            usersinfo = line.split(" ")
    return  usersinfo
read_text()


import csv
def read_csv(file_name = "./login_user.csv"):
    datas = []
    with open(file_name,'r',encoding='utf-8') as file:
        lines = csv.reader(file)
        for line in lines:
            datas.append(line)
    return  datas
# data = read_csv()
print(read_csv())

import xlrd
def read_excel(file_name="./info.xlsx", sheet_name="login.xlsx"):
    data = []
    book = xlrd.open_workbook(file_name)  # open_workbook打开工作簿
    sheet = book.sheet_by_name(sheet_name)
    rows = sheet.nrows  # 所有行
    cols = sheet.ncols  # 所有列
    print(rows, cols)
    # 遍历行
    for row in range(1, rows):
        row_content = sheet.row_values(row)
        row_content[1] = str(int(row_content[1]))
        data.append(row_content)
    return data
print(read_excel())




