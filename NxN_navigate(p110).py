# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:39:21 2023

@author: ITWILL
"""

#n을 입력받기 
n= int (input())
x,y=1,1 #초기 상태
plans=input().split()  #가는 방향 입력받기
dx =[0,0,-1,1]  # L R U D에 대한 x좌표 
dy=[-1,1,0,0] # L R U D에 대한 y좌표
move_types=['L','R','U','D']

#이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기 
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i] #x좌표
            ny = y+dy[i]
        #공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y = nx,ny
    
    
print(x,y)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            