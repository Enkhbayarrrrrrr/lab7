
num1 = int(input())
num2 = int(input())
num3 = int(input())


total_seconds = num1 + num2 + num3


minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"{minutes}:{seconds:02d}")
