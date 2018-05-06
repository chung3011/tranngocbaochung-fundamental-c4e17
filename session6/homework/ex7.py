def remove_dollar_sign (s):
    newstr = s.replace("$","")
    return(newstr)
if __name__=="__main__":
    s=input("Input a string: ")
    print(remove_dollar_sign (s))
