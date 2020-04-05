link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    #функция для открытия страницы с логином
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser): 
    browser.get(link) 
    go_to_login_page(browser)
    #вызываем функцию открытия страницы с логином

