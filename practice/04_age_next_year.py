age_text = input("Tuổi hiện tại của bạn: ").strip()

if age_text == "":
    print("Bạn chưa nhập tuổi.")
else:
    age = int(age_text)
    age_next_year = age + 1
    print(f"Năm sau bạn sẽ {age_next_year} tuổi.")