from lxml import etree

import proxy


myProxy = proxy.MyProxy()

url = 'http://www.sodu888.com/book/288771.html'

while True:
    html = myProxy.get(url)
    # html = s.get('https://www.facebook.com/login.php?login_attempt=1', proxies=proxies, verify=False)
    print(html.status_code)
    selector = etree.HTML(html.text)
    # print(selector)
    zjs = selector.xpath('//a[@rel="nofollow"]')
    #print(zjs)
    for zj in zjs:
        zjName = (zj.xpath('./text()')[0])
        print(zjName)

