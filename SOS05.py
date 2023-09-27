# จงเขียนโปรแกรม Python คำนวนหาเงินเดือนสุทธิของพนักงาน แล้วแสดงผลทางหน้าจอ โดยรับค่ารหัส
# พนักงาน ชื่อพนักงาน และเงินเดือนปกติของพนักงานทางแป้นพิมพ์ ทั้งนี้เงินเดือนสุทธิของพนักงานนั้นจะต้องหัก
# ค่าภาษี และเบี้ยประกันสังคมออกจากเงินเดือนปกติเสียก่อน โดยที่ พนักงานต้องเสียภาษี 7% ของเงินเดือนปกติ 
# และจ่ายค่าเบี้ยประกันสังคม 500 บาท 
# สูตร เงินเดือนสุทธิ = เงินเดือนปกติ - (เงินเดือนปกติ * 7 / 100) - 500                          (อย่างน้อย 3 ฟังก์ชั่น)

def A():
    ID = input("ป้อนรหัสพนักงาน: ")
    NAME = input("ป้อนชื่อพนักงาน: ")
    MM = float(input("ป้อนเงินเดือนปกติของพนักงาน: "))
    return ID, NAME, MM

def B(MM):
    PC = 7  
    TAX = (MM * PC) / 100
    return TAX

def C():
    SSF = 500
    return SSF

def D(MM, TAX, SSF):
    NS = MM - TAX - SSF
    return NS

def E(ID, NAME, MM, TAX, SSF, NS):
    print(f"ป้อนรหัสพนักงาน : {ID}")
    print(f"ป้อนชื่อพนักงาน : {NAME}")
    print(f"ป้อนเงินเดือนปกติ : {MM:.2f} บาท")
    print(f"ภาษีเป็นเงิน : {TAX:.2f} บาท")
    print(f"ค่าเบี้ยประกันสังคม : {SSF:.2f} บาท")
    print(f"เงินเดือนสุทธิเป็นเงิน : {NS:.2f} บาท")

print("=================================")
print("====== คำนวณเงินเดือนพนักงาน =======")
print("=================================")
ID, NAME, MM = A()
print("=================================")
TAX = B(MM)
SSF = C()
NS = D(MM, TAX, SSF)
E(ID, NAME, MM, TAX, SSF, NS)
print("=================================")


#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣷⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢿⣿⣿⣿⡿⠟⠋⢁⣀⠀⠐⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⢴⣶⠾⠿⠿⠿⠶⢻⣿⣿⣿⣿⣿⣿⣿⢿⣿⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⡹⣗⣚⣫⠅⠠⣾⣿⣿⣁⠀⠈⠛⢿⣿⣿⣿⣿⠇⣏⠩⢻⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣍⠂⠀⠀⣴⡾⢻⣝⣛⡛⠦⠀⠀⠀⠙⢿⣿⡟⠀⣿⣟⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣽⣦⠀⠉⠂⢻⣿⣿⡿⠂⡀⠀⠀⠀⠀⠀⠀⠀⠛⠉⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡯⢹⡀⠀⠀⠙⠒⠶⠀⠈⠁⠀⠀⠀⢱⠀⠀⠸⣤⢼⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡀⡼⠀⠰⠚⢻⢦⣀⠀⠀⠀⠀⠀⠀⢨⠇⠀⠀⠀⢸⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⣄⡴⠻⠛⠀⠀⣠⣤⡀⠀⠀⠀⡞⠀⠀⠀⠀⢸⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣏⢳⣴⣶⠖⢋⡅⠀⠉⠀⠀⡞⠁⠀⠀⠀⣠⠞⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⡉⠉⠉⠁⠀⠀⢀⡼⠊⠀⠀⠀⣠⠞⠁⠀⠀⢸⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠖⠋⣿⢦⣄⣀⣠⡴⠋⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠔⢋⡟⠁⠀⢠⡏⠀⠠⣝⠓⠒⢲⣦⣾⡋⠀⠀⠀⠀⠀⠀⣼⣿⣿⠿⠿⢿⣿⣿⡟⠛⠉⠉⠀⠈⠙⠒⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢀⣀⠤⠖⠋⠁⠀⢀⡾⠀⠀⠀⠸⡇⠀⠀⠈⠓⡴⠛⡇⠀⣽⣗⠤⢄⠀⠀⣰⣿⣿⠏⠀⠀⠀⠀⠹⣧⠀⡀⠀⠀⠀⠈⠙⠢⠬⢻⣿⣷⣦⡀⠀⠀⠀
#⠀⢠⣶⡞⠉⠁⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⣷⠀⢀⣠⠞⠁⢀⡗⢺⡁⠘⢧⡀⠀⡼⠃⣿⡿⠀⠀⠀⠀⠀⠀⢹⣦⣥⡀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣷⡄⠀⠀
#⢠⠏⣿⠃⠀⠀⠀⠀⠀⠀⠐⢧⣄⡀⠀⠀⠀⠸⣦⣿⠁⠀⠀⣼⠀⠈⣇⠀⠀⠙⠞⠁⢀⣿⡇⠀⠀⠀⠀⣤⣴⣾⣿⣿⠿⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣷⠀⠀
#⣸⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣬⠿⠃⠀⠀⠀⠀⣿⠀⢀⣼⣿⠀⠀⣿⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⠉⠻⢿⡉⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡇⠀
#⡇⠀⢿⠀⠀⠀⠀⠀⠀⠀⢸⡟⠁⠀⠀⠀⠀⠀⠀⠁⠀⡟⢸⣿⡀⠀⣿⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⡀⣀⣀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⠀
#⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⢸⡇⡇⠀⣿⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠃⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣗⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⡇⢧⠀⢹⡄⠀⠀⠀⢺⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠏⠁⠀⠀⠀⠀⠀⣿⣿⡿⠛⠉⠉⢻⣿⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠘⡆⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⢿⣿⡏⠀⠀⠀⠀⢿⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⣿⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠐⠀⠸⡆⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢳⠚⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀