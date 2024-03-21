"""
202111467 차일권
heapq 우선순위 큐를 사용하여 리스트 정렬하기
"""
import heapq  # heapq 모듈을 가져오기

def number_list(nums):
    heapq.heapify(nums)  # 주어진 리스트를 최소 힙으로 변환

    sorted_nums = []  # 정렬된 숫자들을 저장할 리스트를 초기화

    # 힙이 비어있을 때까지 반복
    while nums:
        sorted_nums.append(heapq.heappop(nums))  # 힙에서 가장 작은 원소를 꺼내서 정렬된 리스트에 추가한다

    return sorted_nums  # 정렬된 리스트를 반환

numbers = [1213, 12, 323, 211, 35, 429, 552, 916]  # 주어진 숫자들을 리스트에 저장

# 주어진 숫자들을 정렬하고 정렬된 리스트를 출력
sorted_numbers = number_list(numbers)
print("정렬된 리스트:", sorted_numbers)
