from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Firefox(
    executable_path="/Users/admin/Documents/congrego/webscraper/geckodriver")

df = pd.DataFrame(columns=["Title", "Location",
                           "Company", "Salary"])

for i in range(0, 50, 10):
    driver.get("https://ca.indeed.com/jobs?q=Hourly+Jobs&l=Canada&start="+str(i))
    driver.implicitly_wait

    all_jobs = driver.find_elements_by_class_name('result')

    for job in all_jobs:

        result_html = job.get_attribute('innerHTML')
        soup = BeautifulSoup(result_html, 'html.parser')

        try:
            title = soup.find("a", class_="jobtitle").text.replace('\n', '')
        except:
            title = 'None'

        try:
            location = soup.find(
                "span", class_="location").text.replace('\n', '')
            print(location)
        except:
            location = 'None'

        try:
            company = soup.find(
                "span", class_="company").text.replace('\n', '')
            print(company)
        except:
            company = 'None'

        try:
            salary = soup.find(
                "span", class_="salaryText").text.replace('\n', '')
            print(salary)
        except:
            salary = 'None'

        sum_div = job.find_element_by_xpath('./div[3]')
        try:
            sum_div.click()
        except:
            close_button = driver.find_elements_by_class_name(
                'popover-x-button-close')[0]
            close_button.click()
            sum_div.click()

        df = df.append({'Title': title, 'Location': location,
                        'Company': company, 'Salary': salary}, ignore_index=True)

        print("Got these many results:", df.shape)

df.to_csv("ai.csv", index=False)
