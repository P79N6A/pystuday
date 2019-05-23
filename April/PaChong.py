import urllib.request
import urllib.parse

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

referer='https://pre-newretail.alibaba-inc.com/price/skuGroupList'

post_data={'id': "133", 'current': '1'}

headers={'User_Agent':user_agent,'referer':referer}

post_data_encode = urllib.parse.urlencode(post_data)

post_data_encode = post_data_encode.encode(encoding='utf-8')

request_url=('https://www.baidu.com')

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

request = urllib.request.Request(request_url,post_data_encode, headers=headers)

reponse = urllib.request.urlopen(request)
# print(reponse.)
# print(reponse.read())
print (reponse.read().decode('utf-8'))