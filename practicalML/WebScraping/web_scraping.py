from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup

# 指定 ChromeDriver 的路径
service = Service('/usr/bin/chromedriver')

# 初始化 ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

# 初始化 WebDriver，并指定 ChromeDriver 的路径
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开网页
html_page = driver.get("https://www.zillow.com/stanford-ca/sold/")

# 获取页面的 HTML 内容
html_page = driver.page_source

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_page, "html.parser")

# 将 HTML 内容保存到本地文件
with open("saved_page.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

# 打印格式化后的 HTML 内容
print(soup.prettify())

# 关闭浏览器
driver.quit()
