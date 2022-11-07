#攝氏('c)轉換成華氏('F)程式
#讓user輸入攝氏溫度，然後執行程式印出華氏溫度

#公式: 華氏等於(攝氏乘9/5) + 32。攝氏零度 = 100 X (9/5) + 32 = 華氏212度。

C_temperature = input('請輸入要換算的華氏溫度')
C_temperature = int(C_temperature)
F_temperature = int(C_temperature * 9 / 5 + 32)
print('華氏溫度為：', F_temperature)

#更好的寫法是直接寫成
# C_temperature = input('請輸入要換算的華氏溫度')
# C_temperature = float(C_temperature) ~~>用float是避免user輸入有小數點的值時造成程式有問題
# F_temperature = C_temperature * 9 / 5 + 32
# print('華氏溫度為：', F_temperature)