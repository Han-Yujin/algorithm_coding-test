n = 1260
count = 0
coin_type = [500, 100, 50, 10]
for coin in coin_type:
    count += n // coin  # n을 coin으로 나눈 값 = coin의 갯수
    n %= coin  # n을 coin을 나눈 나머지 값으로 다시 계산
print(count)
