#Party of Couples
S = [1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6]
data = []
for i in S:
  num=0
  for j in range(len(S)):
    if i==S[j]:
      num+=1
  data.append(num)
fidata=data.index(1)
print(S[fidata])      
    

