message = "\n請在每一次的詢問中加入一種比薩配料： "
message += "\n如果配料規劃完成了，請輸入'quit'來結束。"

pizza = ""

while pizza != 'quit':
    pizza = input(message)
    if pizza != 'quit':
        print("我們將會為您加入" + pizza + "於比薩中！")
