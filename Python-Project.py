while True:
    print("Zismail Dev Programming")
    print("")
    print("1. หาพื้นที่ 4 เหลี่ยม")
    print("2. หาพื้นที่ 3 เหลี่ยม")
    print("3. หาพื้นที่วงกลม")
    print("4. คำนวณค่าไฟ")
    print("5. คำนวณเกรด")
    print("")

    zis = int(input("Select Your Want: "))

    if zis == 1:
        while True:
            print("คุณได้เลือกโปรแกรมคำนวณหาพื้นที่ 4 เหลี่ยม")
            print("")
            print("1. หาพื้นที่สี่เหลี่ยมจตุรัส")
            print("2. หาพื้นที่สี่เหลี่ยมผืนผ้า")
            print("3. หาพื้นที่สี่เหลี่ยมด้านขนาน")
            print("4. หาพื้นที่สี่เหลี่ยมขนมเปียกปูน")
            print("0. ย้อนกลับไปที่เมนูหลัก")
            print("")
            squares = int(input("Enter Your Squares Want: "))

            if squares == 1:
                print("Your select หาพื้นที่สี่เหลี่ยมจตุรัส")
                side1 = int(input("Enter Your Side1: "))
                side2 = int(input("Enter Your Side2: "))

                resultarea1 = side1 * side2

                print(f"ปริมาตรสี่เหลี่ยมของคุณคือ : {resultarea1}")

            elif squares == 2:
                print("Your Select หาพื้นที่สี่เหลี่ยมผืนผ้า")
            elif squares == 3:
                print("ํYour Select หาพื้นที่สี่เหลี่ยมด้านขนาน")
            elif squares == 4:
                print("ํYour Select หาพื้นที่สี่เหลี่ยมขนมเปียกปูน")
            elif squares == 0:
                break  # ย้อนกลับไปที่เมนูหลัก
            else:
                print("ไม่อยู่ในตัวเลือก")

    elif zis == 2:
        print("คุณได้เลือกโปรแกรมคำนวณหาพื้นที่ 3 เหลี่ยม")

    elif zis == 3:
        print("คุณได้เลือกโปรแกรมคำนวณหาพื้นที่วงกลม")

    elif zis == 4:
        print("คุณได้เลือกโปรแกรมคำนวณค่าไฟ")
        watts = int(input("Enter Your Watts: "))
        hour = int(input("Enter Your Hour: "))
        day = int(input("Enter Your Day: "))
        unit = float(input("Enter Your Unit: "))

        varul = watts * hour / 1000 * unit
        result4 = varul * day

        print(f"ค่าไฟในการเปิดคอมของคุณคือ  : {result4}")

    elif zis == 5:
        print("คุณได้เลือกโปรแกรมคำนวณเกรด")

    else:
        print("ไม่อยู่ในตัวเลือก")

    restart = input("ต้องการทำงานใหม่หรือไม่? (y/n): ")
    if restart.lower() != "y":
        break
