"""
202111467 차일권
피보나치 수열을 큐를 사용하여 계산하기
"""

from collections import deque  # collections 모듈에서 deque 클래스를 가져온다

def fibonacci_queue(n):
    if n <= 0:  # 만약 n이 0 이하면 빈 리스트를 반환한다
        return []

    fibonacci = deque([0, 1])  # deque를 사용하여 피보나치 수열의 처음 두 항을 담은 큐를 생성

    if n == 1:  # 만약 n이 1이면 첫 번째 피보나치 수열 값인 0을 반환
        return [0]

    list = [0, 1]  # 결과를 저장할 리스트를 초기화
    for i in range(2, n):  # 두 번째부터 n-1번째까지 반복
        fib_number = fibonacci[0] + fibonacci[1]  # 큐의 맨 앞의 두 항을 더하여 새로운 피보나치 수를 계산
        list.append(fib_number)  # 새로운 피보나치 수를 결과 리스트에 추가
        fibonacci.popleft()  # 큐의 맨 앞 항을 제거한다
        fibonacci.append(fib_number)  # 새로운 피보나치 수를 큐에 추가

    return list  # 결과 리스트를 반환

print(fibonacci_queue(10))  # 피보나치 수열의 처음 10개 항을 출력
