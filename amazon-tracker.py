# import required files and modules

import requests
from bs4 import BeautifulSoup
import smtplib
import time

# set the headers and user string (this may change depending on your preferred browser and OS type)
headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

#enter the link you want tracked here
link = https://www.amazon.ca/MSI-GeForce-RTX-3060-12G/dp/B08WPJ5P4R/ref=sr_1_12?crid=1O3VY85AZOS58&keywords=graphics+card&qid=1672890342&sprefix=graphics+car%2Caps%2C159&sr=8-12

# send a request to fetch HTML of the page
response = requests.get(link, headers=headers)

# create the soup object
soup = BeautifulSoup(response.content, 'html.parser')

# change the encoding to utf-8
soup.encode('utf-8')

threshold = 500;
# function to check if the price has dropped below a set amount (determined by var threshold, which is 500 dollars in this case)
def check_price():
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('$', '').replace(' ', '').strip()

  # converts string value to number, ommiting the symbols
  converted_price = float(price[0:5])
  print(converted_price)
  # if the new price is below the threshold, send an email
  if(converted_price < threshold):
    send_mail()

  #using strip to remove extra spaces in the title
  print(title.strip())




# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  
  # enter your email and temporary password here (can be requested through google settings)
  server.login('email@gmail.com', 'password')

  subject = 'Price Fell Down'
  body = "Check the amazon link"

  msg = f"Subject: {subject}\n\n{body}"
  
  # enter the sender and receiver emails here
  server.sendmail(
    'sender@gmail.com',
    'receiver@gmail.com',
    msg
  )
  # print a message to check if the email has been sent
  print('Hey Email has been sent')
  # quit the server
  server.quit()

# loop that allows the program to regularly check for prices
while(True):
  check_price()
  time.sleep(60 * 60)
