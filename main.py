from flask import Flask,request
import requests
import Message 


API= f 'https://api.telegram.org/bot{BOT_TOKEN}'+'{method_name}'

app = Flask(__name__)
@app.route('/',method=['GET','POST'])
def main(*args,**kwargs):
    message= new Message(request.json['message'])
    method_name,params=message.get_response()
    while not send_response(method_name,params):
        time.sleep(5)
    return 'OK'
def send_response(method_name,params):
    r=requests.post(url=API.format(method_name=method_name),params=params)
    return r.status_code == 200
    
if __name__ == '__main__':
    app.run()

