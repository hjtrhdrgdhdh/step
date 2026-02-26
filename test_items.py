import time
from selenium.webdriver.common.by import By


def test_add_to_basket_button_is_present(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(button) == 1, f"Ожидался уникальный элемент, найдено {len(button)}"





