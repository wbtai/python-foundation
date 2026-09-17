# Task 1: Nhận và làm sạch dữ liệu
name = input("Name : ").strip()
total = float(input("Total: ").strip())
people = int(input("People: ").strip())

# Task 2: Tính số tiền mỗi người
if total < 0 or people <= 0:
    print("Error: Total must be greater than or equal to 0 and people must be greater than 0.")
else:
    per_person = total / people

# Task 3: Hiển thị kết quả
print(type(name))
print(type(total))
print(type(people))
print(f"Name: {name}")
print(f"Mỗi người: ¥{per_person:.2f}")