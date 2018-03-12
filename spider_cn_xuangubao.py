
# coding: utf-8

# In[23]:


import requests
from lxml import etree
import pandas as pd


# 选股宝code格式603104.SS 300148.SZ
def get_symbol(code):
    if str(code).startswith('300') or str(code).startswith('00'):
        return 'https://www.xuangubao.cn/stock/' + str(code)+'.SZ'
    else:
        return 'https://www.xuangubao.cn/stock/' + str(code)+'.SS'
    
# 获取数据
def get_html(code):
    headers = {
        'referer':'https://www.xuangubao.cn/stock/600267.SS',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    url = get_symbol(code)
    # 请求
    res = requests.get(url,headers = headers).text
    # 解析
    html = etree.HTML(res)
    return html

def get_data(html):
    # 找到每条信息的a标签
    results = html.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/a')
    row = []
    for result in results:
        title = result.xpath('div[1]/text()')[0] # 取文字部分
        percent = result.xpath('div[2]/text()')[0] # 取百分比
        link = result.xpath('@href')[0]
        link = 'https://www.xuangubao.cn' + link # 链接
        data = {
            'title':title,
            'percent':percent,
            'link':link,
        } 
        row.append(data)
    return row

# 整理成表
def arr_data(row):
    df = pd.DataFrame(row)
    return df

# 主函数
def main():
    html = get_html(600267)
    data = get_data(html)
    df = arr_data(data)
    print(df)
    
main()


# In[ ]:




