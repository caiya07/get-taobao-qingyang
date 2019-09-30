# -*- coding: utf-8 -*-
import requests,time,os
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    html = requests.get(url,headers=headers).content.decode('gbk')
    return html

if __name__ == '__main__':
    url = 'https://list.tmall.com/search_product.htm?q=%CB%AE%D6%AE%C3%DC%D3%EF&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    for item in soup.find_all('div', class_='product'):
        url = item.find('div').find_all('p')[1].find('a').attrs['href'][2:]
        url = 'https://chaoshi.{}'.format(url)
        price = item.find('div').find('p').find('em').text[1:]

        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        title = soup.find('div', class_="tb-detail-hd").find('h1').text
        title = title.strip('\t\r\n\t\t\t\t\t ')

        data = '{},{}'.format(title,price)
        print(data)
        filename = '{}\ShuiZhiMiYu.csv'.format(os.getcwd())
        with open(filename,'a',encoding='GBK')as f:
            f.write('{}\n'.format(data))
            time.sleep(0.1)








