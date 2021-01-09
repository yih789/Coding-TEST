arr1 = [3, 6, 1, 2, 9, 4, 5, 5, 8]

# 파이썬 내장함수 sorted
# 정렬한 리스트를 반환하고 원래 리스트는 그대로이다.
result = sorted(arr1)

print(result)
print(arr1)

arr2 = [3, 6, 1, 2, 9, 4, 5, 5, 8]

# 리스트 객체의 내장 함수
# 반환값 없이 기존 리스트를 정렬한다.
result = arr2.sort()

print(result)
print(arr2)

# 내림차순
result = arr2.sort(reverse=True)

print(result)
print(arr2)


# 기본 정렬함수는 오름차순
# 내림차순
# 사용자가 정렬기준 정의 # key 매개변수를 사용
arr3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(arr3, key=setting)
print(result)