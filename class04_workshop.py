# แสดงรายชื่อหนัง
def show_movies(movie_list):
    print(" รายชื่อหนัง:")
    for i in range(len(movie_list)):
        print(movie_list[i]['movie_name'] )

# ตรวจสอบอายุ
def check_age(user_age, age_restriction):
    if age_restriction== 'G':
        return True
    elif user_age >= int(age_restriction):
        return True
    else:
        return False

# คำนวณราคาตั๋ว
def calculate_price(price, cal):
    if cal == 'Romantic':
        return price + 50
    else:
        return price

# ซื้อตั๋วหนัง
def buy_ticket(movie_list):
    show_movies(movie_list)
    choice = int(input("เลือกหนัง (1-5): ")) - 1
    if choice >= 0 and choice < len(movie_list):
        movie = movie_list[choice]
        age = int(input("กรุณาใส่อายุของคุณ: "))

        if check_age(age, movie['age_restriction']):
            print("เลือกเสียง: 1 = พากย์ไทย, 2 = Soundtrack")
            sub = input("เลือกเสียง: ")

            if sub == '1':
                sound = "พากย์ไทย"
            elif sub == '2':
                sound = "Soundtrack"
            else:
                sound = "ไม่ระบุ"

            price = calculate_price(movie['ticket_price'], movie['cal'])

            print("ตั๋วหนังของคุณ")
            print("เรื่อง:", movie['movie_name'])
            print("เสียง:", sound)
            print("ราคาตั๋ว:", price, "บาท")
        else:
            print(" คุณอายุน้อยเกินไปสำหรับหนังเรื่องนี้")
    else:
        print(" เลือกหนังไม่ถูกต้อง")

# เมนูหลัก
def main():
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    print(" เมนู")
    print("1. แสดงหนังทั้งหมด")
    print("2. ซื้อตั๋วหนัง")

    menu = input("เลือกเมนู (1 หรือ 2): ")

    if menu == '1':
        show_movies(movies)
    elif menu == '2':
        buy_ticket(movies)
    else:
        print(" เมนูไม่ถูกต้อง")

# เรียกใช้งาน
main()
