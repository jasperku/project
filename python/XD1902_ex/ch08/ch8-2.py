import math
R=0      #「半徑」變數
Area=0   #「圓面積」變數
Len=0    #「圓周長」變數
R=int(input("請輸入半徑："))
Area=int(math.pi*pow(R,5))
Len=int(2* math.pi *R)
print("圓面積=",Area)
print("圓周長=",Len)
