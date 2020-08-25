from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'firefoxdriver/geckodriver.exe')
driver.get("https://orteil.dashnet.org/cookieclicker/")

actions = ActionChains(driver)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range (1, -1, -1)]
upgrade = []

actions = ActionChains(driver)
actions.click(cookie)

for i in range (5000): 
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])

    for item in items:
        value = int(item.text)

        if value <= count:
            if count > 50:
                upgrade = [driver.find_element_by_css_selector("div#upgrades div:nth-child(1)")]
                for up in upgrade:               
                    action = ActionChains(driver)
                    action.move_to_element(up).click().perform()

            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item).click().perform()  
