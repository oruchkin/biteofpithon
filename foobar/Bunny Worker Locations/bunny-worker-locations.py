def solution(x, y):

    # fining x with y==1 (x,1)
    x_number = 0
    for i in range(1, x+1):
        x_number += i

    # finding id accoridng to y
    y_number = 0
    for i in range(1, y):
        y_number += (x-1) + i
    y_number += x_number

    return str(y_number)
