# 導入time模組，用於計時
import time
# 匯入 tqdm 模組，用於在過程中顯示進度條，提供使用者視覺上的進度感知
import tqdm

def countdown_timer(seconds):
    # 定義一個倒數計時函數，參數為倒數的秒數
    # 當秒數不為零時，進入循環，並印出剩餘的秒數
    for second in tqdm.tqdm(range(seconds, 0, -1), desc="秒數倒數中"):
        # 暫停一秒
        time.sleep(1)
    # 當倒數結束時，顯示"Time's up!"
    print("Time's up!")

# 請使用者設定倒數計時的秒數
countdown_time = input("請輸入預計倒數的秒數：")
# 呼叫倒數計時函數並開始倒數
countdown_timer(int(countdown_time))