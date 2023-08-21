def add():
    fp=open("calculator2.txt","a")
    a=input("please enter first number:")
    b=input("please enter second number:")
    c=int(a)+int(b)
    print("result of ",a,"and",b,"is",c,file=fp)
    fp.close()


def sub():
    fp=open("calculator2.txt","a")
    a=input("please enter first number:")
    b=input("please enter second number:")
    c=int(a)-int(b)
    print("result of ",a,"and",b,"is",c,file=fp)
    fp.close()


def multiply():
    fp=open("calculator2.txt","a")
    a=input("please enter first number:")
    b=input("please enter second number:")
    c=int(a)*int(b)
    print("result of ",a,"and",b,"is",c,file=fp)

def divide():
    fp=open("calculator2.txt","a")
    a=input("please enter first number:")
    b=input("please enter second number:")
    c=int(a)/int(b)
    print("result of ",a,"and",b,"is",c,file=fp)
    fp.close()

def showresult():
   print("Show result")
   fp=open("calculator2.txt","r")
   print(fp.read())
   fp.close()
   
def main():
    while True:
      print("1. Add")
      print("2.Subtract")
      print("3.Multiply")
      print("4.Divide")
      print("0.Result")
      num=input("please input a number:")
      if num=='1':
         add()

      elif num=='2':
         sub()
      elif num=='3':
         multiply()
      elif num=='4':
         divide()
      elif num=='0':
        showresult()
         
      else:
         print("invalid")
        

main()