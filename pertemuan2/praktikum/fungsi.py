def greeting(hour = 1):
    if hour < 12:
        return "Selamat Pagi!"
    elif hour < 18:
        return "Selamat Sore!"
    else:
        return "Selamat Malam!"

print(greeting())