import sys, os
from os import chdir
chdir('D:\\git\\python\\basic_deep')
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from dataset.mnist import load_mnist
import comm_func
from PIL import Image


#def identify_fun(x):
#    return x
#
#X = np.array([1.0, 2.0])
#W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.1, 0.4]])
#B1 = np.array([0.2, 0.1, 0.3])
#
#A1 = np.dot(X, W1) + B1
#Z1 = sigmoid(A1)
#
#W2 = np.array([[0.1, 0.3], [0.2, 0.1], [0.3, 0.1]])
#B2 = np.array([0.2, 0.1])
#
#A2 = np.dot(Z1, W2) + B2
#Z2 = sigmoid(A2)
#
#W3 = np.array([[0.2, 0.3], [0.1, 0.2]])
#B3 = np.array([0.1, 0.2])
#
#A3 = np.dot(Z2, W3) + B3
#Y = identify_fun(A3)
#
#print(Y)

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

#    print ('W1', W1.shape)
#    print ('W2', W2.shape)
#    print ('W3', W3.shape)
#    print ('b1', b1.shape)
#    print ('b2', b2.shape)
#    print ('b3', b3.shape)

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

#data =init_network()
#print(data)

x, t = get_data()
print(x.shape, t.shape)
network = init_network()

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis = 1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))