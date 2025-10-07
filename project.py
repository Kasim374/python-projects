print("welcome to the pattern generator and number analyser!")
print("Select an option:")
print("1. generate a pattern")
print("2. Analyze a range of number")
print("3. Exit")
ch=int(input("enter the number of choice :"))





if(ch==1) :
    i=int(input("enter the number of rows for the pattern:"))
    input(" triangle Pattern:")

    for i in range(1,i+1):
        stars="*" * i
        print(stars)
elif(ch==2):
    start_range=int(input("Enter the Start of the range:"))
    end_range=int(input("Enter the end of the range:"))
    total_sum=0
    for i in range(start_range,end_range):
      if i%2==0:
       print("number",i,"is even")
      else:
        print("number",i,"is odd")

    input("sum of all numbers from 2 to 15 is:")        
    print(start_range+end_range)
elif(ch==3):
    print("exit a program!. Goodbye Have a nice day")


