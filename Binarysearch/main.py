# 이진탐색 함수
def binary_search(arr, target, start, end):
  while(start <= end):
    mid = (start + end) // 2
    # 중간점과 target 비교
    if (arr[mid] == target): # target과 중간점이 같다면
      return mid
    elif( target > arr[mid]): # target이 중간점보다 크다면
      start = mid + 1
    else: # target이 중간점보다 작다면
      end = mid - 1

# 데이터 개수, target 입력
n, target = map(int, input().split())

# 정렬할 데이터 입력
data = list(map(int, input().split()))

# 이진탐색 결과
result = binary_search(data, target, 0, len(data)-1)

if(result == None):
  print("해당 데이터가 존재하지 않습니다.")
else:
  print("{}의 위치는 {}번째 입니다.".format(target, result+1))