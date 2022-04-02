n=int(input('n='))
a=(n//2)+1
s=a-1
for i in range(1,a+1):
 print(' '*s,end=' ')
 for j in range(1,i+1):
  print('*',end=" ")
 s=s-1
 print(' ')
a=n//2
s=1
for i in range(a,0,-1):
 print(' '*s,end=' ')
 for j in range(1,i+1):
  print('*',end=' ')
 s=s+1
 print(' ')
