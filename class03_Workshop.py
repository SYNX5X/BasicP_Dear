monster = 200
weapon1 = 50
weapon2 = 30
weapon3 = 100

start = True
while start :
    print("เส้นทางเเห่งความมันส์ของคิริตู่")
    print("Kill Monster")
    print("Go Home and Sleep")
    g = int(input("เลือกเส้นทางเเห่งความมันส์"))
    if g == 1 :
        k = int(input("คุณจะจัดการมอนเตอร์นี้กี่รอบ"))
        for i in range(k):
            print("กรุณาเลือกอาวุธที่ใช้ในการโจมตี")
            print(weapon1 )
            print(weapon2)
            print(weapon3)
            print("Hp monster = ",monster)
            print("เหลือโอกาศตีอยู่:",k - i)
            w = int(input("เลือกอาวุธเอาชิ้นไหน"))
            print("คุณเลือกอาวุธ", w)
            if (w == 1) :
                print("คุณตีไป 50 หน่วย")
                monster -= weapon1
                print("จำนวนเหลืดที่เหลือ",monster, "Hp")
                if (monster < 0):
                    print("ตีเเรกเกินนไปเว้ยย เเม่งมีสกิลเด้งเลือด 20 หน่วย")
                    monster = 20
            elif w == 2 :
                print("คุณตีไป 30 หน่วย")
                monster -= weapon2
                print("จำนวนเหลืดที่เหลือ",monster, "Hp")
                if (monster < 0):
                    print("ตีเเรกเกินนไปเว้ยย เเม่งมีสกิลเด้งเลือด 20 หน่วย")
                    monster = 20
            elif w == 3 :
                print("คุณตีไป 100 หน่วย")
                monster -= weapon3
                print("จำนวนเหลืดที่เหลือ",monster, "Hp")
                if (monster < 0):
                    print("ตีเเรกเกินนไปเว้ยย เเม่งมีสกิลเด้งเลือด 20 หน่วย")
                    monster = 20
            elif monster == 0 :
                print("monster is dead hp 0")
                break
        if (monster > 0):
            print("หมดโอกาศแล้ว")
            print("mon ไม่ตาย = มึงตาย")
            start = False
        else:
            print("มอนตายเครียเกมได้เเเล้วกลับบ้านได้")
            start = False
    else:
        print("กลับบ้านนอนปลอดภัย")
        break