n,k= map(int,input().split())
result =0
#N이 k이상이면 계속 나누기 
while n>= k:
    #n이 k로 나누어 떨어지지 않는다면 N에서 1씩 빼기 
    while n %k !=0:
        n-=1
        result += 1
        #print(n,k,"1")
    #K로 나누기 
    n //= k
    result += 1
    #print(n,k,"2")
 #마지막 남은 수에 대하여 1씩 빼기 (2) 
while n> 1:
    n-=1
    result += 1
    #print(n,k,"3")
print(result)