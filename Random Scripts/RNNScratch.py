#Series prediction in RNN
#Given a sequence of 50 numbers belonging to a sine wave, predict the 51st number in the series. 
#-----------------------
#Import libraries 
import math
import matplotlib as mtl
from matplotlib import pyplot as plt
import numpy as np
#------------------------
#Sigmoid/Activation function
def sigmoid(x): #This is what separates learning algorithm from curve fitting
    return 1/(1+np.exp(-x))
#-------------------------
#Calculate Loss
#Forward pass through RNN model and calculate the squared error for the predictions to get the loss value.
def calculate_loss(X, Y, U, V, W):
    loss = 0.0
    for i in range(Y.shape[0]):
        x, y = X[i], Y[i]
        prev_activation = np.zeros((hidden_dim, 1)) # value of previous activation(initialize at 0)
        for timestep in range(seq_len):
            #Tokenizer-ish:Weight Matrix with all values other than current one 0
            new_input = np.zeros(x.shape)       # forward pass, done for each step in the sequence
            new_input[timestep] = x[timestep]   # define a single input for that timestep
            mulu = np.dot(U, new_input)         # dot product
            mulw = np.dot(W, prev_activation)
            _sum = mulu + mulw
            activation = sigmoid(_sum)
            mulv = np.dot(V, activation)
            prev_activation = activation
        # calculate and add loss per record
        loss_per_record = float((y - mulv)**2/2) 
        loss += loss_per_record #Sum Square Loss
    return loss, activation

# takes x values and the weights matrices
# returns layer dictionary, final weights (mulu, mulw, mulv)
def calc_layers(x, U, V, W, prev_activation):
    layers = []
    #Tokenizer-ish:Weight Matrix with all values other than current one 0
    for timestep in range(seq_len):
        new_input = np.zeros(x.shape)
        new_input[timestep] = x[timestep]
        #multiply the input with the weights between input and hidden layers
        mulu = np.dot(U, new_input)
        #multiplication of weights in the RNN layer
        mulw = np.dot(W, prev_activation)
        #add to get knowledge of previous timestamps
        _sum = mulw + mulu
        #Pass it through a sigmoid activation function
        activation = sigmoid(_sum)
        #At the output layer, we have a linear activation of the values 
        mulv = np.dot(V, activation)
        #Save the state at the current layer and also the state at the previous timestep
        layers.append({'activation': activation, 'prev_activation': prev_activation})
        prev_activation = activation

    return layers, mulu, mulw, mulv

#calculate the differential for the previous activation of the hidden layer
#3 ips : Sum of weight ops, op layer differential and weights layer
def get_previous_activation_differential(_sum, ds, W): 
        #Differential of the sum
        d_sum = _sum * (1 - _sum) * ds          
        #Differential of the hidden layer output 
        dmulw = d_sum * np.ones_like(ds)        #matrix in the shape of ds
        return np.dot(np.transpose(W), dmulw)   

#After the forward propagation step, we calculate the gradients at each layer, and backpropagate the errors.
#Truncated BPTT since normal/vanilla BPTT is computation heavy
#--------Important  
# The dot product is taken on transpose of weight matrices(Dimensional issues) 
def backprop(x, U, V, W, dmulv, mulu, mulw, layers):
    #Weight differentials
    dU = np.zeros(U.shape)
    dV = np.zeros(V.shape)
    dW = np.zeros(W.shape)
    #Differential at given timestamp
    dU_t = np.zeros(U.shape)
    dV_t = np.zeros(V.shape)
    dW_t = np.zeros(W.shape)
    #Differential for bppt
    dU_i = np.zeros(U.shape)
    dW_i = np.zeros(W.shape)
    
    _sum = mulu + mulw
    dsv = np.dot(np.transpose(V), dmulv)
    
    #For each timestep in the sequence length, 
    # Get the differential of the last layer in that time step by multiplying the last layer differential by the last layer activation. 
    # Then set up the differential of the last layer as the dsv value we assigned in the set up.
    for timestep in range(seq_len):
        dV_t = np.dot(dmulv, np.transpose(layers[timestep]['activation']))
        ds = dsv
        dprev_activation = get_previous_activation_differential(_sum, ds, W)
        # Create the differential for recurrent timestep as dot product of the hidden weights and the timestep’s previous activation. 
        for _ in range(timestep-1, max(-1, timestep-bptt_truncate-1), -1):
            ds = dsv + dprev_activation
            dprev_activation = get_previous_activation_differential(_sum, ds, W)
            dW_i = np.dot(W, layers[timestep]['prev_activation'])
            #get differential ...same as forward pass
            new_input = np.zeros(x.shape)
            new_input[timestep] = x[timestep]
            dU_i = np.dot(U, new_input)
            #Update
            dU_t += dU_i
            dW_t += dW_i
        #update   
        dU += dU_t
        dV += dV_t
        dW += dW_t
        
        # take care of possible exploding gradients
        if dU.max() > max_clip_val:
            dU[dU > max_clip_val] = max_clip_val
        if dV.max() > max_clip_val:
            dV[dV > max_clip_val] = max_clip_val
        if dW.max() > max_clip_val:
            dW[dW > max_clip_val] = max_clip_val
        
        if dU.min() < min_clip_val:
            dU[dU < min_clip_val] = min_clip_val
        if dV.min() < min_clip_val:
            dV[dV < min_clip_val] = min_clip_val
        if dW.min() < min_clip_val:
            dW[dW < min_clip_val] = min_clip_val
        
    return dU, dV, dW
#-------------------------------------
# Train Model
def train(U, V, W, X, Y, X_validation, Y_validation):
    for epoch in range(max_epochs):
        # calculate initial loss, ie what the output is given a random set of weights
        loss, prev_activation = calculate_loss(X, Y, U, V, W)

        # check initial validation loss
        val_loss, _ = calculate_loss(X_validation, Y_validation, U, V, W)

        # train model/forward pass
        for i in range(Y.shape[0]):
            x, y = X[i], Y[i]
            layers = []
            prev_activation = np.zeros((hidden_dim, 1))
            
            layers, mulu, mulw, mulv = calc_layers(x, U, V, W, prev_activation)
                
            # difference of the prediction
            dmulv = mulv - y
            dU, dV, dW = backprop(x, U, V, W, dmulv, mulu, mulw, layers)
            
            # update weights
            U -= learning_rate * dU
            V -= learning_rate * dV
            W -= learning_rate * dW
            
    return U, V, W

if __name__=="__main__":
    #---------------------------------------------
    #Step 1: RNN Architecture
    learning_rate = 0.0001    #Learning Rate
    seq_len = 50            #Sequence length
    max_epochs = 25         #Predefined max number of epoch to avoid overfitting
    hidden_dim = 100        #100 hidden layers
    output_dim = 1          #1 output layer
    bptt_truncate = 5       # backprop through time --> lasts 5 iterations
    min_clip_val = -10      #clip values to avoid exploding gradient
    max_clip_val = 10
    #---------------------------------------------
    #Step 2: Create Data
    sin_wave = np.array([math.sin(x) for x in range(200)])
    #Training Data
    X = []
    Y = []
    num_records = len(sin_wave) - seq_len # 150

    # X entries are 50 data points
    # Y entries are the 51st data point
    for i in range(num_records-50): #-50 because 50 are used in validating
        X.append(sin_wave[i:i+seq_len])
        Y.append(sin_wave[i+seq_len])

    X = np.expand_dims(np.array(X), axis=2) # 100 x 50 x 1 (100 data,50 in seq,1 seqtype)
    Y = np.expand_dims(np.array(Y), axis=1) # 100 x 1       (100 data, 1 seqtype)

    # Validation data
    X_validation = []
    Y_validation = []
    # X entries are 50 data points
    # Y entries are the 51st data point
    for i in range(num_records-seq_len, num_records):
        X_validation.append(sin_wave[i:i+seq_len])
        Y_validation.append(sin_wave[i+seq_len])

    X_validation = np.expand_dims(np.array(X_validation), axis=2)# 100 x 50 x 1 (100 data,50 in seq,1 seqtype)
    Y_validation = np.expand_dims(np.array(Y_validation), axis=1)# 100 x 1       (100 data, 1 in seq)

    #Randomize weights
    np.random.seed(12161)                                   #reseed peudorandom function
    U = np.random.uniform(0, 1, (hidden_dim, seq_len))      # weights from input to hidden layer
    V = np.random.uniform(0, 1, (output_dim, hidden_dim))   # weights from hidden to output layer
    W = np.random.uniform(0, 1, (hidden_dim, hidden_dim))   # recurrent weights for layer (RNN weigts)
    #---------------------------------
    
    #Train model
    U, V, W = train(U, V, W, X, Y, X_validation, Y_validation)
    
    # predictions on the training set
    predictions = []
    for i in range(Y.shape[0]):
        x, y = X[i], Y[i]
        prev_activation = np.zeros((hidden_dim,1))
        # forward pass
        for timestep in range(seq_len):
            mulu = np.dot(U, x)
            mulw = np.dot(W, prev_activation)
            _sum = mulu + mulw
            activation = sigmoid(_sum)
            mulv = np.dot(V, activation)
            prev_activation = activation
        predictions.append(mulv)

    predictions = np.array(predictions)

    plt.plot(predictions[:, 0,0], 'g')
    plt.plot(Y[:, 0], 'r')
    plt.title("Training Data Predictions in Green, Actual in Red")
    plt.show()

    # predictions on the validation set
    val_predictions = []
    for i in range(Y_validation.shape[0]):
        x, y = X[i], Y[i]
        prev_activation = np.zeros((hidden_dim,1))
        # forward pass
        for timestep in range(seq_len):
            mulu = np.dot(U, x)
            mulw = np.dot(W, prev_activation)
            _sum = mulu + mulw
            activation = sigmoid(_sum)
            mulv = np.dot(V, activation)
            prev_activation = activation
        val_predictions.append(mulv)

    val_predictions = np.array(val_predictions)

    plt.plot(val_predictions[:, 0,0], 'g')
    plt.plot(Y_validation[:, 0], 'r')
    plt.title("Test Data Predictions in Green, Actual Data in Red")
    plt.show()
