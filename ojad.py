from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import shutil
import time
#import os

import csv


options = Options()
options.add_argument("--headless")

#expression = 'それは、不思議な夢だった。'
#expression = 'しかも、こんな重たいリュックと4リットルの水を背負って、この2倍もある場所まで行くってか？は～」と、大げさに深いため息をついた。しかも、こんな重たいリュックと4リットルの水を背負って、この2倍もある場所まで行くってか？は～」と、大げさに深いため息をついた。'

driver = webdriver.Chrome(options=options)
driver.get("https://www.gavo.t.u-tokyo.ac.jp/ojad/eng/phrasing/index")



def getScreenshot(expression):

    #driver = webdriver.Chrome(os.getcwd() +"\chromedriver.exe")

    searchField = driver.find_element(By.ID, "PhrasingText")
    searchField.send_keys(Keys.CONTROL+"A")
    searchField.send_keys(Keys.DELETE)
    searchField.send_keys(expression)

    analyzeButton = driver.find_element(By.CSS_SELECTOR, '[value="Analyze"]')
    analyzeButton.click()

    pitchDiagram = driver.find_element(By.ID, "phrasing_main")
    pitchDiagram.screenshot(expression + '.png')
    print(expression + '.png')

    #shutil.move(expression + '.png', 'C:\\Users\\xelak\\OneDrive\\Personal\\02_Learning\\Python\\OJAD_extractor\\Screenshots\\' + expression + '.png') # 
    
    #



#Get the expression from the csv file
def getExpressions():
    #UTF8 , column 8
    with open('pitch.csv', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')

        with open('new_pitch.csv', 'w', newline='', encoding='utf-8') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',') # , escapechar='|', quoting=csv.QUOTE_NONE, quotechar='"'
        
            for row in csv_reader:
                #print(row[7])
                #row.append(r'<img src="' + row[7] + r'.png">')''.join('<img src="', row[7], '.png">')
                new_row_element = ('<img src=\"', row[7], '.png\">')
                row.append(''.join(new_row_element))
                #print(row[8])
                getScreenshot(row[7])
                csv_writer.writerow(row)

                
            
             







getExpressions()