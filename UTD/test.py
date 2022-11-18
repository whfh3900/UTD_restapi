# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from make_parameter import *
import numpy as np
from utd import UniqueTransactionDetect

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(make_trantmrg('2022-10-23 13:22:00', "1"))
    # print(make_tranweekday('2022-11-17 13:22:00'))
    # print(make_attime('2022-11-17 13:22:00', "1"))
    # print(preprocess_amt("456000"))

    #
    #
    #
    #
    #
    #
    #
    #
    test_data = [3, 1, 1, 1, 1, 3, 2, 4.0]
    test_data = np.array(test_data)

    utd_model = UniqueTransactionDetect()
    print(utd_model.predict_result(test_data))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
