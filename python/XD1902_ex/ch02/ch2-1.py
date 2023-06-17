def FahrenheitConverter(c):
   return c *9/5 +32
while True:
  isQuit = input("是否結束？[type q to quit]: ")
  if isQuit == 'q':
       break
  c = int(input("請輸入攝氏溫度：").strip())
  output = FahrenheitConverter(c)
  print("華氏溫度是{} 度 F".format(output))