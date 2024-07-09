# 這個函式是用於說明主選單選項
def init():
    # 顯示主選單標題
    print("主選單:")
		# 顯示選項一
    print("1. 選項一")
		# 顯示選項二
    print("2. 選項二")
# 這個函式會接收一個參數，並根據參數判斷要回傳什麼內容的字串
def action(user_choice):
    # 如果選擇為1，顯示相應的訊息
    if user_choice == '1':
        return "你選擇了選項一。"
    # 如果選擇為2，顯示相應的訊息
    elif user_choice == '2':
        return "你選擇了選項二。"
# 程式的主入口點，確保只在直接執行這個程式時執行以下代碼
if __name__ == "__main__":
    # 顯示主選單說明文字
    init()
    # 要求使用者輸入選擇，並將使用者選擇結果用變數保存
    choice = input("請輸入選擇 (1/2): ")
    # 根據使用者選擇結果，利用自定義的action函式判斷要顯示什麼文字，並用變數保存回傳的判斷結果
    result = action(choice)
    # 顯示判斷結果
    print(result)