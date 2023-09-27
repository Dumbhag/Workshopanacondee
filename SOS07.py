# จงเขียนโปรแกรม Python ของโปรแกรม Game Bingo โดยให้ผู้ใช้ป้อนตัวเลขที่ต้องการทายทางแป้นพิมพ์ 
# แล้วให้โปรแกรมตรวจสอบว่าตรงกับที่โปรแกรมกำหนดไว้หรือไม่ในที นี้คือ 25 หากไม่ตรงให้แสดงข้อความว่า "Not Correct !!!." ทางหน้าจอ 
# หากตรงให้แสดงข้อความว่า "Correct, You are the winner"                   (อย่างน้อย 3 ฟังก์ชั่น)

import random

def A():
    return 25  

def B(user, number):
    return user == number

def C():
    number = A()
    print("ยินดีต้อนรับสู่ Game bingo นะไอสาส!!!!")

    while True:
        user = int(input("ใส่เลข : "))

        if user == 25:
            print("เหมือนเก่งอ่ะแต่ก็ถูก!!!")
            break

        if B(user, number):
            print("Correct, You are the winner")
            break
        else:
            print("เดาไม่ถูก กากวะเฮ้ย!!!")
print("      ⠀  ⠀   (\__/)  ")
print("             (•ㅅ•)      Don’t talk to    ")
print("          ＿ノヽ ノ＼＿      me or my son  ")
print("       `/　`/ ⌒Ｙ⌒ Ｙヽ     ever again.")
print("       ( 　(三ヽ人　 /  |                ")
print("        |　ﾉ⌒＼ ￣￣ヽ   ノ              ")
print("        ヽ＿＿＿＞､＿_／                   ")
print("           |　ﾉ⌒＼ ￣￣ヽノ               ")
print("           ｜( 王 ﾉ〈  (\__/)             ")
print("           /ﾐ`ー―彡\  (•ㅅ•)              ")
print("          / ╰    ╯ \ /    \>              ")
C()
print("=================================")











