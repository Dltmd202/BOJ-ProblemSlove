for i in range(int(input())):
    q = input()
    arr_len = int(input())
    if (arr_len == 0):
        input_arr = input()
        input_arr = []
    else:
        input_arr = list(map(int, input()[1:-1].split(',')))
    is_reverse = False
    is_ok = True
    front = 0
    rear = 0

    for act in q:
        try:
            if (act == 'R'):
                is_reverse = not is_reverse
            elif (act == 'D' and not is_reverse):
                front += 1
            elif (act == 'D' and is_reverse):
                rear += 1
        except:
            is_ok = False
            print('error')
            break

    if (is_ok):
        if (front + rear <= arr_len):
            if (not is_reverse):
                input_arr = input_arr[front:arr_len - rear]
                print(str(input_arr).replace(' ', ''))
            else:
                input_arr = input_arr[::-1][rear:arr_len - front]
                print(str(input_arr).replace(' ', ''))
        else:
            print('error')