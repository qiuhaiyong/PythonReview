import requests

def download_picture(url):
    print(f'开始下载：{url}')
    response = requests.get(url)
    print('下载完毕')
    with open(url[-10:], 'wb') as file:
        file.write(response.content)


def main():
    url_list = [
        'https://n.sinaimg.cn/spider20260129/217/w600h417/20260129/3e26-917ee55a8a42b8626807c332c24981de.png',
        'https://n.sinaimg.cn/finance/transform/97/w630h267/20260129/97c4-b211cc51784830f09ee19e450475c93b.png',
        'https://n.sinaimg.cn/spider20260129/539/w1439h700/20260129/e09a-cc2ca319e00f701ccfca3ebc62aa8772.png'
    ]
    for url in url_list:
        download_picture(url)

main()