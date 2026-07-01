text = "Hawnj pk swhg xabkna ukq nqj."
eng_lower = "abcdefghijklmnopqrstuvwxyz"
eng_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for shift in range(26):
    result_text = ""
    for symbol in text:
        if symbol in eng_lower:
            result_text += eng_lower[(eng_lower.find(symbol) + shift) % 26]
        elif symbol in eng_upper:
            result_text += eng_upper[(eng_upper.find(symbol) + shift) % 26]
        else:
            result_text += symbol
    print(f"Сдвиг {shift}: {result_text}")