import pytest 

def leapyear(val):
    try: 
        year = int(val)
    except ValueError:
        print("That's not an int!")
    if(year % 4 == 0): 
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True 
            else: 
                return False 
        else: 
            return True
    else: 
        return False 


def test_1():
    assert leapyear(2018) == False 
def test_2():
    assert leapyear(2020) == True
def test_3():
    assert leapyear(0) == False 

