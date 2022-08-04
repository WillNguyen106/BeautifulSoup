#Complete the main function to get the job role and location from the user and print it on the console.

#import beautifulsoup and request here
from bs4 import BeautifulSoup
import requests
import json

# with open ('3155_Beautiful_Soup_WillNguyen.postman_collection.json') as q:
#     data1 = json.load(q)





#function to get job list from url 'https://www.monster.com/jobs/search?q={role}&where={location}'
def getJobList(role,location):
    url = 'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here
    response = requests.get(url).text
    # print the status code here!
    soup = BeautifulSoup(response,'html.parser')
    JobDetails = soup.find_all('div',class_ = 'card card__job')
    #print(JobDetails)
    # Create an array here
    jobList =[]
    for job in JobDetails:
        jobTitle = job.find('h2', class_='card__job-title').text.strip()
        company = job.find('div', class_='card__job-empname-label').text.strip()
        description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
        jobDetailsjson = {
                "Title": jobTitle,
                "Company": company,
                "Description" : description
            }
        jobList.append(jobDetailsjson)

        
# Add jobDetailsjson to that array
    # jobList.append(jobDetailsjson)
    print(jobList)
    return jobList

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    JobData = json.dump(jobDetails)
    with open ('jobDetails.json') as b:
        data = json.load(b)
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location you want to search")
    location = input()

    getJobList(role,location)
    #saveDataInJSON()
    
    
if __name__ == '__main__':
    main()

