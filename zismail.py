print("Savings calculation program")
print("Zismail-Dev")
print("Program for Zismail")

while True:
    money = float(input("กรุณาใส่จำนวนเงิน (บาท) : "))
    percent = int(input("กรุณาใส่สัดส่วนการออม (เปอร์เซนต์) (50, 30, 20, 10) : "))

    # คำนวณค่าใช้จ่าย, เงินลงทุน, เงินที่ใช้ไม่ได้, และเงินที่เหลือสำหรับใช้ได้
    earn = (money * percent) /100
    expenses = earn * (percent / 100)
    investment = earn * 0.2
    unusable_money = earn * 0.3
    balance = money - earn

    # แสดงผลลัพธ์
    print(f"ค่าใช้จ่าย (expenses): {expenses:.2f} บาท")
    print(f"เงินลงทุน (investment): {investment:.2f} บาท")
    print(f"เงินที่ใช้ไม่ได้ (unusable_money): {unusable_money:.2f} บาท")
    print(f"เงินที่เหลือสำหรับใช้ได้ (remaining_money): {balance:.2f} บาท")
    
    another_round = input("ต้องการคำนวณเพิ่มเติมหรือไม่? (y/n): ")
    if another_round.lower() != 'y':
        print("ขอบคุณที่ใช้บริการครับ ลาก่อย")
        break