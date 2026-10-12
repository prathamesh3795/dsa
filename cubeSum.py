'''
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
print this pattern
'''
# n=int(input("Enter number of rows"))
# for i  in range(1,n+1):
#     for j  in range(1,i+1):
#         print(j,end=" ")
#     print()

# n=int(input("enter number"))
# sum=(n*(n+1)//2)**2
# print(sum)

# n=int(input("Enter number of rows"))
# for i  in range(n,0,-1):
#     for j  in range(i,0,-1):
#         print(j,end=" ")
#     print()

'''
            1
          1 2 1
        1  2  3  1
      1  2  3  4  1
    1  2  3  4   5  1
print this pattern
'''
# n=5
# sp=5
# for i in range(1,n+1):
#     for s in range(0,sp):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     if(i!=1):
#         print("1")
#     print()
#     sp-=1

# n = int(input("Enter no of rows :"))
# for i in range(n):
#     print( ' ' * (n-i+1) , end="")
#     for j in range(2*i+1):
#         print(chr(65+j), end=" ")
#     print()

n = int(input("Enter no of rows :"))
for i in range(n):
    print( ' ' * (n-i+1) , end="")
    for j in range(2*i+1):
        if (j==0 or j==2*i or i==n-1):
            print(chr(65+j), end=" ")
        else:
            print(" ",end=" ")
    
    print()
