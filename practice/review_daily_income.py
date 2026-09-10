hour_text = input("通勤時間 (0-23): ")

if hour_text.isdigit():
    hour = int(hour_text)
    hour_rate_text = input("時給 (円): ")
    if hour_rate_text.isdigit():
        hour_rate = float(hour_rate_text)
        daily_income = hour * hour_rate
        print(f"1日の収入は {daily_income} 円です。")
    else:
        print("時給は数値で入力してください。")
        exit()
else:
    print("通勤時間は0から23の整数で入力してください。")
    exit()

