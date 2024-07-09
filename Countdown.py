# 導入time模組，用於計時
import time


def countdown_timer(seconds):
    # 定義一個倒數計時函數，參數為倒數的秒數
    # 當秒數不為零時，進入迴圈
    while seconds:
        # 暫停一秒
        time.sleep(1)
        # 印出剩餘的秒數
        print(f"剩餘秒數：{seconds}秒")
        # 將秒數減一
        seconds -= 1
    # 當倒數結束時，顯示"Time's up!"
    print("Time's up!")


# 請使用者設定倒數計時的秒數
countdown_time = input("請輸入預計倒數的秒數：")
# 呼叫倒數計時函數並傳入countdown_time為參數
countdown_timer(int(countdown_time))
