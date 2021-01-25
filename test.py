import time
from selenium import webdriver
from tqdm import tqdm


def login():
    driver.get("http://ks.rsmu.ru")   
    driver.find_element_by_name('authUserLogin').send_keys('KS_LOGIN')
    time.sleep(0.1)
    driver.find_element_by_name('authUserPass').send_keys('KS_PASS')
    time.sleep(0.15)
    driver.find_element_by_xpath('/html/body/div[4]/span/form/table/tbody/tr[4]/td[2]/input').click()
    time.sleep(1.5)

def contol_test():
# Зайти в контрольные тесты
    driver.find_element_by_xpath('/html/body/div[5]/ul/li[2]/span').click()
    time.sleep(0.3)
    driver.find_element_by_xpath('/html/body/div[5]/ul/li[2]/ul/li[2]/span').click()
    time.sleep(5)

def some_test():
# экзаменнационный тест
    driver.find_element_by_xpath('/html/body/div[5]/ul/li[2]/span').click()
    # тесты
    time.sleep(0.4)
    driver.find_element_by_xpath('/html/body/div[5]/ul/li[2]/ul/li[1]/span').click()
    # само
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="dfdGridCell_0_2_0"]').click()
    # курс 2
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="dfdGridBtn_0_btnShift_0"]').click()
    # дисциплины
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="dfdGridBody_TD_spOpen_1_4"]').click()
    # гистология
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="dfdGridBody_TD_spOpen_1_24"]').click()
    # экзамен
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="dfdGridBody_TD_spOpen_1_38"]').click()
    # модуль
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="dfdGridCell_1_45_0"]').click()
    # тест
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="dfdGridBtn_1_btnShift_0"]').click()
    # тест
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="dfdTestButton_Start"]').click()
    # старт
    time.sleep(0.6)

def complete():
    for i in range(69):
        info = driver.find_element_by_xpath('//*[@id="dfdTestWinMain_2"]')
        time.sleep(0.4)
        with open('some1.txt','a') as f:
            try:
                photo = driver.find_element_by_xpath('//*[@id="dfdTestWinMain_2"]/img').get_attribute('src')
                f.write(photo+'\n')
            except Exception:
                pass
            f.write(info.text +'\n'*2)
        driver.find_element_by_xpath('//*[@id="dfdTestButton_Next"]').click()  


def test():
    if 'ВСЕ ПРАВИЛЬНЫЕ' in driver.find_element_by_xpath('//*[@id="dfdTestWinMain_2"]').text:
        a=[]
        for j in range(1,8):
            try:
                driver.find_element_by_xpath(f'//*[@id="dfdTestWinMain_2"]/table/tbody/tr[{j}]/td[1]/label')
                a.append(j)
            except Exception:
                break
        a.pop()
        for i in a:
            driver.find_element_by_xpath(f'//*[@id="dfdTestWinMain_2"]/table/tbody/tr[{i}]/td[1]/label').click()
    else:
        driver.find_element_by_xpath('//*[@id="dfdTestWinMain_2"]/table/tbody/tr[1]/td[1]/label').click()
    

def result():
    driver.find_element_by_xpath('//*[@id="div_fdAlert"]/div[4]/input').click()
    res = driver.find_element_by_xpath('//*[@id="dfdTestWinMain_2"]/div/table/tbody/tr[2]/td[2]').text
    if '1' in res:
        driver.find_element_by_xpath('//*[@id="dfdTestButton_View"]').click()
        time.sleep(1)
        write_it = driver.find_element_by_xpath('//*[@id="dfdTestWinMain_view2"]/ul/li[1]').text
        time.sleep(1)
        with open('answers.txt','a') as f:
            try:
                photo = driver.find_element_by_xpath('//*[@id="dfdTestWinMain_view2"]/ul/li[1]/img').get_attribute('src')
                f.write(photo+'\n')
            except Exception:
                pass
            f.write(write_it + '\n')
            f.write('\n')
            f.close()


for i in tqdm(range(9)):
    try:
        driver = webdriver.Firefox(executable_path='path/to/geckodriver')
        login()
        for i in range(1,21):
            driver.execute_script("window.open('');")
            time.sleep(0.15)
            driver.switch_to.window(driver.window_handles[i])
            login()
            some_test()
            test()
        time.sleep(41*60)
        for i in range(1,21):
            driver.switch_to.window(driver.window_handles[i])
            result()
            time.sleep(0.2)
        driver.quit()
    except Exception as e:
        print(e)
