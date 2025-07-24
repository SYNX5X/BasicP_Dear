def hello (name): 
    print(name)

name = input("ค่าที่รับ",)
hello(name)


# def sum(a , b):
#     result = a + b 
#     print("ผลรวม: ", result)
#     return result
# num1=int(input("กรอกตัวเลข",))
# num2=int(input("กรอกตัวเลข",))
# result = sum(num1,num2)
# print(result)


# def add(num1,num2):
#     result  = num1+num2
#     return result
# def minus(num1,num2):
#     result  = num1-num2
#     return result
# def mutiple(num1,num2):
#     result  = num1*num2
#     return result
# def divide(num1,num2):
#     result  = num1//num2
#     return result
# def is_even(num):
#     result = num%2 
#     if result == 0 :
#         return "is_even"
#     else : 
#         return "is odd"
# def main():
#     num1 = int(input("กรอกตัวเลขตัวที่ 1",))
#     num2 = int(input("กรอกตัวเลขตัวที่ 2",))
#     print("+ - * / กดเลือกสัญลักษณ์" )
#     print(" 1 = +")
#     print(" 2 = -")
#     print(" 3 = *")
#     print(" 4 = /")
#     op = int(input("กดตัวเลข:" ))
#     if(op == 1) :
#         result = add(num1,num2)
#         print("ผลบวกคือ ",result)
#     elif(op == 2) :
#         result =minus(num1,num2)
#         print("ผลต่างคือ ",result)
#     elif(op == 3) :
#         result =mutiple(num1,num2)
#         print("ผลคูณคือ ",result)
#     elif(op == 4) :
#         result =divide(num1,num2)
#         print("ผลหารคือ ",result)
#     print(is_even(result))
    
# main()