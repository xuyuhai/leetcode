import threading
import lingkou
import time
from bs4 import BeautifulSoup
from selenium import webdriver
url = 'https://leetcode-cn.com/api/problems/all/'
html = lingkou.get_html(url)
url_list = lingkou.get_url(html)
content = [] # 用于存储题目内容及题目等信息
service_args = []
service_args.append('--load-images=no')  ##关闭图片加载
service_args.append('--disk-cache=yes')  ##开启缓存
# service_args.append('--ignore-ssl-errors=true')  ##忽略https错误
# 获取单个网页的全部内容
def get_one_content(url,driver):

    time.sleep(0.1)
    driver.get(url)  # 获取网页
    # driver.get(url_list)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    src_data = soup.select(
        "#app > div.layout__3fIJ > div.main__2_tD > div.content__2aZ1 > div.container__3dQk > div.side-tools-wrapper__2Fg5 > div.side-tools__3wY- > div.wrapper__UUUo")
    try:
        title = soup.title.text
        title = str(title).split("-")[0]
        print(title, "============================================ ")
        description = str(src_data[0].text).split("贡献者")[0]
        print(description)
        content.append([title , description , url])
    except:
        # count += 1
        print("爬取失败----------------------------")  # + str(count))
def get_content1(url_list):
    # 启动Chrome驱动
    driver = webdriver.Chrome("D:\\Program Files\\chromedriver.exe", service_args=service_args)
    for i in range(1,222):
        url = url_list[i]
        get_one_content(url,driver)
    driver.quit()
def get_content2(url_list):
    driver2 = webdriver.Chrome("D:\\Program Files\\chromedriver.exe", service_args=service_args)
    for i in range(223,446):
        url = url_list[i]
        get_one_content(url,driver2)
    driver2.quit()
def get_content3(url_list):
     driver3 = webdriver.Chrome("D:\\Program Files\\chromedriver.exe", service_args=service_args)
     for i in range(447,667):
         url = url_list[i]
         get_one_content(url,driver3)
     driver3.quit()
def main():
    time_start = time.time()
    #开三个进程同时爬取
    t1 = threading.Thread(target=get_content1, args=(url_list,))
    t2 = threading.Thread(target=get_content2,args=(url_list,))
    t3 = threading.Thread(target=get_content3, args=(url_list,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    time_end = time.time()
    print('totally cost', time_end - time_start)
if __name__ == '__main__':
    main()

