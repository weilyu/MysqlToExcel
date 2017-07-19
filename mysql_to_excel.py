import pymysql
import json
import openpyxl

settings = json.loads(open('settings.json', encoding='utf-8').read())
host = settings['host']
port = settings['port']
user = settings['user']
password = settings['password']
database = settings['database']
connection = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
tables = settings['tables']
workbook = openpyxl.Workbook()
with connection.cursor() as cursor:
    for table in tables:
        worksheet = workbook.create_sheet(table)
        get_col_names_sql = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s"
        count_col = cursor.execute(get_col_names_sql, (database, table))
        col_names = cursor.fetchall()
        get_data_sql = 'select * from ' + table
        cursor.execute(get_data_sql)
        data = cursor.fetchall()
        for i in range(len(col_names)):
            worksheet.cell(row=1, column=i + 1).value = col_names[i][0]
        for row in range(len(data)):
            for col in range(count_col):
                worksheet.cell(row=row + 2, column=col + 1).value = data[row][col]
workbook.remove(workbook.active)
workbook.save('test.xlsx')
