# MysqlToExcel
A tool to export data from mysql and convert to excel file. The sheet names will be table names and the first row will contain column names.

## How to use it?
1. Install a python interpreter. Visit https://www.python.org/ and download the latest stable version for your os. Check the checkbox which shows "add pip to PATH".
2. Open terminal, and run the following commands
	pip install -r requirements.txt
3. Change the configuration by editing the settings.json file. Then the names of tables you want to export. 
4. cd to this folder, run 'python mysql_to_excel', then a test.xlsx file will be generated, which contains all the data you need. 
