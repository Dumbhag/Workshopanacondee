# จงเขียนโปรแกรม Python คำนวณค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยวของกรุ๊ปทัวร์ ทั้งนี้รูปแบบการใช้งาน
# โปรแกรมจะต้องป้อนชื่อหัวหน้ากรุ๊ปทัวร์ เบอร์โทรศัพท์ติดต่อกลับของหัวหน้ากรุ๊ปทัวร์ และจำนวนคนที่จะไปทัวร์ 
# ทางแป้นพิมพ์ โดยในการคิดคำนวณค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยวของกรุ๊ปทัวร์ มีหลักเกณฑ์ในการคิดคำนวณ ดังนี้ 
# จำนวนคนที จะไปทัวร์ตั้งแต่ 1 - 2 คน คิดแพ็กเกจละ 300 บาทต่อคน
# จำนวนคนที จะไปทัวร์ตั้งแต่ 3 - 5 คน คิดแพ็กเกจละ 250 บาทต่อคน
# จำนวนคนที จะไปทัวร์ตั้งแต่ 6 - 10 คน คิดแพ็กเกจละ 210 บาทต่อคน
# จำนวนคนที จะไปทัวร์ตั้งแต่ 11 คนขึ้นไป คิดแพ็กเกจละ 150 บาทต่อคน

def SMT() :
    print('ค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยวของกรุ๊ปทัวร์')

def inputData() :
    count = int(input('ป้อนจำวนคน : '))
    return count

def C(acount) :
    if count <= 2 :
        print(f'จำนวน{acount}คน คิดแพ็กเกจละ 300 บาทต่อคน')
    elif count >= 3 and count <= 5 :
        print(f'จำนวน{acount}คน คิดแพ็กเกจละ 250 บาทต่อคน')
    elif count >= 6 and count <= 10 :
        print(f'จำนวน{count}คน คิดแพ็กเกจละ 210 บาทต่อคน')    
    else :
        print(f'จำนวน{count}คน คิดแพ็กเกจละ 150 บาทต่อคน')
print('----------------------------------------------')
SMT()
print('----------------------------------------------')
count =inputData()
print('----------------------------------------------')
C(count)
print('----------------------------------------------')

#⠀⠀⠀⠀⠀⠀⣀⣀⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⣀⡴⠛⠁⢀⡴⢚⣩⠭⠟⠛⠋⠉⠉⠉⠉⠉⠛⠲⢤⡀⠀⠀⠀⠀⠀⠀
#⠀⠀⡼⠋⠀⠀⢀⡿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⠀⠀⠀
#⠀⣸⠧⠤⣄⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀
#⠘⠷⢶⡚⢹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀
#⠀⠀⠀⢳⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⣀⣀⣤
#⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣭⣿⣿
#⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⢉⠥⠐
#⢀⣀⣠⣤⣴⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠘⢲⣐
#⣿⣿⣿⣾⡿⠿⠿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣦⡀⠀⠀⠀⣸⠛⠋⠉⠁
#⠉⡩⠒⠒⠈⢉⡆⠙⣦⠀⠀⠀⠀⠀⢠⠴⠞⠛⠛⠉⠉⢳⣤⡤⠶⡏⠀⠀⠀⠀
#⠀⠙⣒⣒⣬⡭⠴⠖⠚⢳⡄⠀⢀⣀⡼⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠙⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀