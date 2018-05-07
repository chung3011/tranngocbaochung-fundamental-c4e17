def calc(x,y,op):
    if op not in ['+','-','*','/']:
        res="error"
    else:
        if op == "+":
            res=x+y
        elif op == "-":
            res=x-y
        elif op == "*":
            res=x*y
        elif op == "/":
            res=x/y
        res=round(res,2)
    return(res)
# x=int(input("x= "))
# y=int(input("y= "))
# op=input("op: ")
# print("Result:",calc(x,y,op))
# print(__name__)
if __name__=="__main__":
    print("eval.py imported")
