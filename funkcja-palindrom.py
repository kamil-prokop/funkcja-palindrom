def palindrom(arg_1 = "palindrom"):
    middle_letter = len(arg_1) // 2

    counting = 0
    for i in range(0, int(middle_letter)):
        if arg_1[i] == arg_1[len(arg_1) - 1 - i]:
            counting +=1

palindrom()