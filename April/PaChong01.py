import urllib.request
import urllib.parse

user_agent =' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

referer='https://pre-newretail.alibaba-inc.com/price/skuGroupList'

post_data={'id': "133", 'current': '1'}

headers={'User_Agent':user_agent,'referer':referer}

post_data_encode = urllib.parse.urlencode(post_data)

post_data_encode = post_data_encode.encode(encoding='utf-8')

request_url=('http://www.baidu.com')



request = urllib.request.Request(request_url,post_data_encode)


reponse = urllib.request.urlopen(request)

print (reponse.read().decode('utf-8'))