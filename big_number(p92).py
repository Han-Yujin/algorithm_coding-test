#N,M,K를 공백으로 구분하여 입력받기 
n,m,k= map(int,input().split())
#N개의 수를 공백으로 구분하여 입력받기 
data = list(map(int,input().split()))

data.sort # 입력받은 수 정렬
first = data[n-1]
second = data[n-2]


count = int(m/(k+1))*k
count+= m%(k+1)

result =0
result += (count) *first
result += (m-count) * second
print(result)



# =============================================================================
# result =0
# 
# while True:
#   for i in range(k):
#     if m==0: #m이 0이라면 반복문 탈출 
#       break
#     result += first 
#     m-=1 # 더할 때 마다 1씩 빼기
#   if m==0:
#     break
#   result += second
#   m-=1 
# print(result)
# =============================================================================