import numpy as np
# this function will return based on 3x3 array: mean, variance, standard deviation, max, min, and sum
def calculate(array_):
    if type(array_) == list:
        array_ = np.array(array_)
    try:
        array_ = array_.reshape(3,3)
        result = {
            "mean" : [array_.mean(axis=0), array_.mean(axis=1), array_.mean()],
            "variance" : [array_.var(axis=0), array_.var(axis=1), array_.var()],
            "standard deviation" : [array_.std(axis=0), array_.std(axis=1), array_.std()],
            "max" : [array_.max(axis=0), array_.max(axis=1), array_.min()],
            "min" : [array_.min(axis=0), array_.min(axis=1), array_.min()],
            "sum" : [array_.sum(axis=0), array_.sum(axis=1), array_.sum()]
        }
        return result
    except ValueError as e:
        print("ValueError",": List must contain 9 digits.")