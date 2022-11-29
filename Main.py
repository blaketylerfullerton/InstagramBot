from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import getpass
import pickle

print("Starting...")

username = input("What is your username? : ")

options = Options()
options.add_argument(("user-data-dir=" + str(username)))
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
options.headless = True
driver = webdriver.Chrome(chrome_options=options)

sleep(3)

def get_credentials(username):
  
  password = getpass.getpass()

  login(username, password)

def login(username, password):
  print ("Logging in...")
  driver.get("https://instagram.com/accounts/login/")
  sleep(3)
  x = driver.find_element_by_name("username")
  x.click()
  x.send_keys(username)
  y = driver.find_element_by_name("password")
  y.click()
  y.send_keys(password)
  login_button = driver.find_element_by_xpath("html/body/div/section/main/div/article/div/div/div/form/div[4]/button")
  login_button.click()
  sleep(3)
  try:
    driver.get("https://instagram.com/accounts/login/")
    sleep(3)
    x = driver.find_element_by_name("username")
    print("Login failed. Try password again...")
    get_credentials(username)
  except:
    logged_in()

def startliking():
    print ("Liking image: " + str(driver.current_url))

    sleep(2)

    driver.find_element_by_xpath("html/body/div[4]/div[2]/div/article/div[2]/section/span/button").click()

    print ("Image liked")

    driver.find_element_by_xpath("html/body/div[4]/div/div/div/a[2]").click()

def logged_in():
  print("Login Successful!")

  hashtag = input("Which hashtag do you want to like? (one word): ")

  driver.get("https://www.instagram.com/explore/tags/%s/" % hashtag)
  driver.find_element_by_xpath("html/body/div/section/main/article/div[2]/div/div/div").click()

  print("Getting #%s posts..." % hashtag)

  sleep(2)
  
  for i in range(10000):
    try:
      startliking()
    except Exception as e:
      print("Gotta refresh...")
      driver.get("https://www.instagram.com/explore/tags/%s/" % hashtag)
      driver.find_element_by_xpath("html/body/div/section/main/article/div[2]/div/div/div").click()
      print("Done. Continuing.")
      pass
    
try:
  driver.get("https://instagram.com/accounts/login/")
  sleep(3)
  x = driver.find_element_by_name("username")
  get_credentials(username)
  
except KeyboardInterrupt:
  exit()
except:
  logged_in()
