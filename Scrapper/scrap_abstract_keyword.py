from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
import time
import numpy as np
driver = webdriver.Chrome()

data= pd.read_csv('papers.csv')
data['keywords'] = data['keywords'].astype('object')
missed=[]
for row in range(52600,len(data)):
    try:
        if(data.iloc[row]['abstract'] is not np.nan):
            continue
        link=data.iloc[row]['link']

        driver.get(link)
        #abstract finding
        abstract_path='u-mb-1'
        abstract=driver.find_elements(By.CLASS_NAME, abstract_path)
        abstract=  abstract[1].text.replace("Abstract:\n","")


        #IEEE keyword finding

        keywords_path='keywords'
        keywords=driver.find_element(By.ID, keywords_path)
        driver.execute_script('arguments[0].scrollIntoView();',keywords)
        driver.execute_script('arguments[0].click();',keywords)
        ieee_key_path='doc-keywords-list-item'
        keys=driver.find_elements(By.CLASS_NAME, ieee_key_path)
        iee='IEEE Keywords'
        keys=[i.text for i in keys if iee in i.text]
        keys=keys[0].replace(iee,'')
        keys=keys.replace('\n','')
        keys=keys.split(',')
        # time.sleep(0.8)

        data.loc[row,'abstract']=abstract
        data.at[row, 'keywords'] = keys
            
        #storing
        if(row%100==0):
            data.to_csv("papers.csv",index=False)
            print(row)
    except:
        missed.append(row)
data.to_csv("papers.csv",index=False)
print(missed)