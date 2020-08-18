a=int(input("enter any no: "))
b=int(input("enter any no: "))
def calc(a,b):
  print("1.add\n2.sub\n3.mul\n4.div")
  n=int(input("enter your choice: "))
  if n==1:
     def add(a,b):
        print(a+b)
     return add(a,b)
  elif(n==2):
      def sub(a,b):
        print(a-b)
      return sub(a,b)
  elif(n==3):
      def mul(a,b):
        print(a*b)
      return mul(a,b)
  else:
      def div(a,b):
        print(a/b)
      return div(a,b)
  
calc(a,b)
while True:
  m=input("repeat this calc press'y': ")
  if(m=='y'):
      a=int(input("enter any no: "))
      b=int(input("enter any no: "))
      calc(a,b)
  else:
    print("exit:)")
    break
