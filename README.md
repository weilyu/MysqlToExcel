# MysqlToExcel
A tool to export data from mysql and convert to excel file. The sheet names will be table names and the first row will contain column names.

## How to use it?
1. Install a python interpreter. Visit https://www.python.org/ and download the latest stable version for your os. Check the checkbox which shows "add pip to PATH".
2. Open terminal, and run the following commands
	```
	pip install -r requirements.txt
	```
3. Change the configuration by editing the settings.json file. Then the names of tables you want to export. 
4. cd to this folder, run 'python3 mysql_to_excel', then a test.xlsx file will be generated, which contains all the data you need. 

# テストデータ導出ツール
MySQLで作ったデータをExcelファイルとして導出するツールです。
Excelファイル仕様：
シート名：テーブル名
１行目：カラムの物理名
２行目以降：データ

## 使い方
1. Pythonをインストール（https://www.python.org/downloads/）
2. Windowsの場合、install_dependencies.batファイルを実行する。それ以外の場合、ターミナルでこのフォルダーを開けて、下記コマンドを実行する。
	```
	pip install -r requirements.txt
	```
3. settings.jsonファイルのDB情報を設定する。
4. ターミナルで```python3 mysql_to_excel```コマンドを実行する。
