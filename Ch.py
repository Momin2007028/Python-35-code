Q-2: A
  # AB
  ABC
 ABCD
ABCDE #


n=5
k=5
for  i in range(65,70):
    for j in range(1,k):
        print(end=" ")
    k=k-1
    for j in range(65,i+1):
        print(chr(j),end="")
    print()
