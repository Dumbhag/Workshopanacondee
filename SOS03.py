# จงเขียนโปรแกรม Python ของโปรแกรมคำนวณภาษี ณ ที่ จ่ายของสินค้า โดยรับชื่อสินค้า และราคาสินค้า 
# ทางแป้นพิมพ์และแสดงผลภาษีที่คำนวณได้ทางหน้าจอ ทั้งนี้ภาษีคิดที ร้อยละ 7 ของราคาสินค้า         (อย่างน้อย 3 ฟังก์ชั่น)

def A():
    product = float(input("กรุณากรอกราคาสินค้า: "))
    return product

def B(product):
    tax_rate = 7  
    tax = (product_price * tax_rate) / 100
    return tax

def C(tax_amount):
    print(f"ภาษีที่คำนวณได้: {tax_amount:.2f} บาท")
print("++++++++++++++++++++++")
print("++++คำนวนภาษีราคาสินค้า++")
print("++++++++++++++++++++++")
product_price = A()
print("++++++++++++++++++++++")
tax = B(product_price)
C(tax)
print("++++++++++++++++++++++")
