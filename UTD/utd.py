__title__ = 'utd'
__version__ = '0.0.1'
__author__ = 'suchoi'
__license__ = ''
__copyright__ = 'Niccompany'

import os
import pickle
import numpy as np
installpath = os.path.dirname(os.path.realpath(__file__))


def numpy_check(x):
    assert type(x).__module__ == np.__name__, "array 형식이 아닙니다. 적요 텍스트의 타입을 확인해주세요. {}".format(x)

class UniqueTransactionDetect():
    def __init__(self):
        with open('%s/model/tranmodel_k24.pkl' % installpath, 'rb') as handle:
            self.model = pickle.load(handle)
        self.categorical = [0, 1, 2, 3, 4, 5, 6]

    def predict_result(self, x):
        numpy_check(x)
        x = x.reshape(8, 1).T
        result = str(self.model.predict(x, categorical=self.categorical)[0])
        return 'c'+result


