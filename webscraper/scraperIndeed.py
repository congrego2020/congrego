from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Firefox(
    executable_path="/Users/admin/Documents/congrego/webscraper/geckodriver")

df = pd.DataFrame(columns=["Title", "Location",
                           "Company", "Salary", "Sponsored", "Description"])

# Step1: Get the page
driver.get("https://ca.indeed.com/jobs?q=Hourly+Jobs&l=Canada")
driver.implicitly_wait

all_jobs = driver.find_elements_by_class_name('result')

for job in all_jobs:

    result_html = job.get_attribute('innerHTML')
    soup = BeautifulSoup(result_html, 'html.parser')

    try:
        title = soup.find("a", class_="jobtitle").text.replace('\n', '')
    except:
        title = 'None'

    sum_div = job.find_element_by_xpath('./div[3]')
    try:
        sum_div.click()
    except:
        close_button = driver.find_elements_by_class_name(
            'popover-x-button-close')[0]
        close_button.click()
        sum_div.click()

    df = df.append({'Title': title}, ignore_index=True)

    print("Got these many results:", df.shape)

df.to_csv("ai.csv", index=False)
