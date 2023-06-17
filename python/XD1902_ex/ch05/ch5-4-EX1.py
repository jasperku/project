print("===============程式描述========================")
print("= 程式名稱：ch5-4-EX1.py                      =")
print("= 程式目的：單向鏈結串列                       =")
print("==============================================")
#實作單向鏈結串列
class ScoreNode :
   #初始化ScoreNode類別
   def __init__(node, data, link) :
      node.data = data       
      node.link = link
