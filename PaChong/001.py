#1.获取到当前网页源代码
#2.从网页源代码里面把相关的URL给提取出来
#3.通过请求这个图片的URL  来把图片保存到本地

def tuPian():
    url = "https://www.google.com.sg/search?q=123&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjnhuHqv7rdAhUIbo8KHYryCa4Q_AUICigB"
    headers ={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    r = request.get(url, headers=headers)
    ret =r.text
   # print(ret)



pic_url_list = re.findall('"objURL":"(.*?)"',ret)   #result就是我们所有图片的URL

for pic_url in pic_url_list:
#    print(i)
    while open('./jpg/{}'.format(pic_url[-10:]),'ab') as f:
        pic = requests.get(pic_url,headers = headers,
