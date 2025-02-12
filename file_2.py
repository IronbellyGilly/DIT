def determine_quadrant(x, y):
    if x > 0 and y > 0:
        print("I")  
    elif x < 0 and y > 0:
        print("II")
    elif x < 0 and y < 0:
        print("III")  
    elif x > 0 and y < 0:
        print("IV")  
    else:
        print("Точка находится на оси координат или в начале координат.")


determine_quadrant(3, 4)  
determine_quadrant(-2, 5) 
determine_quadrant(-3, -1)  
determine_quadrant(4, -2)  
determine_quadrant(0, 0)

# def ask_password():
#     correct_password = "password"
#     for attempt in range(3):
#         user_input = input("Введите пароль: ")
#         if user_input == correct_password:
#             print("Пароль принят")
#             return 
#         else:
#             print("Неверный пароль. Попробуйте еще раз.")
#     print("Вы исчерпали все попытки.")

# ask_password()

### test