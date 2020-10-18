def add_digit(number):
    my_sum = 0
    for digit in number:
        my_sum += int(digit)
    if len(str(my_sum)) == 1:
      return my_sum
    else:
      return add_digit(str(my_sum))


def cal_answer(number):
    temp = one_counter = two_counter = 0
    one_list = []
    two_list = []
    for num in range(int(number) + 1):
        temp = add_digit(str(num))

        if temp == 1:
            one_counter += 1
            one_list.append(num)
        elif temp == 2:
            two_counter += 1
            two_list.append(num)
    return (one_counter, two_counter,one_list, two_list)

def compare(one, two):
    if one > two:
        return "one > two"
    elif one < two:
        return "tow > one"
    else:
        return "equal"


user_input = (input("enter a number: "))
ans = cal_answer(user_input)
print("ONE:",ans[2])
print("TWO:",ans[3])
print(compare(ans[0], ans[1]))