print("Zismail Program")
print("")

amount = float(input("ป้อนจำนวนเงินที่ต้องการออม: "))
percent = int(input("เลือกเปอร์เซ็นต์ที่ต้องการออม (50, 30, 20, หรือ 10): "))

if percent in [50, 30, 20, 10]:
    savings = (amount * percent) / 100
    print(f"คุณจะออมได้ {savings:.2f}")
else:
    print("เปอร์เซ็นต์ไม่ถูกต้อง โปรดเลือก 50, 30, 20, หรือ 10.")
