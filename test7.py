import requests
import json


#:authority:papago.naver.com
#:method:POST
#:path:/apis/n2mt/translate
#:scheme:https
#accept:application/json
#accept-encoding:gzip, deflate, br
#accept-language:ko
#content-length:163
#content-type:application/x-www-form-urlencoded; charset=UTF-8
#cookie:NNB=DIOH4K6JQBVVS; npic=TnhoVEm2WTUiHAZSMGjuPzhFCLIFN2+n6+B9btGFhKbBobEUA1VkkQXzP9SLC9CECA==; __date_rename_layer=2017731; ASID=d36e17960000015e054c782100000048; nx_ssl=2; _ga=GA1.2.265821840.1501686173
#device-type:pc
#origin:https://papago.naver.com
#referer:https://papago.naver.com/
#user-agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
#x-apigw-partnerid:papago

#headers = {'x-apigw-partnerid': 'papago'}
#payload = dict(data='rlWxnJA0Vwc0paIyLCJkaWN0RGlzcGxheSI6NSwic291cmNlIjoia28iLCJ0YXJnZXQiOiJlbiIsInRleHQiOiLrgrTqsIAg7LWc6rOg64ukIn0%3D')
#
#url = 'https://papago.naver.com/apis/n2mt/translate'
#recvd = requests.post(url, data=payload, headers=headers)
#print(recvd)
#print(recvd.text)
#
#root = json.loads(recvd.text)
#print(type(root))
#print(root.keys())

def translate(text, toEng):

    headers = {'x-apigw-partnerid': 'papago'}
    payload = dict(data=text)

    url = 'https://papago.naver.com/apis/n2mt/translate'
    recvd = requests.post(url, data=payload, headers=headers)

    result = json.loads(recvd.text)
    return result['translatedText']

print(translate('rlWxnJA0Vwc0paIyLCJkaWN0RGlzcGxheSI6NSwic291cmNlIjoia28iLCJ0YXJnZXQiOiJlbiIsInRleHQiOiLrgrTqsIAg7LWc6rOg64ukIn0%3D', True))