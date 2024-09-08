import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        calculations = {}
        arr = np.array(list).reshape(3,3)
        mean_list = [np.mean(arr, axis = 0).tolist(), np.mean(arr, axis = 1).tolist(), np.mean(arr).tolist()]
        calculations['mean'] = mean_list
        var_list = [np.var(arr, axis = 0).tolist(), np.var(arr, axis = 1).tolist(), np.var(arr).tolist()]
        calculations['variance'] = var_list
        std_list = [np.std(arr, axis = 0).tolist(), np.std(arr, axis = 1).tolist(), np.std(arr).tolist()]
        calculations['standard deviation'] = std_list
        max_list = [np.max(arr, axis = 0).tolist(), np.max(arr, axis = 1).tolist(), np.max(arr).tolist()]
        calculations['max'] = max_list
        min_list = [np.min(arr, axis = 0).tolist(), np.min(arr, axis = 1).tolist(), np.min(arr).tolist()]
        calculations['min'] = min_list
        sum_list = [np.sum(arr, axis = 0).tolist(), np.sum(arr, axis = 1).tolist(), np.sum(arr).tolist()]
        calculations['sum'] = sum_list
        return calculations

