geo = input("Геометрийн төрлийг оруулна уу (square, rectangle, circle, triangle): ")

if geo == "square":
    a1 = int(input("Хажуугийн урт оруулна уу: "))
    print(f"Талбай: {a1 * a1}")
elif geo == "rectangle":
    a1 = int(input("Урт оруулна уу: "))
    a2 = int(input("Өргөн оруулна уу: "))
    print(f"Талбай: {a1 * a2}")
elif geo == "circle":
    radius = int(input("Дугуйны радиус оруулна уу: "))
    print(f"Талбай: {3.14 * radius * radius}")
elif geo == "triangle":
    base = int(input("Үндсэн талыг оруулна уу: "))
    height = int(input("Өндрийг оруулна уу: "))
    print(f"Талбай: {0.5 * base * height}")
else:
    print("Таны оруулсан геометрийн төрөл буруу байна.")
