x='NIKHILPATIL'
x= x.upper()
for i in range(len(x)):
  counter = 0
  for j in range(len(x)):
       if i == j or x[i] == x[j]:
           continue
       else:
           counter +=1
  if  counter == len(x) -1:
      print(f"first non repetitive letter is {x[i]}")
      break
cnt = 0
print(x)
for i in x:
    if i in ['A', 'E', 'I', 'O' ,'U']:
        print(i)
        cnt +=1
print("number of vowels is", cnt)