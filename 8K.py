import cv2
import schedule
import time
from datetime import datetime
# 王
# 更改項目 刪除列出可用鏡頭程式以及更改videoCapture參數以達到減少程式運行時間的效果+debug
# 待測項目 在亞威時遇到無法拍出8000*6000的畫質的問題 我已debug完成希望能順利執行 (結案)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cnt = 0
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 8000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 4000)
#杜 貼心提醒 請把設定相機畫質寫在外面 不然會爛掉
def take_picture():
    if not cap.isOpened():
        print("無法抓取鏡頭")
        return


    ret, frame = cap.read()
    if ret:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"photo_{timestamp}.png"
        cv2.imwrite(filename, frame)
        global cnt
        cnt += 1
        print(f"已拍攝照片並保存為： {filename} [{cnt}]")
    else:
        print("無法讀取鏡頭 frame")


if __name__ == '__main__':

    schedule.every(3).seconds.do(take_picture)

    print("程式已啟動，按 Ctrl+C 退出")
    try:
        while True:
            time.sleep(1)
            schedule.run_pending()
    except KeyboardInterrupt:
        print("程式已结束")
        cap.release()