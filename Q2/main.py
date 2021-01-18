s_to_int = list(map(int, input()))

result = 0

for n in s_to_int:

  if result==0 or n==0 or n==1:
    result += n
  else:
    result *= n

print(result)