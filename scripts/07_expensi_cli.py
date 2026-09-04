category = input("Loai: ").strip().lower()

amount_text = input("So tien: ").strip()


if category == "":
    print("Category khong duoc de trong")
else:
    if amount_text == "":
        print("Amount_text khong duoc de trong")
    else:
        try:
            amount = float(amount_text)
            if amount <=0 :
                print("Amount phai lon hon 0")
            else:
                print(f"Da ghi:food - {amount} yen ")
                print(f"Sau giam 10%: {amount-amount*0.1} yen")
        except ValueError:
            print("Amount phai la 1 so, vi du 500 hoac 500.5")
