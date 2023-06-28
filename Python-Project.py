print("Zismail Dev Programing")
print("")
print("1 หาพื้นที่ 4 เหลี่ยม")
print("2 หาพื้นที่ 3 เหลี่ยม")
print("3 หาพื้นที่วงกลม")
print("4 คำนวนค่าไฟ")
print("5 คำนวนเกรด")
print("")

zis = int(input("Select Your Wont : "))

if zis == 1 :
    print("คุณได้เลือกโปรแกรมคำนวหาพื้นที่ 4 เหลี่ยม") 
    print("")
    print("1 หาพื้นที่สี่เหลี่ยจตุรัส")
    print("2 หาพื้นที่สี่เหลี่ยมผืนผ้า")
    print("3 หาพื้นที่สี่เหลี่ยมด้านขนาน")
    print("4 หาพื้นที่สี่เหลี่ยมขนมเปียกปูน")
    print("")
    squares = int(input("Enter Your Squares Want : "))

    if squares == 1 :
        print("Your select หาพื้นที่สี่เหลี่ยมจตุรัส")
        side1 = int(input("Enter Your Side1 : "))
        side2 = int(input("Enter Your Side2 : "))

        resultarea1 = side1 * side2

        print(resultarea1)

    elif squares == 2 :
        print("Your Select หาพื้นที่สี่เหลี่ยมผืนผ้า")
    elif squares == 3 :
        print("ํYour Select หาพื้นที่สี่เหลี่ยมด้านขนาน")
    elif squares == 4 :
        print("ํYour Select หาพื้นที่สี่เหลี่ยมขนมเปียกปูน")
    else :
        print("ไม่อยู่ในตัวเลือก")
elif zis == 2 :
    print("คุณได้เลือกโปรแกรมคำนวหาพื้นที่ 3 เหลี่ยม")
elif zis == 3 :
    print("คุณได้เลือกโปรแกรมคำนวหาพื้นที่วงกลม")
elif zis == 4 :
    print("คุณได้เลือกโปรแกรมคำนวค่าไฟ")
    watts = int(input("Enter Your Watts : "))
    hour = int(input("Enter Your Hour : "))
    day = int(input("Enter Your Day : "))
    unit = int(input("Enter Your Unit : "))

    varul = watts * hour /1000 * unit
    result4 = varul * day

    print(result4)
elif zis == 5 :
    print("คุณได้เลือกโปรแกรมคำนวนเกรด")
else :
    print("ไม่อยู่ในตัวเลือก")