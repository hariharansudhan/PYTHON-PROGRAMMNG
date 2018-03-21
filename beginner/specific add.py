N=int(raw_input())
K=int(raw_input())
m=[]
sum=0
for i in range(0,N):
  r=int(raw_input())
  m.append(r)
for j in range(0,K):
  sum+=m[j]
print(sum)

