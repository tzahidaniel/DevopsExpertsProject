import requests
import pymysql
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""
The script will: 
1. Post any new user data to the REST API using POST method.
2. Submit a GET request to make sure data equals to the posted data.
3. Using pymysql, check posted data was stored inside DB (users table).
4. Start a Selenium Webdriver session.
4a. Navigate to web interface URL using the new user id.
4b. Check that the user name is correct.
!!! Any failure will throw an exception using the following code: raise Exception("test failed")
"""

username='test5'
schema_name = "freedb_devops"
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_lalala', passwd='P!?k!gbS*5QXnU8', db=schema_name)
conn.autocommit(True)
cursor = conn.cursor()

# Post any new user data to the REST API using POST method.
url = 'http://127.0.0.1:5000/users'
body = {'user_name': f"{username}"}
response = requests.post(url, json=body)

uuid = response.json()[0]['id']




# # # Submit a GET request to make sure data equals to the posted data.
get_req_test = requests.get(f'http://localhost:5000/users/{uuid}')
get_response = get_req_test.json()[0]['user_name'][1]

if get_response == username:
    print("Successfuly received same user")



driver = webdriver.Chrome(service=Service("C:/Users/Tzahi/Downloads/chromedriver_win32/chromedriver.exe"))
driver.get(f"http://127.0.0.1:5000/users/{uuid}")
