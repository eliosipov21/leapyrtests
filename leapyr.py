'''
How to run the file: 
simply run the command: python ilya_osipov_hw1.py in the command line (or python3 ilya_osipov_hw1.py)
'''

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