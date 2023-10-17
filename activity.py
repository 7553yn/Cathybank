def findLastPerson(n):
    circle = list(range(1, n + 1))  # 創建一個由1到n的列表，表示人員圈子
    index = 0  # 表示當前報數的人在圈子中的索引位置
    
    while len(circle) > 1:
        index = (index + 2) % len(circle)  # 下一個報數的人的索引位置
        circle.pop(index)  # 將報數為3的人移出圈子
    
    return circle[0]

n = int(input("請輸入人數 n："))
lastPerson = findLastPerson(n)
print(f"最後留下的同事是第 {lastPerson} 順位")