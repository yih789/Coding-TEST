# 입력 데이터의 개수가 많은 문제에서 input()
# 사용은 시간초과로 이어질 수 있다.
# 이를 해결하기 위해 sys 라이브러리 사용

import sys

# readline은 엔터를 포함하기 때문에 무조건 rstrip() 사용
data = sys.stdin.readline().rstrip()

print(data)