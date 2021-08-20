from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep,time
import re # regular expression library (regex) to make output cleaner to the eye


class bcolors: # terminal colors for regex errors and stuff like that </3
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def bordered(text,title=""):
    text = bcolors.FAIL+title+bcolors.ENDC+"\n"+text
    text = text.splitlines()
    maxlen = max(len(s) for s in text)
    colwidth = maxlen + 2
    TORET = ""

    TORET += '+' + '-'*colwidth + '+\n'
    for s in text:
        TORET += '| %-*.*s ' % (maxlen, maxlen, s) + "\n"
    TORET += '+' + '-'*colwidth + '+\n'
    return TORET

last = time()
options = Options()
options.headless = True # there is no need for user interface so make it as fast as possible
driver = webdriver.Firefox(options=options, executable_path="C:\\Users\\floyd\\Downloads\\geckodriver.exe") # the firefox driver to make it work
print("Headless firefox driver started")
print("Took "+bcolors.OKGREEN+str(time()-last)+bcolors.ENDC+" seconds from last varset")
last = time()
driver.get('https://devforum.roblox.com/c/help-and-feedback/scripting-support') # send the driver the URL to open
try: # wait for the page to load by waiting for the topic box's XPATH to be found, 10 sec timeout
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody"))
    )
except Exception:
    print(Exception)
print("Loaded page")
print("Took "+bcolors.OKGREEN+str(time()-last)+bcolors.ENDC+" seconds from last varset")
last = time()

# next 7 lines: get the first 3 topics in the page body based on the element's XPATH
elm1 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody")
elm2 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody/tr[1]")
ref2 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody/tr[1]/td/span/a").get_attribute("href")
replies2 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[3]").get_attribute("title")
elm3 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody/tr[2]")
ref3 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody/tr[2]/td/span/a").get_attribute("href")
replies3 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[3]").get_attribute("title")
elm4 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody/tr[3]")
ref4 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody/tr[3]/td/span/a").get_attribute("href")
replies4 = driver.find_element_by_xpath("/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[3]/table/tbody/tr[3]/td[3]").get_attribute("title")
text2 = elm2.text
text3 = elm3.text
text4 = elm4.text

# regex to find text until a newline occurance
text2match = re.match(r"(?P<name>[A-Za-z\t .,\'’[\]\"]+)",text2)
if text2match:
    text2 = text2match.group()

text3match = re.match(r"(?P<name>[A-Za-z\t .,\'’\[\]\"]+)",text3)
if text3match:
    text3 = text3match.group()

text4match = re.match(r"(?P<name>[A-Za-z\t .,\'’[\]\"]+)",text4)
if text4match:
    text4 = text4match.group()

print("Indexed and regexed entries")
print("Took "+bcolors.OKGREEN+str(time()-last)+bcolors.ENDC+" seconds from last varset")
last = time()

# print out their text attributes and quit the driver
if text2match:
    apt = ""
    apt += text2+"\n\n"
    apt += bcolors.OKCYAN+replies2+bcolors.ENDC+"\n"
    apt += "Reference URL: "+bcolors.OKBLUE+ref2+bcolors.ENDC+"\n"
    print(bordered(apt,"Match #1")+"\n")
else:
    apt = ""
    apt += bcolors.FAIL+"TEXT MATCH #1 (ID=2) FAILED: no regex group"+bcolors.ENDC
    print(bordered(apt,"Match #1")+"\n")
if text3match:
    apt = ""
    apt += text3+"\n\n"
    apt += bcolors.OKCYAN+replies3+bcolors.ENDC+"\n"
    apt += "Reference URL: "+bcolors.OKBLUE+ref3+bcolors.ENDC+"\n"
    print(bordered(apt,"Match #2")+"\n")
else:
    apt = ""
    apt += bcolors.FAIL+"TEXT MATCH #2 (ID=3) FAILED: no regex group"+bcolors.ENDC
    print(bordered(apt,"Match #2")+"\n")
if text4match:
    apt = ""
    apt += text4+"\n\n"
    apt += bcolors.OKCYAN+replies4+bcolors.ENDC+"\n"
    apt += "Reference URL: "+bcolors.OKBLUE+ref4+bcolors.ENDC+"\n"
    print(bordered(apt,"Match #3")+"\n")
else:
    apt = ""
    apt += bcolors.FAIL+"TEXT MATCH #3 (ID=4) FAILED: no regex group"+bcolors.ENDC
    print(bordered(apt,"Match #3")+"\n")
driver.quit()
