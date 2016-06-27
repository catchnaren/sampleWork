import re
import sys
import time
import schedule
import datetime
from selenium import webdriver
from pyvirtualdisplay impot Display
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

display = Display(visible = 0, size = (800, 600))
display.start()

class deviceType:
    def __init__(self):
        print 'Initializing build download automation...'

    def loginDriver(self, url, username, passwd):
        try:
            global driver
            driver = webdriver.Chrome('C:\Users\chromedriver')
            driver.set_window_size(1600, 920)
            driver.get(url)
            emailElem = driver.find_element_by_id('no_table_username').send_keys(username)
            passElem = driver.find_element_by_id('no_table_password').send_keys(passwd)
            loginElem = driver.find_element_by_xpath('//*[@id="submit_record__row"]/td[2]/input')
            loginElem.click()
        except Exception, e:
            print str(e)
            #driver.close()

    def shipBranchElements(self, fireOs, ship, device):
        try:
            driver.implicitly_wait(300)
            osElem = driver.find_element_by_link_text(fireOs)
            hover = ActionChains(driver).move_to_element(osElem)
            hover.perform()
            shipElem = driver.find_element_by_link_text(ship)
            hover = ActionChains(driver).move_to_element(shipElem)
            hover.perform()
            sloaneElem = driver.find_element_by_link_text(device)
            sloaneElem.click()
        except Exception, e:
            print str(e)
            #driver.close()

    def fileSearch(self, date, status, fileId):
        try:
            driver.implicitly_wait(300)
            fosDateElem = driver.find_element_by_xpath(date).text
            fosStatusElem = driver.find_element_by_xpath(status).text
            fosFileElem = driver.find_element_by_xpath(fileId)
            today = str(datetime.date.today())
            dateRegex = re.compile(r'\d\d\d\d-\d\d-\d\d')
            mo = dateRegex.search(fosDateElem)
            if mo.group() == today and fosStatusElem == 'success':
                fElem = fosFileElem
                fElem.click()
            else:
                print 'Build Status: Pending'
                driver.close()
                #print 'Build Status: Pending | initiating auto check process after 1 hour...'
                #schedule.every(1).minute.do(fileSearch(self))
                #schedule.every(1).hour.do(fileSearch(self))
        except Exception, e:
            print str(e)
            #driver.close()

    def download(self, build, location):
        try:
            driver.implicitly_wait(300)
            userElem = driver.find_element_by_xpath(build)
            userElem.click()
            releaseElem = driver.find_element_by_xpath(location)
            hover = ActionChains(driver).move_to_element(releaseElem)
            hover.click().perform()
            print 'Success | File Download Initiated'
        except Exception, e:
            print str(e)
            #driver.close()

    def __del__(self):
        sys.exit

def main():
    try:
        '''fileHandle = open('C:\payload.txt', 'r')
        payload =
        for line in fileHandle:
            x = line.split(',')
            a = x[0]
            b = x[1]
            c = len(b)-1
            b = b[0:c]
            payload[a] = b'''

        payload = {
        'URL' : 'https://kbits-usw.labcollab.net/login?next_url=%2F',
        'USERNAME' : '*****', # User
        'PASSWORD' : '*****', # Pass
        'osText' : 'FireOS5',
        'shipText' : 'Ship_5210',
        'deviceText1B' : 'bueller_ship_5210',
        'deviceText2S' : 'full_sloane_ship_5210',
        'deviceText3M' : 'montoya_ship_5210',
        'fosDate' : '/html/body/div/table/tbody/tr[4]/td/table/tbody/tr[3]/td[4]',
        'fosStatus' : '/html/body/div/table/tbody/tr[4]/td/table/tbody/tr[3]/td[3]',
        'fosFile' : '/html/body/div/table/tbody/tr[4]/td/table/tbody/tr[3]/td[5]/a/img',
        'buildType' : '//*[@id="filetree"]/ul/li[10]/div/a',
        'buildLoc1B' : '//*[@id="filetree"]/ul/li[10]/ul/li[16]/div/span/a/span',
        'buildLoc2S' : '//*[@id="filetree"]/ul/li[10]/ul/li[16]/div/span/a/span',
        'buildLoc3M' : '//*[@id="filetree"]/ul/li[10]/ul/li[14]/div/span/a/span'
        }
        bueller = deviceType()
        sloane = deviceType()
        montoya = deviceType()
        bueller.loginDriver(payload['URL'], payload['USERNAME'], payload['PASSWORD'])
        bueller.shipBranchElements(payload['osText'], payload['shipText'], payload['deviceText1B'])
        bueller.fileSearch(payload['fosDate'], payload['fosStatus'], payload['fosFile'])
        bueller.download(payload['buildType'], payload['buildLoc1B'])
        sloane.loginDriver(payload['URL'], payload['USERNAME'], payload['PASSWORD'])
        sloane.shipBranchElements(payload['osText'], payload['shipText'], payload['deviceText2S'])
        sloane.fileSearch(payload['fosDate'], payload['fosStatus'], payload['fosFile'])
        sloane.download(payload['buildType'], payload['buildLoc2S'])
        montoya.loginDriver(payload['URL'], payload['USERNAME'], payload['PASSWORD'])
        montoya.shipBranchElements(payload['osText'], payload['shipText'], payload['deviceText3M'])
        montoya.fileSearch(payload['fosDate'], payload['fosStatus'], payload['fosFile'])
        montoya.download(payload['buildType'], payload['buildLoc3M'])
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    main()
