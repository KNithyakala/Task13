"""
Here we are going to automate drag and drop operation in the Url 'https://jqueryui.com/droppable/'.
Using Actionchains we are going to do drag and drop.
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Automating drag and drop

#Initialization of Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Navigate to a URL
driver.get('https://jqueryui.com/droppable/')

#Instance creation of Action Chain class
actions = ActionChains(driver)

# Identifying frame using find element and getting background color
Droppable_frame=driver.find_element(By.XPATH,'//div[@id="content"]/iframe')

#Switching to frame
driver.switch_to.frame(Droppable_frame)

#Identifying drag and drop element in the frame
Drag_me_element=driver.find_element(By.XPATH,"//div[@id='draggable']")
Drop_here_element=driver.find_element(By.XPATH,"//div[@id='droppable']")

#Doing drag and drop using Actionchains
actions.drag_and_drop(source=Drag_me_element, target=Drop_here_element).perform()

#Screenshot of dropping box
driver.save_screenshot('Drag_Drop_Screenshot.png')

#Identifying dropped box and getting background color & text
Dropped_element=driver.find_element(By.XPATH,'//div[@id="droppable"]/p')

if (Dropped_element.text=="Dropped!"):
    print("Drag and Drop is done successfully.")

#Close the browser
driver.quit()
