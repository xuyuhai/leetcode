import requests
import json
'''
    该页主要获取每个题目的网址
'''
def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except:
        print("Erro" + response.status_code)

# 用json对demo网页的源码进行解析
# 准确的说是用来提取题目的名称和题目的链接
def get_url(html):
    analyze_html = json.loads(html)  # 将https://leetcode-cn.com/problems/all/页面的json数据解析成python对象
    urls = []  # 定义一个用于存储题目链接的列表
    questions = []  # 定义一个用于存储题目的列表
    # 从json数据中提取我们需要的题目,放入questions[]中
    # 通过IDLE对字典analyze_html进行解析可知题目名在列表stat_status_pairs中
    for i in range(667):
        questions.append(analyze_html['stat_status_pairs'][i]['stat']['question__title_slug'])
        # 将名称与leetcode url 的基础 http://leetcode-cn.com/
        url = 'https://leetcode-cn.com/problems/' + questions[i]
        urls.append(url)
    return urls
if __name__ == "__main__":
    url = 'https://leetcode-cn.com/api/problems/all/'
    html = get_html(url)
    url_lists = get_url(html)
