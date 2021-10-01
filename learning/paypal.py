import requests
import json
def GenerateToken():
    url="https://api-m.sandbox.paypal.com/v1/oauth2/token"
    headers={"Accept":"application/json","Accept-Language":"en_US"}
    data={"grant_type":"client_credentials"}
    response=requests.post(url,headers=headers,data=data,auth=("AaxRSlM27EvRDp_Thhsc_ws8UM8xnrsYTyvJnzbLlSx9hod9wBJsBACa-eo2ZhIIqfR4f-zq--aV7PsC","EBw9hd2OMRD1mGRV8MBbL8yTYo8djRuAiVJKoM0zc9_49DLFm2RqGStzlspjhuolbA4mNro9DIqrKnbp"))
    data=response.json()
    access_token=data['access_token']
    return access_token
def CreateProduct(access_token,hashed_request_id):
    headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}',
                'PayPal-Request-Id': hashed_request_id,
            }
            
    data={"name": "UnoStartup Subscription","type": "SERVICE"}
    data=json.dumps(data)
    
    response = requests.post('https://api-m.sandbox.paypal.com/v1/catalogs/products',headers=headers,data=data)
    if response.status_code != 200 or response.status_code !=201:
        access_token=GenerateToken()
        headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}',
                'PayPal-Request-Id': hashed_request_id,
            }
        response = requests.post('https://api-m.sandbox.paypal.com/v1/catalogs/products',headers=headers,data=data)
        

    data=response.json()
    return data['id']
def CreatePlan(access_token,package_price,package_name):
    url="https://api-m.sandbox.paypal.com/v1/billing/plans"
    headers={
                "Accept":"application/json",
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
                "Prefer":"return=representation"
            }
    infile=open("paypal_product_id.txt","r") 
    product_id=infile.read()
    data={
      "product_id":product_id,
      "name": package_name,
      "description": "Basic plan",
      "type":"FIXED",
      "status":"ACTIVE",
      "billing_cycles": [
        
            {
              "frequency":
               {
                 "interval_unit": "MONTH",
                 "interval_count": 1
                 },
                 "tenure_type": "REGULAR",
                 "sequence": 1,
                 "total_cycles": 0,
                 "pricing_scheme": 
                 {
                   "fixed_price": 
                   {
                   "value": f"{package_price}",
                   "currency_code": "EUR"
                   }
                   }
                   }
                   ],
                   "payment_preferences": 
                   {
                     "auto_bill_outstanding": "true",
                     "setup_fee_failure_action": "CONTINUE",
                     "payment_failure_threshold": 3
                     },
                     "taxes": 
                     {
                       "percentage": "1",
                       "inclusive": "false"
                       }}
    data=json.dumps(data)
    response = requests.post(url,headers=headers,data=data)
    print(response.json())
    if(response.status_code == 201):
      response=response.json()
      return response['id']
    else:
      access_token=GenerateToken()
      headers={
                "Accept":"application/json",
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
                "Prefer":"return=representation"
            }
      response = requests.post(url,headers=headers,data=data)
      response=response.json()
      return response['id']
      #return "Could not be created"
def PauseSubscription(subscription_id,access_token):
    url=f"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/{subscription_id}/suspend"
    headers={
      "Content-Type":"application/json",
      "Authorization":f"Bearer {access_token}"
    }
    data={"reason":"Customer-requested pause"}
    data=json.dumps(data)
    response=requests.post(url,headers=headers,data=data)
    if response.status_code != 200 or response.status_code != 201:
      access_token=GenerateToken()
      headers={
      "Content-Type":"application/json",
      "Authorization":f"Bearer {access_token}"
    }
    response=requests.post(url,headers=headers,data=data)
def ResumeSubscription(subscription_id,access_token):
  url=f"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/{subscription_id}/activate"
  headers={
      "Content-Type":"application/json",
      "Authorization":f"Bearer {access_token}"
    }
  data={"reason":"Reactivating on customer request"}
  data=json.dumps(data)
  response=requests.post(url,headers=headers,data=data)
  if response.status_code != 200 or response.status_code != 201:
    access_token=GenerateToken()
    headers={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {access_token}"
  }
  response=requests.post(url,headers=headers,data=data)
def CreateSubscription(access_token,plan_id,user_profile):
    url="https://api-m.sandbox.paypal.com/v1/billing/subscriptions"
    headers={
        "Accept": "application/json" ,
   "Authorization": f"Bearer {access_token}" ,
   "Prefer": "return=representation" ,
   "Content-Type": "application/json" 
    }
    data={
        "plan_id": f"{plan_id}",
      "start_time": "2020-02-27T06:00:00Z",
      "subscriber": {
        "name": {
          "given_name": user_profile.user.first_name,
          "surname": user_profile.user.last_name
        },
        "email_address": user_profile.user.email
      },
      "application_context": {
        "brand_name": "UnoStartup",
        "locale": "en-US",
        "shipping_preference": "SET_PROVIDED_ADDRESS",
        "user_action": "SUBSCRIBE_NOW",
        "payment_method": {
          "payer_selected": "PAYPAL",
          "payee_preferred": "IMMEDIATE_PAYMENT_REQUIRED"
        },
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }

def SendPayout(email_receiver,amount,payout_id,access_token):
    url="https://api-m.sandbox.paypal.com/v1/payments/payouts"
    headers={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {access_token}"
    }
    data={
    "sender_batch_header":{
      "sender_batch_id":f"{payout_id}",
      "email_subject": "You have a payout!",
      "email_message": "You have received a payout! Thanks for using our service!"
        },
    "items":[
        {
        "recipient_type": "EMAIL",
      "amount": {
        "value": f"{amount}",
        "currency": "USD"
      },
      "note": "Thanks for your patronage!",
      "sender_item_id": f"{payout_id + 1}",
      "receiver": f"{email_receiver}"
        }
     ]
    }
    data=json.dumps(data)
  
    response=requests.post(url,headers=headers,data=data)
    response=response.json()
    try:
        err=response['error']
    except:
        err=''
    if err != '':
        access_token=GenerateToken()
        headers={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {access_token}"
  }
        response=requests.post(url,headers=headers,data=data)
        response=response.json()
    infile=open("/var/www/money_buddy/moneybuddy/logs/text7.txt","w")
    infile.write(str(response))
    infile.close()

    return response
def ListTransactions(subscription_id,access_token):
    url=f"https://api-m.sandbox.paypal.com/v1/billing/subscriptions/{subscription_id}/transactions?start_time=2018-01-21T07:50:20.940Z&end_time=2022-08-21T07:50:20.940Z"
    headers={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {access_token}"
  }
    #nfile=open('/var/www/money_buddy/moneybuddy/logs/text3.txt','w')
  
      
    response=requests.get(url,headers=headers)
    response=response.json()
    if response['error']:
        access_token=GenerateToken()
        headers={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {access_token}"
  }
        response=requests.get(url,headers=headers)
    response=response.json()
    infile=open("/var/www/money_buddy/moneybuddy/logs/text4.txt","w")
    infile.write(str(response))
    infile.close()
    return response

def GetPlans(token):
  headers={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {token}"
  }
  url="https://api-m.sandbox.paypal.com/v1/payments/billing-plans"    
  response=requests.get(url,headers=headers)
  print(response.text)
  # response=response.json()
  return response