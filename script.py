import requests, urllib.request as req

MOBILE_NUMBER = "MOBILE_NUMBER"
SENDER_ID = "SENDER ID"
API_KEY = "API KEY HERE"
MESSAGE = req.pathname2url("Hello")

url = 'http://bulksmswebsiteurl/sendSMS?key='+ API_KEY +'&sender='+ SENDER_ID +'&mobile='+ MOBILE_NUMBER +'&msg='+ MESSAGE

result = requests.get(url) 
print(result)
