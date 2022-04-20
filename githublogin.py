from bs4 import BeautifulSoup
import requests
import re
requesturl="https://github.com/session"
id="your_id"
password="your_password"
session = requests.Session()
html = session.get(requesturl)
BeautifulSoupObject = BeautifulSoup(html.text,"html.parser")
authenticity_token = BeautifulSoupObject.find('input',{'name':'authenticity_token'}).get('value')
timestamp = BeautifulSoupObject.find('input',{'name':'timestamp'}).get('value')
timestamp_secret = BeautifulSoupObject.find('input',{'name':'timestamp_secret'}).get('value')
required_field = BeautifulSoupObject.find("input", {'type': 'text', 'name': re.compile("^required_field")}).get("name")
#print("authenticity_token : "+authenticity_token,"timestamp : "+timestamp,"timestamp_secret : "+timestamp_secret,"required_field : "+required_field,sep="\n")

data = {
    'commit': 'Sign in',
    'authenticity_token': authenticity_token,
    'login': id,
    'password': password,
    'webauthn-support': 'supported',
    'webauthn-iuvpaa-support': 'unsupported',
    'return_to': '',
    required_field: '',
    'timestamp': timestamp,
    'timestamp_secret': timestamp_secret
}
response = session.post(requesturl,data=data)
print("Status Code", response.status_code)
print("Response ", response.text)
