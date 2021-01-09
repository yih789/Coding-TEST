# 계수정렬 함수
def count_sort(arr):
  # 최댓값 크기의 리스트 생성
  # 0 초기화
  data = [0] * (max(arr)+1)

  for num in arr:
    data[num] += 1

  for i, count in enumerate(data):
    if count > 0:
      for _ in range(count):
        print(i, end=' ')

    
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count_sort(arr)