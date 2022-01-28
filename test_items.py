import time


def test_guest_should_see_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    shop_button = browser.find_elements_by_css_selector(".btn.btn-lg")
    assert len(shop_button) > 0, "Basket button not found"
 ##