import re

#validation for postcode
#Aus postcodes range from 0200 - 9729
#Checks for a numbers of 3 and 4 digits in length - no range validation
def validatePostcode(postCode):
    try:    
        postTest = re.match('^[0-9]{3,4}$',str(postCode))
        if postTest is None:
            return False
        else:
            return True
    except:
        print('An error occured in validatePostcode')
        return False

#validation for date
#Checks format %d/%m/%Y %H:%M
def validateDate(inputDate):
    try:    
        dateTest = re.match('^\d{1,2}\/\d{2}\/\d{4} \d{1,2}:\d{2}$',str(inputDate))
        if dateTest is None:
            return False
        else:
            return True
    except:
        print('An error occured in validateDate')
        return False

#validation for amounts
#Checks for sign, digits, decimal, and where applicable 1-2 decimal places
def validateDollarAmount(inputAmount):
    try:    
        amountTest = re.match('^[+-]?\d\d*\.?\d?\d?$',str(inputAmount))
        if amountTest is None:
            return False
        else:
            return True
    except:
        print('An error occured in validateDollarAmount')
        return False

#validation for numeric ID
#Checks for numeric value
def validateNumeric(inputNumeric):
    try:    
        numericTest = re.match('^\d{1,}$',str(inputNumeric))
        if numericTest is None:
            return False
        else:
            return True
    except:
        print('An error occured in validateNumeric')
        return False