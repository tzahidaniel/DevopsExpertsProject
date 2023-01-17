import requests
import pymysql
import
schema_name = "freedb_devops"
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_lalala', passwd='P!?k!gbS*5QXnU8', db=schema_name)
conn.autocommit(True)
cursor = conn.cursor()


def test_add_user():
    try:
       response = requests.post('http://127.0.0.1:5000/users' , json={'user_name': "john"})
       print("post", response.status_code)
       print(response.reason)


if __name__ == '__main__':
    test_add_user()

