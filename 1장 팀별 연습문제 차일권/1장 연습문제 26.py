"""
202111467 차일권
합집합 교집합 차집합을 정리하고 진부분집합인지 확인하기 
"""
def plus(A, B):  
    return list(set(A) | set(B))  # A와 B의 합집합을 반환

def kho(A, B):
    return list(set(A) & set(B))  # A와 B의 교집합을 반환

def cha(A, B):
    return list(set(A) - set(B))  # A와 B의 차집합을 반환

def real(A, B):  
    if set(A) == set(B):  # A와 B가 같은 집합인지 확인.
        return False  
    return set(A).issubset(set(B))  # 결과를 반환합니다.

A = [1, 2, 3,]
B = [1, 2, 3, 4]

# 각 함수를 호출하여 결과를 출력합니다.
plus_result = plus(A, B)
print("합집합:", plus_result)

kho_result = kho(A, B)
print("교집합:", kho_result)

cha_result = cha(A, B)
print("차집합:", cha_result)

real_result = real(A, B)
print("A는 B의 진부분집합입니까?", real_result)
