import jwt
import requests
import json
import time




def qrCreate():
    session = json.loads(sessionCreate())

    secret_key = "4ZycJi+SNg6cf0zIvlAg2p4l3vXABvEKWpnKZHxxixE="

    sesion_id = session["data"]["id"]
    my_json = {
        "params": {
            "sessionId": sesion_id,
            "systemType": "ECOM",
            "clientId": '1'
        },
        "data": {
            "externalId": 2222,
            "description": "test",
            "amount": 100,
            "redirectUrl": "https://www.libertygroup.club",
            "type": "PAY"
        },
        "iat":int(time.time())

    }
    q = json.dumps(my_json)


    token = jwt.encode({'data': q}, secret_key, algorithm="HS256")


    sendid = {
   "params": {
      "sessionId": sesion_id,
      "systemType": "ECOM"
   },
   "data": {
      "externalId": "2222",
      "description": "test",
       "amount": 100,
      "type": "PAY",
      "token": token
   }
}
    qsendid = json.dumps(sendid)
    headers = {
            "content-type": "application/json; charset=utf-8"
        }

    response = requests.request("POST", "https://api.uapay.ua/api/invoicer/invoices/create", data = qsendid, headers=headers)

    print(response.text)
    # de_data = jwt.decode(response.text, secret_key, algorithms=["HS256"])
    #
    # print(de_data)
def sessionCreate():
    q='''{
   "params":{
      "clientId":"1"
   }
}'''
    headers = {
        "content-type": "application/json; charset=utf-8"
    }
    response = requests.request("POST", "https://api.uapay.ua/api/sessions/create", data=q,
                                headers=headers)
    return response.text

qrCreate()