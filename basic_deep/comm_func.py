import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(data):
    el_max = np.max(data)
    exp_a = np.exp(data - el_max) # 오버 플로우 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# Mean Squared error (MSE)
def mean_squared_error(y, t):
    return 0.5 * np.sum((y -t)**2)

# Cross Entropy Error (CEE)
#def cross_entory_error(y, t):
#    delta = 1e-7
#    return -np.sum(t * np.log(y + delta))

def cross_entory_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y)) / batch_size

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) # generate same zero matrix with x

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 -fxh2) / (2*h)
        x[idx] = tmp_val
        
    return grad

