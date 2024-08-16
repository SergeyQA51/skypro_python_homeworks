from lesson_7.calculator.pages.calcMainPage import CalcMain

def test_calculator_assert(chrome_browser):
        calcmain = CalcMain(chrome_browser)
        calcmain.insert_time()
        calcmain.clicking_button()
        assert "15" in calcmain.wait_button_gettext()