End to End Text Summarization---

--python -m venv venv -- virtual environment
how you can activate a virtual environment
for windows-- .\venv\Scripts\activate
linux: source venv/bin/activate
dummy.py for testing
dummy.py -- hugging face-->models-->summarization-->accelerated interface
venv interpreter will be used- check this.
as in my file, python 3.10.12 interpreter is used by venv 
in dummy.py
request library is used for making http methods calling(access anything from www)
pip install requests to install requests model in venv
comment out whole code except import requests to understand request better
takae this following code from real python, of requests to underestand it better.
response = requests.get("https://api.github.com")
print(response)
on execution, terminal shows <Response [200]> indicate all data came inside it, success || 500+ --> server error || webpage not available- 400 
remove comment from code and run.
------
accelerated inference api documentation -- detailed parameters --- summarization task -- from there we change api rule to ensure we can changee min length, max length, and sooonn



using transformer based model - use hugging face api
github for commit the project
post api
cicd deployment using github action as cicd tool
aws account

// jinja work as a bridge, it opens a gatewaly between two (frontwnd, baaackend)

add app.py file - exist outside all the folder
add folder static and template(flask find html page in template named folder, that's why we make this folder), static contain javascript and css(static files)

if want to send something from backend to the frontend - use jinja
if from frontend to backend(maxL, minL) - in this too jinja help in this

command to run flask program, flask run

if __name__ == '__main__': same like main function of functional programming

{{}} -- gateway to use jinja. 

{{result}} should include in html file and the same name will be added in app.py in order to print result or show output

if we want to hit any url and want to take url, then url_for is used

method post is used for more secure data while get easily shows your pwd and all.

request can be import in two ways:- 
one from flask and other from requests. remember this!!!
