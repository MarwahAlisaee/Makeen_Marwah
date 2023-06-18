username = input("input the name ")

unique_chars = set(username)  # الأحرف الغير مكررة في اسم المستخدم

if len(unique_chars) % 2 == 0:
    print("she is girl")
else:
    print("hi is boy")


