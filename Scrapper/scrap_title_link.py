from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
import time


all_papers_title=[]
all_papers_links=[]
i= 7000 #each page contains 25 manuscripts 1200*25=30000
next_page=2
link='https://ieeexplore.ieee.org/search/searchresult.jsp?highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&refinements=ControlledTerms:learning%20(artificial%20intelligence)&refinements=ControlledTerms:optimisation&refinements=ControlledTerms:feature%20extraction&refinements=ControlledTerms:neural%20nets&refinements=ControlledTerms:medical%20image%20processing&refinements=ControlledTerms:image%20classification&refinements=ControlledTerms:image%20segmentation&refinements=ControlledTerms:computational%20complexity&refinements=ControlledTerms:pattern%20classification&refinements=ControlledTerms:object%20detection&refinements=ControlledTerms:cloud%20computing&refinements=ControlledTerms:Internet%20of%20Things'
driver = webdriver.Chrome()
driver.get(link)

while(i):
    try:
        time.sleep(2)
        #save papers
        paper_box='List-results-items'
        papers=driver.find_elements(By.CLASS_NAME, "fw-bold")
        title=[paper.text for paper in papers]
        links=[paper.get_attribute('href') for paper in papers]
        all_papers_title.extend(title)
        all_papers_links.extend(links)

        # move to next page
        next_path= 'stats-Pagination_arrow_next_'+ str(next_page)
        load=driver.find_element(By.CLASS_NAME, next_path) 
        driver.execute_script('arguments[0].scrollIntoView();',load)
        driver.execute_script('arguments[0].click();',load)
        time.sleep(2)
    except:
        df = pd.DataFrame(list(zip(all_papers_title, all_papers_links)),
               columns =['Title', 'link'])
        df.to_csv("papers.csv",index=False)
    finally:
        next_page+=1
        i-=1
        print(i)
        




driver.close()

df = pd.DataFrame(list(zip(all_papers_title, all_papers_links)),
               columns =['Title', 'link'])
df.to_csv("papers.csv",index=False)