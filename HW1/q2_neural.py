
# coding: utf-8

# In[1]:

import numpy as np
import random
from q1_softmax import softmax
from q2_sigmoid import sigmoid, sigmoid_grad
from q2_gradcheck import gradcheck_naive


# In[2]:

def forward_backward_prop(data, labels, params, dimensions):
    """ 
    Forward and backward propagation for a two-layer sigmoidal network 
    
    Compute the forward propagation and for the cross entropy cost,
    and backward propagation for the gradients for all parameters.
    """

  ### Unpack network parameters (do not modify)
    ofs = 0
    Dx, H, Dy = (dimensions[0], dimensions[1], dimensions[2])

    W1 = np.reshape(params[ofs:ofs + Dx * H], (Dx, H))
    ofs += Dx * H
    b1 = np.reshape(params[ofs:ofs + H], (1, H))
    ofs += H
    W2 = np.reshape(params[ofs:ofs + H * Dy], (H, Dy))
    ofs += H * Dy
    b2 = np.reshape(params[ofs:ofs + Dy], (1, Dy))


    ### YOUR CODE HERE: forward propagation
    ## data(20 x 10), W1(10x5), W2(5 x 10)
    z1 = np.dot(data,W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1,W2) + b2
    a2 = softmax(z2)
    
    ## error of cross-entropy loss
    ## a2(20x10), labels(20x10)
    logs = -np.multiply(np.log(a2),labels)
    cost = np.sum(logs)
    ### END YOUR CODE
    
    ### YOUR CODE HERE: backward propagation
    ## delta3(20x10), delta2(20x5), W2(5x10)
    delta3 = (a2 - labels) 
    delta2 = np.multiply(sigmoid_grad(a1),np.dot(delta3,W2.T))
    
    ## a1(20x5)
    gradW1 = np.dot(data.T,delta2)
    gradW2 = np.dot(a1.T,delta3)
    
    gradb1 = np.sum(delta2, axis=0)
    gradb2 = np.sum(delta3, axis=0)
    ### END YOUR CODE
    
    ### Stack gradients (do not modify)
    grad = np.concatenate((gradW1.flatten(), gradb1.flatten(), gradW2.flatten(), gradb2.flatten()))

    return cost, grad

    
    


# In[3]:

def sanity_check():
    """
    Set up fake data and parameters for the neural network, and test using 
    gradcheck.
    """
    print "Running sanity check..."

    N = 20
    dimensions = [10, 5, 10]
    data = np.random.randn(N, dimensions[0])   # each row will be a datum
    labels = np.zeros((N, dimensions[2]))
    for i in xrange(N):
        labels[i,random.randint(0,dimensions[2]-1)] = 1
    
    params = np.random.randn((dimensions[0] + 1) * dimensions[1] + (dimensions[1] + 1) * dimensions[2], )

    gradcheck_naive(lambda params: forward_backward_prop(data, labels, params, dimensions), params)

def your_sanity_checks(): 
    """
    Use this space add any additional sanity checks by running:
        python q2_neural.py 
    This function will not be called by the autograder, nor will
    your additional tests be graded.
    """
    print "Running your sanity checks..."
    ### YOUR CODE HERE
    ### END YOUR CODE

if __name__ == "__main__":
    sanity_check()


# In[ ]:




# In[ ]:


