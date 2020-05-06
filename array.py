#simple program to add elements in an array
#hackerank problem#2
def simpleArraySum(array):
    sum=0
    for i in array:
        sum += i
    print(sum)   
        


n = int(input("Enter number of elements"))
ar =list(map(int,input("\nEnter the elements").strip().split()))[:n] 
simpleArraySum(ar)

