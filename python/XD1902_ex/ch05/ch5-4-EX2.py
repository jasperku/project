print("===============程式描述========================")
print("= 程式名稱：ch5-4-EX2.py                      =")
print("= 程式目的：建立單向鏈結串列                   =")
print("==============================================")
#實作單向鏈結串列
class ScoreNode :
   #初始化ScoreNode類別
   def __init__(node, data, link) :
      node.data = data       
      node.link = link

#產生物件 S1~S5
C1,C2,C3,C4,C5 = eval(input('請輸入一心、二聖、三多、四維，五福分數，並以逗點分隔：\n'))
S5 = ScoreNode(C5,None)
S4 = ScoreNode(C4,S5)
S3 = ScoreNode(C3,S4)
S2 = ScoreNode(C2,S3)
S1 = ScoreNode(C1,S2)
headNode = S1
print('[', S1.data, ']-> [', S2.data, ']-> [', S3.data, ']->[', S4.data, ']->[', S5.data, ']-> None') 