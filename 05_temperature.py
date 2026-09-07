celsius_text = input("Nhiet do Celsius: ").strip()

if celsius_text == "":
    print("Ban chua nhap nhiet do")
else:
    celsius = float(celsius_text)
    fahrenheit = celsius*9/5 +32

    print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")