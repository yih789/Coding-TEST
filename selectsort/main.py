# 선택정렬 함수
def select_sort(arr):
  # n -1번 반복
  for i in range(len(arr)-1):
    # 현재 위치를 최솟값으로 초기화
    min_index = i
    # 현재 위치보다 +1부터 끝까지 탐색
    for j in range(i+1,len(arr)):
      # 최솟값 인덱스 탐색
      if(arr[min_index] > arr[j]):
        min_index = j
    # swap
    arr[i], arr[min_index] = arr[min_index], arr[i]
  
  return i

arr = [9, 1, 3, 2, 7, 5, 6, 8]

# 선택정렬
select_sort(arr)
# 결과
print(arr)
