from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://account.mail.ru/login?page=https%3A%2F%2Faccount.mail.ru%2F%3F&')
input_username = driver.find_element_by_xpath("//input[@name='username']")
input_username.send_keys('Логин для профиля без @')
input_voiti = driver.find_element_by_xpath("//span[@class='inner-0-2-89 innerTextWrapper-0-2-90']").click()
input_password = driver.find_element_by_xpath("//input[@name='password']")
input_password.send_keys('Пароль для профиля')
input_voitiPass = driver.find_element_by_xpath("//span[@class='inner-0-2-89 innerTextWrapper-0-2-90']").click()
driver.implicitly_wait(2000)
input_Profile = driver.find_element_by_xpath("//div[@class='ph-project ph-project__account svelte-1hiqrvn ph-project-any']").click()
capture_path = '/адрес сохранения картинки/mailrutest.png'
driver.save_screenshot(capture_path)
browser.quit()
