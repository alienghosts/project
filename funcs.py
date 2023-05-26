import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import patoolib
from pathlib import Path
import os
import shutil
import glob


def download_folder(number):
    if os.path.exists('Распакованный архив'):
        shutil.rmtree('Распакованный архив')
    link = 'https://rosstat.gov.ru/compendium/document/13265'
    link2 = 'https://rosstat.gov.ru'
    request = requests.get(link)
    soup = BeautifulSoup(request.text, 'html.parser')
    links = []
    for l in soup.find_all('a'):
        if l.get('href') and l.get('href').endswith('.rar'):
            links.append(l.get('href'))
    rar_link = link2 + links[number - 1]
    file_name = rar_link.split('/')[-1]
    rar_r = requests.get(rar_link)
    with open(file_name, 'wb') as f:
        f.write(rar_r.content)
    rar_name = file_name
    os.mkdir('Распакованный архив')
    test_folder_name = 'Распакованный архив'
    patoolib.extract_archive(rar_name,
                             outdir=Path().absolute() / test_folder_name)
    for file_name in os.listdir():
        if file_name.endswith('.rar'):
            os.remove(file_name)


def painting():
    address = str(glob.glob('**/*1.1.xlsx', recursive=True))
    table_name = 'Таб. 1.1.xlsx'
    test_folder_name = 'Распакованный архив'
    filename = ''
    for root, dirs, files in os.walk(test_folder_name):
        for file in files:
            if file.endswith(table_name):
                filename = os.path.join(root, file)
                break

        if filename:
            break

    excel_data_df = pd.read_excel(filename,
                                  decimal=',', index_col=None)
    columns = ['Сводные таблицы', 'Unnamed: 6']
    rows = [i for i in range(6, len(excel_data_df))]
    filtered_data = excel_data_df.loc[rows][columns].reset_index(drop=True)
    filtered_data.columns = [excel_data_df.iloc[5][0],
                             excel_data_df.iloc[3][6]]
    filtered_data.plot.bar(x='Всего', )
    plt.show()
