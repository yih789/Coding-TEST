# 삽입정렬 함수
def insertion_sort(arr):
  for i in range(1, len(arr)):
    for j in reversed(range(0, i)):
      if(arr[j] > arr[i]):
        j, i = i, j
        arr[j], arr[i] = arr[i], arr[j]
      else:
        break

arr = [9, 1, 3, 2, 7, 5, 6, 8, 4]

# 삽입정렬
insertion_sort(arr)
# 결과
print(arr)