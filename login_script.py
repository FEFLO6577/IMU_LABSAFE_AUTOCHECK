# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager

# 自动下载匹配的 chromedriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
# 浏览器驱动配置（需自行下载对应版本）
DRIVER_PATH = '/usr/local/bin/chromedriver'

# 登录凭证
USERNAME = '32407082'
PASSWORD = 'Natsuki6577/'

# 初始化浏览器
driver = webdriver.Chrome(service=Service(DRIVER_PATH))
driver.get('https://labsafe.imu.edu.cn/lab-platform/login')

try:
    # 定位统一认证登录按钮
    auth_btn = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/form/div/div/div/a"))
    )
    auth_btn.click()

    # 等待跳转到认证页面
    WebDriverWait(driver, 30).until(
        EC.url_contains('cer.imu.edu.cn')
    )
    # 定位用户名输入框
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
    )
    username.send_keys(USERNAME)

    # 定位密码输入框
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys(PASSWORD)

    # 点击登录按钮
    login_btn = driver.find_element(By.XPATH, '//*[@id="login_submit"]')
    login_btn.click()

    # 等待登录完成
    WebDriverWait(driver, 15).until(
        EC.url_contains('lab-platform')
    )
    print("登录成功！")
    
    # 等待并点击目标元素
    target_element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapApp"]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/ul/li'))
    )
    target_element.click()
    
    # 等待并点击目标元素
    target_element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapApp"]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr/td[5]/div/span'))
    )
    target_element.click()

    target_element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapApp"]/div/div[2]/div[2]/div/div[1]/h3/div/label[1]'))
    )
    target_element.click()

    target_element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapApp"]/div/div[2]/div[2]/div/div[2]/div/button[1]'))
    )
    target_element.click()

    print("打卡结束！")
    # 保持浏览器打开
    time.sleep(30)

except Exception as e:
    print ("发生错误")
finally:
    driver.quit()
