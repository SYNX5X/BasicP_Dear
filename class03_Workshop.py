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
            print("weapon1 = 50","กดเลข 1")
            print("weapon2 = 30","กดเลข 2")
            print("weapon3 = 100","กดเลข 3")
            print("monsterhp = ",monster)
            print("จำนวนครั้งที่เหลือ ",k - i )
        w = int(input("เลือกอาวุธเอาชิ้นไหน"))
        print("คุณเลือกอาวุธ", w)
        if (w == 1) :
            w1 = 200-50
            print(w1)
        
       


    





    else :
        print("กลับบ้านดีกว่า")
        break