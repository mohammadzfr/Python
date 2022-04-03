import requests
from bs4 import BeautifulSoup
import smtplib
import time

#insert the URL that you want to track
URL = 'https://www.amazon.ca/Sony-ILCE7M2K-Mirrorless-28-70mm-Compact/dp/B00PX8CNCM/ref=sr_1_4?keywords=sony+a7&qid=1584504361&sr=8-4'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.prettify)

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[5:6] + price[7:10])

    print(converted_price)
    print(title.strip())

    if (converted_price > converted_price * 0.9):
        send_mail()

     
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #enter email and password here
    #server.login('johnsmith@email.com', 'password123')

    subject = 'Price Drop!'
    body = 'The price of your item fell by 10%!\nCheck the amazon link! {URL}'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'johnsmith@email.com',
        'janesmith@email.com',
        msg
    )
    print('The email has been sent successfully')

    server.quit()



check_price()

while(True):
    check_price()
    time.sleep(60*60*24)



    

