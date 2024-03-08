from bs4 import BeautifulSoup
import requests

# http so'rovlarni amalga oshirish uchun kerak bo'ladigan object
session = requests.session()

url = "https://algo.ubtuit.uz/user/sign-in/login?back=%2Fuser%2Fsign-in%2Flogin"
login_url = "https://algo.ubtuit.uz/user/sign-in/login"

url_response = session.get(url)
url_response_html = BeautifulSoup(url_response.text, "html.parser")


# url dan olingan _csrf-token malumoti
csrf_token = url_response_html.find("input", {"name": "_csrf"})["value"]

# Shaxsiy username va passwordni kiriting
username = input("Ismingizni kiriting: ")
password = input("Paroldi kiriting: ")

data = {
    "username": username,
    "password": password,
    "_csrf": csrf_token
}

login_url_user = session.post(login_url, data=data)

if login_url_user.status_code == 200:
    print("Succes!")
    
    # Profilga kirish urli
    user_link = f"https://algo.ubtuit.uz/users/{username}"
    user_html = requests.get(user_link)
    user_html_content = user_html.text
    # profil html ma'lumotlari
    
    with open("index.html", "w") as f:
        f.write(str(user_html_content))
        
    # # Nechanchi misol kerak bo'lsa o'sha sonni kiriting
    # count = int(input("Misol sonini kiriting: "))
    
    # # Misol joylashgan url
    # task_count_url = f"https://algo.ubtuit.uz/problem/{count}"
    # task_count_html = requests.get(task_count_url)
    
    # # Kerak bo'lgan misolning html fayli
    # with open("task.html", "w") as f:
    #     f.write(str(task_count_html.text))
else:
    print("Error!")
