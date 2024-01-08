import pandas as pd

__all__ = ['submitForm']

def submitForm():
    print('hello actors')

def startRegistration(variableExcelPath):
    df = pd.read_excel(variableExcelPath)
    rowMap = {}

    for index, row in df.iterrows():
        rowMap[row['No.']] = {
        '제품URL': row['제품URL'],
        '사이즈': row['사이즈'],
        '등록희망 수량': row['등록희망 수량']
    }
        
    print(rowMap)