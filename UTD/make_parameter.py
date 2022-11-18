import numpy as np
from datetime import datetime



def string_check(x):
    assert type(x) is str, "문자열 형식이 아닙니다. 적요 텍스트의 타입을 확인해주세요. {}".format(x)

def integer_check(x):
    assert type(x) is int, "정수가 아닙니다. 적요 텍스트의 타입을 확인해주세요. {}".format(x)

def make_trantmrg(dt, net_code):
    string_check(dt)
    integer_check(net_code)

    if net_code in ["3", "4"]:
        return 99

    hour = int(datetime.strptime(dt, '%Y-%m-%d %H:%M:%S').hour)
    if hour in range(0, 6):
        return 3
    elif hour in range(6, 9):
        return 6
    elif hour in range(9, 12):
        return 9
    elif hour in range(12, 15):
        return 12
    elif hour in range(15, 18):
        return 15
    elif hour in range(18, 21):
        return 18
    elif hour in range(21, 24):
        return 21

def make_tranweekday(dt):
    string_check(dt)
    weekday = int(datetime.strptime(dt, '%Y-%m-%d %H:%M:%S').weekday())
    if weekday == 6:
        return 5
    return weekday

def make_attime(dt, net_code):
    string_check(dt)
    integer_check(net_code)

    if net_code in ["3", "4"]:
        return 99

    hour = int(datetime.strptime(dt, '%Y-%m-%d %H:%M:%S').hour)
    if hour in range(0, 6):
        return 0
    elif hour in range(6, 12):
        return 1
    elif hour in range(12, 18):
        return 2
    elif hour in range(18, 24):
        return 3

def preprocess_amt(amt):
    integer_check(amt)
    return np.log10(int(amt))
