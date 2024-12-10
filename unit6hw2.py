def isInteger(check):
    #create a word bank
    digits  = "+-0123456789"
    ABCs = "abcdefghijklmnopqrstuvwxyz"
    #strip the code of leadind and trailing white space
    check = check.strip()
    #check for digits and ABCs
    for character in ABCs:
        if character in check:
            return False
        
    for character in digits:
        if character in check:
#return true and false 
            return True
    return False


print(isInteger("123"))        
print(isInteger("   -456  "))  
print(isInteger("+789"))       
print(isInteger("abc"))        
print(isInteger("  "))         
print(isInteger("-ji"))          