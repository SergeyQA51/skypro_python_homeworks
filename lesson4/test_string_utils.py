import pytest
from string_utils import StringUtils

utils = StringUtils ()

#capitalize

def test_capitalize():
    """positive test utilite - capitalize"""
    assert utils.capitalize("murmansk") == "Murmansk"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("123") == "123"
    """negative test utilite - capitalize"""
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("12345test") == "12345test"    

#trim
def test_trim():
    """positive test utilite - trim"""
    assert utils.trim(" word") == "word"
    assert utils.trim("  hello world  ") == "hello world  "
    assert utils.trim("  WORD  ") == "WORD  "
    """negative test utilite - trim"""
    assert utils.trim("") == ""

#to_list
@pytest.mark.parametrize('string, delimeter, result', [
    #positive
    ("яблоко, банан, апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1, 2, 3, 4, 5", ",", ["1","2","3","4","5"]),
    ("*@$", "@", ["*","@","$"]),
    #negative
    ("", None, []),
])        
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res=utils.to_list(string)
    else:
        res=utils.to_list(string, delimeter)  
    assert res == result      

#contains
@pytest.mark.parametrize('string, symbol, result', [
    """positive test"""
    ("банан", "б", True),
    ("кресло-качалка", "-", True),
    ("море", "е", True),
    ("123", "1", True),
    ("", "", True),
    """negative test"""
    ("Кострома", "к", False), 
    ("море", "E", True),   
])        
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol, result) 
    assert res == result

#delete symbol
@pytest.mark.parametrize('string, symbol, result', [
    """positive test"""
    ("Лук", "л", "ук"),
    ("Петр", "р", "Пет"),
    ("мордор", "м", "ордор"),
    ("Лютое месиво", " ", "Лютоемесиво"),
    ("комод", " ", "комод"),
    """negative test""" 
    ("Лук", "Л", "Лук"),
    ("Петр", "р", "Перт"),
    ("100500", "1", " "),   
])        
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol) 
    assert res == result

#starts_with
@pytest.mark.parametrize('string, symbol, result', [
    """positive test"""
    ("Лук", "Л", True),
    ("", "", True),
    ("Gangster", "G", True),
    ("+100500", "+", True),
    ("", "Б", False),
    ("Арбуз", "О", False),
    """negative test""" 
    ("", "Б", True),
     ("Лук", "л", True),    
])        
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol) 
    assert res == result

#end_with
@pytest.mark.parametrize('string, symbol, result', [
    """positive test"""
    ("Лук", "к", True),
    ("", "", True),
    ("Gangster", "r", True),
    ("+100500", "0", True),
    ("Ключ", "ь", False),
    ("Помощь", "щ", False), 
    """negative test""" 
    ("Day", "y", False),
    ("34562", "9", True),    
])        
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol) 
    assert res == result

#is_empty
@pytest.mark.parametrize('string, result', [
    """positive test"""
    ("", True),
    (" ", True),
    ("  ", True),
    ("не пусто", False),
    (" не пусто с пробелом в начале", False),
    ("404", False), 
    """negative test"""
    ("  ", False),
    ("не пусто", True),
])        
def test_is_empty(string, result):
    res = utils.end_with(string) 
    assert res == result

#list_to_string
@pytest.mark.parametrize('lst, joiner, result', [
    """positive test"""
    (["s", "o", "s"], ",", "s,o,s"),
    ([1, 2, 3, 4, 5], None, "1,2,3,4,5"),
    (["Первый", "Второй"], "-", "Первый-Второй"),
    ([], None, ""),
    ([], ",", ""),
    """negative test"""
    ([1, 2, 3, 4, 5], None, "5,4,3,2,1"),
    (["c", "u", "p"], ",", "c,у,п"), 
])        
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner) 
    assert res == result




