sum,i=0,0
ListScore=[60,70,80,85,90]          #宣告「陣列」資料結構 
for i in range(0,len(ListScore)):   #使用FOR迴圈的演算法 
    sum+=ListScore[i]
Average=float(sum/len(ListScore))
print("平均成績：%f" %Average)
