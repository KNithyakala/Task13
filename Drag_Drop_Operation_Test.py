"""
Here we are going to verify drag and drop operation in the Url 'https://jqueryui.com/droppable/'.
Using Actionchains we are going to do drag and drop.

Test Cases:
Positive Test Cases:
1. Validation of background color
2. Validation of Text message

Negative Test Cases:
3. Validation of background color
4. Validation of Text message

"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Testcase 1
def test_positive_drag_drop_backgroundcolor():
    """
     Validate background color before and after drag and drop.
    """
    try:
        #Initialization of Chrome Driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        #Navigate to a URL
        driver.get('https://jqueryui.com/droppable/')

        #Instance creation of Action Chain class
        actions = ActionChains(driver)

        #Assigning variables with rgba values to validate background color
        Expected_before_color='rgba(0, 0, 0, 0)' #white color
        Expected_after_color='rgba(255, 250, 144, 1)' #yellow color

        # Identifying frame using find element and getting background color
        Droppable_frame=driver.find_element(By.XPATH,'//div[@id="content"]/iframe')
        Actual_before_color=Droppable_frame.value_of_css_property("background-color")

        #Switching to frame
        driver.switch_to.frame(Droppable_frame)

        #Identifying drag and drop element in the frame
        Drag_me_element=driver.find_element(By.XPATH,"//div[@id='draggable']")
        Drop_here_element=driver.find_element(By.XPATH,"//div[@id='droppable']")

        #Doing drag and drop using Actionchains
        actions.drag_and_drop(source=Drag_me_element, target=Drop_here_element).perform()

        #Identifying dropped box and getting background color & text
        Dropped_element=driver.find_element(By.XPATH,'//div[@id="droppable"]/p')
        Actual_after_color=Drop_here_element.value_of_css_property("background-color")

        #Validating background color
        assert Actual_before_color==Expected_before_color, "Background color before drop is not matched."
        assert Actual_after_color==Expected_after_color, "Background color after drop is not matched."

    finally:
        #Close the browser
        driver.quit()

#Test Case2
def test_positive_drag_drop_text():
    """
    Validate text in drop box after dropping operation.
    """
    try:
        # Initialization of Chrome Driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Navigate to a URL
        driver.get('https://jqueryui.com/droppable/')

        # Instance creation of Action Chain class
        actions = ActionChains(driver)

        # Identifying frame using find element and getting background color
        Droppable_frame = driver.find_element(By.XPATH, '//div[@id="content"]/iframe')

        # Switching to frame
        driver.switch_to.frame(Droppable_frame)

        # Identifying drag and drop element in the frame
        Drag_me_element = driver.find_element(By.XPATH, "//div[@id='draggable']")
        Drop_here_element = driver.find_element(By.XPATH, "//div[@id='droppable']")

        # Doing drag and drop using Actionchains
        actions.drag_and_drop(source=Drag_me_element, target=Drop_here_element).perform()


        # Identifying dropped box and getting background color & text
        Dropped_element = driver.find_element(By.XPATH, '//div[@id="droppable"]/p')

        Actual_TextMessage = Dropped_element.text
        Expected_TextMessage = "Dropped!"

        # Validating text after dropped element
        assert Actual_TextMessage == Expected_TextMessage, "Drag and Drop is not done properly."

    finally:
        # Close the browser
        driver.quit()

#Test Case 3
def test_negative_drag_drop_color():
    """
    Here we are going to give source and target of drag and drop method as same.
    So, drag and drop will not work. and we are validating background color is not changed
    """
    try:
        # Initialization of Chrome Driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Navigate to a URL
        driver.get('https://jqueryui.com/droppable/')

        # Instance creation of Action Chain class
        actions = ActionChains(driver)

        # Assigning variables with rgba values to validate background color
        Expected_before_color = 'rgba(0, 0, 0, 0)'  # white color
        Expected_after_color = 'rgba(255, 250, 144, 1)'  # yellow color

        # Identifying frame using find element and getting background color
        Droppable_frame = driver.find_element(By.XPATH, '//div[@id="content"]/iframe')
        Actual_before_color = Droppable_frame.value_of_css_property("background-color")

        # Switching to frame
        driver.switch_to.frame(Droppable_frame)

        # Identifying drag and drop element in the frame
        Drag_me_element = driver.find_element(By.XPATH, "//div[@id='draggable']")
        Drop_here_element = driver.find_element(By.XPATH, "//div[@id='droppable']")

        # Doing drag and drop using Actionchains
        actions.drag_and_drop(source=Drop_here_element, target=Drop_here_element).perform()

        # Identifying dropped box and getting background color & text
        Dropped_element = driver.find_element(By.XPATH, '//div[@id="droppable"]/p')
        Actual_after_color = Drop_here_element.value_of_css_property("background-color")

        # Validating background color
        assert Actual_before_color == Expected_before_color, "Background color before drop is not matched."
        assert Actual_after_color != Expected_after_color, "Background color after drop is not matched."
    finally:
        # Close the browser
        driver.quit()

#Test Case 4
def test_negative_drag_drop_text():
    """
    Here we are going to give source and target of drag and drop method as same.
    So, drag and drop will not work. and we are validating text is not changed to dropped
    """
    try:
        # Initialization of Chrome Driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Navigate to a URL
        driver.get('https://jqueryui.com/droppable/')

        # Instance creation of Action Chain class
        actions = ActionChains(driver)

        # Identifying frame using find element and getting background color
        Droppable_frame = driver.find_element(By.XPATH, '//div[@id="content"]/iframe')

        # Switching to frame
        driver.switch_to.frame(Droppable_frame)

        # Identifying drag and drop element in the frame
        Drag_me_element = driver.find_element(By.XPATH, "//div[@id='draggable']")
        Drop_here_element = driver.find_element(By.XPATH, "//div[@id='droppable']")

        # Doing drag and drop using Actionchains
        actions.drag_and_drop(source=Drag_me_element, target=Drag_me_element).perform()

        # Identifying dropped box and getting text
        Dropped_element = driver.find_element(By.XPATH, '//div[@id="droppable"]/p')
        Actual_TextMessage = Dropped_element.text

        #Creating a variable for expected text message in the box
        Expected_TextMessage = "Dropped!"

        # Validating text after dropped element
        assert Actual_TextMessage != Expected_TextMessage, "Drag and Drop is not done properly."

    finally:
        # Close the browser
        driver.quit()

