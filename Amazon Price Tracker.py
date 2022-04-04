import requests
from bs4 import BeautifulSoup
import smtplib
import time

#insert the URL that you want to track
URL = '[INSERT URL HERE]'

headers = {
    #insert device and browser type
    "User-Agent": '[REDACTED]'}


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
    #enter email and password here (private information redacted)
    #server.login('johnsmith@email.com', 'password123')

    subject = 'Price Drop!'
    body = f'The price of your item fell by 10%!\nCheck the amazon link! {URL}'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        # type in the sender and recipient
        'johnsmith@email.com',  # sender
        'janesmith@email.com',  # recipient
        msg
    )
    print('The email has been sent successfully')

    server.quit()



check_price()

while(True):
    check_price()
    time.sleep(60*60*24)



    

