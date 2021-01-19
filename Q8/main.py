s = input()

alpha = []
num = []

for i in range(len(s)):
  if s[i].isalpha():
    alpha.append(s[i])
  else:
    num.append(int(s[i]))

alpha.sort()

for c in alpha:
  print(c,end='')
print(sum(num))