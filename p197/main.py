# 이진탐색 함수
def binary_search(arr, target, start, end):
  
  while(start <= end ):
    mid = ( start + end ) // 2
    
    if(target == arr[mid]):
      return mid
    elif(target > arr[mid]):
      start = mid+1
    else:
      end = mid-1

  return None

# 매장 안 부품 종류 개수
N = int(input())

# 매장 안 부품의 고유번호
N_data = list(map(int, input().split()))
# 이진탐색을 위한 정렬
N_data.sort()

# 손님 요청 부품 종류 개수
M = int(input())
M_data = list(map(int, input().split()))

for pro in M_data:
  result = binary_search(N_data, pro, 0, len(N_data)-1)
  if result == None:
    print('no')
  else:
    print('yes')

'''
리스트의 in, not in 연산자를 이용하여 부품 여부 확인
N = int(input())

# 매장 안 부품의 고유번호
N_data = list(map(int, input().split()))

# 손님 요청 부품 종류 개수
M = int(input())
M_data = list(map(int, input().split()))

for pro in M_data:
    if(pro in N_data):
        print('yes')
    else:
        print('no')
'''

