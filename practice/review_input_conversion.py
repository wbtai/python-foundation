name = input("ten cua ban: ").strip()


if name == "":
    print("Ban chua nhap ten")
else:
    study_hours_text = input("so gio hoc: ").strip()
    if study_hours_text == "":
        print("Ban chua nhap so gio hoc")
    else:
        study_hours = float(study_hours_text)
        if study_hours < 0:
            print("so gio hoc khong hop le")
        else:
            print(f"{name} da hoc {study_hours} gio")