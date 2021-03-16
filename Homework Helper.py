from selenium import webdriver


lesson = str('Алгебра')
number = str(input('Введите номер задания: '))

def kf():
    global browser
    browser = webdriver.Chrome("C:\CH\chromedriver.exe")
    browser.set_window_size(1920, 1080)
    browser.get('https://reshak.ru/otvet/otvet15.php?otvet1='+(number))

if lesson == 'Алгебра':
    print('Открываю решебник по вашим данным')
    kf()
else:
    print('Введите в название предмета "Алгебра"')