import requests
from bs4 import BeautifulSoup
import json
#import boto3


def job_scrape():
    titleList = []
    companyList = []
    salaryList = []
    locationList = []

    for i in range(0, 50, 10):
        page = requests.get(
            "https://ca.indeed.com/jobs?q=Hourly+Jobs&l=Canada&start="+str(i))
        content = BeautifulSoup(page.content, 'html.parser')

        allJobs = content.select('.result')

        for job in allJobs:
            try:
                title = job.find("a", class_="jobtitle").text.replace('\n', '')
            except:
                title = 'None'

            titleList.append(title)

            try:
                location = job.find(
                    "div", class_="location").text.replace('\n', '')
            except:
                location = 'None'

            locationList.append(location)

            try:
                company = job.find(
                    "span", class_="company").text.replace('\n', '')
            except:
                company = 'None'

            companyList.append(company)

            try:
                salary = job.find(
                    "span", class_="salaryText").text.replace('\n', '')
            except:
                salary = 'None'
            
            salaryList.append(salary)
    return {
        'jobTitles': titleList,
        'companies': companyList,
        'salaries': salaryList,
        'locations': locationList
    }

def save_file_to_s3(bucket, file_name, data):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, file_name)
    obj.put(Body = json.dumps(data))

def scrape(event, context):
    data = job_scrape()
    file_name = f"jobList"
    for j in range(0,len(data['salaries'])):
        s3entry = {
            'title': data['jobTitles'][j],
            'company':data['companies'][j],
            'salary':data['salaries'][j],
            'location':data['locations'][j]
        }
        save_file_to_s3('indeed_hourly_jobs', file_name, s3entry)