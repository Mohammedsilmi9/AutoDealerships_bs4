from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep
import human
import os
import urllib.request
driver=webdriver.Chrome()
driver.get('https://www.apexcars.net/pre-owned-cars')
human.human_behavior(driver)
res = driver.execute_script("return document.documentElement.innerHTML;")
soup=BeautifulSoup(res,'lxml')
cars = soup.find_all('div',{'class':'ds-vehicle-list-item ds-well'})

counter=0
for car in cars:
    counter+=1
    title  = car.find("meta",  itemprop="name").get("content")
    make   = car.find("meta",  itemprop="brand").get("content")
    model  = car.find("meta",  itemprop="model").get("content")
    vin    = car.find("meta",  itemprop="productID").get("content")
    year   = car.find("meta",  itemprop="releaseDate").get("content")
    desc   = car.find("meta",  itemprop="description").get("content")
    odo    = car.find("meta",  itemprop="mileageFromOdometer").get("content")
    price  = car.find("meta",  itemprop="price").get("content")
    human.human_behavior(driver)
    driver.find_element_by_xpath(f'/html/body/div[6]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[{counter}]/div[2]/div[2]/h4/a').click()
    res1 = driver.execute_script("return document.documentElement.innerHTML;")
    soup1=BeautifulSoup(res1,'lxml')
    images = soup1.findAll('img', attrs={'class':'img-responsive lazy'})
    url_list=[]
    for image in images:
        url_list.append(image['data-src'][2:])
    if not os.path.isdir(rf'C:\Users\Silmi\Desktop\Dealerships_automation\APEX_cars\{make}_{model}_{year}'):
        os.mkdir(rf'C:\Users\Silmi\Desktop\Dealerships_automation\APEX_cars\{make}_{model}_{year}')

    with open(rf'C:\Users\Silmi\Desktop\Dealerships_automation\APEX_cars\{make}_{model}_{year}\info.txt', 'w+') as carfile:
        carfile.write(title +",,"+ make +",,"+ model +",,"+ vin +",,"+ year +",,"+ desc +",,"+ odo +",,"+ price)
    carfile.close()
    for x in range(len(images)):
        try:
            sleep(0.3)
            urllib.request.urlretrieve("https://"+url_list[x],rf"C:\\Users\Silmi\Desktop\Dealerships_automation\APEX_cars\{make}_{model}_{year}\pic_{x+1}.jpg")
        except:
            pass

    driver.execute_script("window.history.go(-1)")
    human.human_behavior(driver)
driver.close()
