from lesson_7.swag_labs.pages.shopmain import ShopmainPage
from lesson_7.swag_labs.pages.shopcontainer import ShopContainer

def test_shop(chrome_browser):
    expected_total = "58.29"

    shopmain = ShopmainPage(chrome_browser)
    shopmain.registration_fields()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.into_container()

    container = ShopContainer(chrome_browser)
    container.checkout()
    container.into()
    container.price()
    assert expected_total in container.price()
    print (f"итоговая сумма равна ${container.price()}")
    