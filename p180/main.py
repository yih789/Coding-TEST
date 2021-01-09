N = int(input())

students = []

for i in range(N):
  A, B = input().split()
  B = int(B)
  students.append([A, B])

# 두 번째 원소를 기준으로
def score_sort(data):
  return data[1]

# 오름차순 정렬
students.sort(key=score_sort)

# 학생의 이름만 출력
for student in students:
  print(student[0], end=' ')

