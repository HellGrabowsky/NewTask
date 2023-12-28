new_array = input("Введите строки через запятую: ").split(", ")

result_array = []
for s in new_array:
    if len(s) <= 3:
        result_array.append(s)

print("Результат:", result_array)

# https://drive.google.com/file/d/11X_ytNPj1jOFXjJb0TaPLNCY95tpssFj/view?usp=sharing
