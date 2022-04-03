import requests
from bs4 import BeautifulSoup
import smtplib
import time

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

    if (converted_price > 1300):
        send_mail()

     
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mohammadalizafar986@gmail.com', 'sttfxhirqpdyjema')

    subject = 'Price fell down!'
    body = 'Check the amazon link! https://www.amazon.ca/Sony-ILCE7M2K-Mirrorless-28-70mm-Compact/dp/B00PX8CNCM/ref=sr_1_4?keywords=sony+a7&qid=1584504361&sr=8-4'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mohammadalizafar986@gmail.com',
        'imstillepic@gmail.com',
        msg
    )
    print('The email has been sent successfully')

    server.quit()



check_price()

while(True):
    check_price()
    time.sleep(60*60*24)



    

