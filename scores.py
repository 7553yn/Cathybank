def revisescore(wrongscores):
    rightscores = []  # 建立一個空列表，用於儲存修正後的成績

    for i in wrongscores:
        # 將十位數和個位數互換，然後添加到正確成績列表中
        units = i // 10
        tens = i % 10
        revisescore = tens * 10 + units
        rightscores.append(revisescore)

    return rightscores

# 輸入錯誤的成績列表
wrongscores = [35, 46, 57, 91, 29]

# 調用函數來修正成績
revisescores = revisescore(wrongscores)

# 列印修正後的成績
print(revisescores)
