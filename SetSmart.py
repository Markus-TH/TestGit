# import package
from selenium.webdriver import Edge
# specify path - using microsoft edge
# because setsmart do not work properly in chrome
driver = Edge(executable_path='E:/Microsoft edge driver/edgedriver_win64/msedgedriver.exe')
# open website
driver.get("https://tradings.maybank-ke.co.th/logonfirst.asp")

# fill out your id and password
driver.find_element_by_name("User").send_keys("your ID")
driver.find_element_by_name("Password").send_keys("your Password ”")
driver.find_element_by_name("Submit").click()
# click the accept button again
driver.find_element_by_xpath("//input[@type='button']").click()

# After u log in, u will have frame problem that makes selenium cannot find element directly
# thus, you need to identify frame first
a = driver.find_elements_by_css_selector("frame")
print(len(a))
# checked and identify where the setsmart button is located in
driver.switch_to.frame(a[1])
# click the button
driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr[3]/td[@onclick = 'javascript:SetSmart()']").click()
# successfully get into set smart automatically