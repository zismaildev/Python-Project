print("Savings calculation program")
print("Zismail-Dev")
print("Program for Zismail")

while True:
    money = float(input("กรุณาใส่จำนวนเงิน (บาท) : "))
    percent = int(input("กรุณาใส่สัดส่วนการออม (เปอร์เซนต์) : "))

    # คำนวณค่าใช้จ่าย, เงินลงทุน, ซื้อของให่้ตัวเอง,เงินที่ใช้ไม่ได้, และเงินที่เหลือสำหรับใช้ได้
    # ถ้าอยากให้เก็บเงินได้เยอะๆ ปรับ 0.2 ลง
    # ถ้าอยากให้เแบ่งเก็บเงินน้อยๆ ปรับ 0.2ขี้น
    # ถ้าจะเพิ่มก็ต้องเพิ่มและ คำนวนดูก่อน แล้วค่อยเขียนเพิ่ม

    earn = (money * percent) /100
    expenses = earn * 0.4
    investment = earn * 0.2
    youself = earn * 0.2
    unusable_money = earn * 0.2
    balance = money - earn

    # แสดงผลลัพธ์ จากตัวแปรข้างบน
    print(f"ค่าใช้จ่าย (expenses): {expenses:.2f} บาท")
    print(f"เงินลงทุน (investment): {investment:.2f} บาท")
    print(f"ซื้อของให้ตัวเอง (give yourself a gift): {youself:.2f} บาท")
    print(f"เงินที่ใช้ไม่ได้ (unusable money): {unusable_money:.2f} บาท")
    print(f"เงินที่เหลือสำหรับใช้ได้ (remaining_money): {balance:.2f} บาท")
    
    another_round = input("ต้องการคำนวณเพิ่มเติมหรือไม่? (y/n): ")
    if another_round.lower() != 'y':
        print("ขอบคุณที่ใช้บริการครับ ลาก่อย")
        break