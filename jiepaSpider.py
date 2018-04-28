import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException

def get_page_index(offset,keyword):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    }
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    response = requests.get(url=url,headers=headers)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def main():
    html = get_page_index(0,'街拍')
    print(html)

if __name__ == '__main__':
    main()





