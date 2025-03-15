from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 指定 ChromeDriver 的路径
service = Service('/usr/bin/chromedriver')

# 初始化 ChromeOptions
chrome_options = webdriver.ChromeOptions()

# 如果你需要无头模式，可以取消注释下面这一行
# chrome_options.add_argument("--headless")

# 初始化 WebDriver，并指定 ChromeDriver 的路径
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开网页
driver.get("https://www.zillow.com/stanford-ca/sold/")

# 使用其 name 属性值找到搜索框
search_box = driver.find_element(By.NAME, "q")

# 在搜索框中输入文本
search_box.send_keys("web scraping")
search_box.send_keys(Keys.RETURN)

# 等待结果加载
time.sleep(5)

# 打印网页标题
print(driver.title)

# 关闭浏览器
driver.quit()
