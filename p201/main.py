# 떡 개수, 요청 떡 길이
N, M = map(int, input().split())

# 떡 길이 데이터
lenth_data = list(map(int, input().split()))

# 최대 길이 구하는 함수 # 이진탐색
def maximum_lenth(arr, leng, start, end):
  while(start <= end):
    total = 0
    mid = ( start + end ) // 2

    for lenth in arr:
      if( lenth > mid):
        total += lenth - mid

    if(total == leng): 
      return mid
    elif(total > leng):
      start = mid + 1
    else:
      end = mid - 1
  return None

result = maximum_lenth(lenth_data, M, 0, max(lenth_data))
print('최댓값 :', result)