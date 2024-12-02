




import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def get_tor_proxy():
#     proxy = {
#         "proxyType": "MANUAL",
#         "httpProxy": "127.0.0.1:9150",
#         "sslProxy": "127.0.0.1:9150"
#     }
#     return proxy

# def configure_driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
    
#     driver = webdriver.Chrome(options=options)
#     return driver

# if __name__ == "__main__":
#     driver = configure_driver()

#     # Navigate to a website to verify the IP address change
#     driver.get("https://linkedin.com/uas/login/")

#     # Print the current page title and URL
#     print("Page Title:", driver.title)
#     print("Current URL:", driver.current_url)

#     # Close the WebDriver session
#     # driver.quit()



# Creating a webdriver instance
driver = webdriver.Chrome()
# This instance will be used to log into LinkedIn


# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")


# Make a request through Tor
# response = requests.get('https://linkedin.com/uas/login', proxies=proxies)

    
    # waiting for the page to load
time.sleep(5)
    
    # entering username
username = driver.find_element(By.ID, "username")
    
    # In case of an error, try changing the element
    # tag used here.
    
    # Enter Your Email Address
username.send_keys("mushfikarafin123@gmail.com")  

    # entering password
pword = driver.find_element(By.ID, "password")
    # In case of an error, try changing the element 
    # tag used here.

    # Enter Your Password
pword.send_keys("MushfikaRafin@123")


# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.



# Opening Kunal's Profile
# paste the URL of Kunal's profile here
texas_company = "https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102748797%22%5D&keywords=company&origin=FACETED_SEARCH&sid=Q0L"

driver.get(texas_company)        # this will open the link



# Give some time for the dynamic content to load
time.sleep(5)  # Adjust the sleep time as needed


# Wait until the page is fully loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Get the page source (which now includes dynamically loaded content)
html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')

# # Write the HTML content to a file
with open("F:\habib\Python\scrapping\LinkedIn\html_content\page_content.html", "w", encoding="utf-8") as file:
    file.write(html_content)


pagination_div = soup.find('div', id="ember609")  # Adjust class name as needed
pagination_child_div = pagination_div.find('div',class_="artdeco-pagination artdeco-pagination--has-controls ember-view pv5 ph2")

if pagination_div:
    print("pagination div found")

# Close the WebDriver session
driver.quit()

# url = "https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102748797%22%5D&keywords=company&origin=FACETED_SEARCH&sid=Q0L"

#  # Send an HTTP GET request to the URL
# response = requests.get(url)
# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Get the HTML content of the webpage
#     html_content = response.text

    # Now you can use Beautiful Soup to parse the HTML content
    # For example, you can create a BeautifulSoup object like this:
    # from bs4 import BeautifulSoup
# print(soup.prettify())  # Print the entire HTML for debugging purposes

# else:
#     print("Failed to retrieve the webpage. Status code:", response.status_code)


# Find the <ul> element by its ID
# ul_element = soup.find('ul', id='list')

# If Id does not exist
# Find all <ul> elements with the class "my-list"
# ul_elements = soup.find_all('ul', class_='reusable-search__entity-result-list list-style-none')
# div_element = soup.find('div', class_='reusable-search__entity-result-list list-style-none')

# Find all <ul> elements with the class "my-list"
# ul_elements = soup.find_all('ul', class_='my-list')
# ul_elements = div_element.find('ul')


# Find the parent <div> element by its ID

parent_div = soup.find('div', class_="pv0 ph0 mb2 artdeco-card overflow-hidden")
# Check if the parent <div> element was found
if parent_div:
    print('parent div found')
    # Find the child <div> element within the parent <div> by its class name
    ul_element = parent_div.find('ul')
    # find_ul = parent_div.find('ul', class_="reusable-search__entity-result-list list-style-none")
    # Check if the child <div> element was found
    if ul_element:
        print('ul found')
        for li in ul_element.find_all('li'):
                print("1")
    else:
        print("No <ul> element found inside the <div>.")
else:
    print("No <div> element found with the specified class.")


#  # Find the pagination div artdeco-card pv0 mb6
#     # artdeco-pagination artdeco-pagination--has-controls ember-view pv5 ph2 ember622
# pagination_div = soup.find('div', id="ember609")  # Adjust class name as needed
# # pagination_div = soup.find('div', class_="artdeco-card pv0 mb6")  # Adjust class name as needed
# # print(pagination_div.prettify())
# pagination_child_div = pagination_div.find('div',class_="artdeco-pagination artdeco-pagination--has-controls ember-view pv5 ph2")

# if pagination_div:
#      print("pagination div found")
#      if pagination_child_div:
#             print("pagination child div found")

#         # Find the next button 
#             next_button = pagination_div.find('button', class_='artdeco-button__text') if pagination_div else None
#         # Check if the next button is found
#             if next_button:
#                 print("next button found")
#                 # Click the next button
#                 next_button.click()
#                 time.sleep(5)  # Adjust the sleep time as needed
#             else:
#                 # No more pages, break out of the loop
#             #  break
#                 print("next button not found")

#     # Close the WebDriver session
# driver.quit()

# # Find the next pagination button
# pagination_ul = soup.find('ul', class_='artdeco-pagination__pages artdeco-pagination__pages--number')  # Adjust class name as needed
# # next_button = pagination_ul.find('li', class_='artdeco-pagination__indicator artdeco-pagination__indicator--number active selected ember-view').find('button') if pagination_ul else None
# next_button = pagination_ul.find('button', aria_current='true') if pagination_ul else None
# # Check if the next button is found
# if next_button:
#     # Click the next button
#     print("next button found")
#     driver.find_element_by_xpath("//button[contains(text(), 'Next')]").click()
#     time.sleep(5)  # Adjust the sleep time as needed
# else:
#     # No more pages, break out of the loop
#     # break
#     None

# # Close the WebDriver session
# driver.quit()

# start = time.time()
# # will be used in the while loop
# initialScroll = 0
# finalScroll = 1000

# while True:
#     driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
#     # this command scrolls the window starting from
#     # the pixel value stored in the initialScroll 
#     # variable to the pixel value stored at the
#     # finalScroll variable
#     initialScroll = finalScroll
#     finalScroll += 1000

#     # we will stop the script for 3 seconds so that 
#     # the data can load
#     time.sleep(3)
#     # You can change it as per your needs and internet speed

#     end = time.time()

#     # We will scroll for 20 seconds.
#     # You can change it as per your needs and internet speed
#     if round(end - start) > 20:
#         break


# src = driver.page_source
# # Now using beautiful soup
# soup = BeautifulSoup(src, 'lxml')


# # Extracting the HTML of the complete introduction box
# # that contains the name, company name, and the location
# intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

# print(intro)
