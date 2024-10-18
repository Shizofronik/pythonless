#inizialization
import sys

#комментарий для проверки работы гита
<<<<<<< Updated upstream
=======
#bugFix
>>>>>>> Stashed changes

#main func
print("esc = выход(оператор) \n"
      "операции +, - \n"
      "1 строчка - 1 слагаемое")

print("Введите слагаемое:")
first = input()
print("Введите оператор:")
operator = input()
if operator == "esc":
    sys.exit("Завершено")

print("Введите слагаемое:")
second = input()

first_list = list(first)
second_list = list(second)
first_list = sorted(first_list)
second_list = sorted(second_list)
print(first_list)
print(second_list)

if operator == "+":
    first = "".join(first_list)
    second = "".join(second_list)
    result = first + second
    print(result)

elif operator == "-":
    for i in range(len(first_list)):
        for e in range(len(second_list)):
            if len(first_list) > 0 and len(second_list) > 0:
                if first_list[i] == second_list[e]:
                    first_list[i] = 0
                    second_list[e] = 0
                    break
            else:
                break
    while 0 in first_list:
        first_list.remove(0)
    while 0 in second_list:
        second_list.remove(0)
    if len(second_list) > 0 and len(first_list) > 0:
        print("".join(first_list), "-", "".join(second_list))
    elif len(second_list) == 0:
        print("".join(first_list))
    elif len(second_list) > 0 and len(first_list) == 0:
        print("-", "".join(second_list))