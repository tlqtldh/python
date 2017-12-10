import torch
from torch.autograd import Variable

x = [ 1.0, 5.0, 6.0]
y = [ 2.0, 4.0, 6.0]

w = Variable(torch.Tensor([1.0]), requires_grad=True)

# Build Model, construct computationl graph.

def forward(x):
    return x * w

# Define Loss Function

def loss(x,y):
    y_pred = forward(x)
    return (y_pred - y) * ( y_pred - y)

# Befor training
print("predict (before training)", 4, forward(4).data[0])

# Training
for epoch in range(10):
    for x_val , y_val in zip(x, y): # list up input data x and y together
        l = loss(x_val, y_val)
        l.backward()
        print("\tgrad: ", x_val, y_val, w.grad.data[0]) # print out only one weight value
        w.data = w.data - 0.01 * w.grad.data # update weights
        w.grad.data.zero_() # Manually zero the gradients after updating weights
    
    print ("Progress: " , epoch , l.data[0])

print("predict (after training)", 4, forward(4).data[0])

