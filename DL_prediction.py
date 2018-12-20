# coding = 'utf-8'
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler


def loadData():
    data = pd.read_csv('train_data_Zk5902.csv', header=None, encoding='utf-8')
    train_x = data.ix[:, [0]]
    train_y = data.ix[:, 1:13]

    return train_x, train_y


# Parameters
learning_rate = 0.001
training_epochs = 500
batch_size = 256
display_step = 10
examples_to_show = 10

# Network Parameters
n_input = 1
n_output = 12

# tf Graph input (only pictures)
X = tf.placeholder("float", (None, n_input))
Y = tf.placeholder("float", (None, n_output))

# hidden layer settings
n_hidden_1 = 12  # 1st layer num features
n_hidden_2 = 12  # 2nd layer num features
n_hidden_3 = 12  # 2nd layer num features
n_hidden_4 = 12  # 2nd layer num features

# n_hidden_2 = 128  # 2nd layer num features
weights = {
    'encoder_h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'encoder_h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
    'encoder_h4': tf.Variable(tf.random_normal([n_hidden_3, n_hidden_4])),
    'encoder_h5': tf.Variable(tf.random_normal([n_hidden_4, n_output])),
}
biases = {
    'encoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'encoder_b3': tf.Variable(tf.random_normal([n_hidden_3])),
    'encoder_b4': tf.Variable(tf.random_normal([n_hidden_4])),
    'encoder_b5': tf.Variable(tf.random_normal([n_output])),
}


# Building the encoder
def encoder(x):
    # Encoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']), biases['encoder_b1']))
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']), biases['encoder_b2']))
    layer_3 = tf.nn.sigmoid(tf.add(tf.matmul(layer_2, weights['encoder_h3']), biases['encoder_b3']))
    layer_4 = tf.nn.sigmoid(tf.add(tf.matmul(layer_3, weights['encoder_h4']), biases['encoder_b4']))
    layer_5 = tf.add(tf.matmul(layer_4, weights['encoder_h5']), biases['encoder_b5'])
    return layer_5


# Construct model
y_pred = encoder(X)
# Targets (Labels) are the input data.
y_true = Y

# Define loss and optimizer, minimize the squared error
cost = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    x_data, y_data = loadData()
    X_train, X_test, Y_train, Y_test = train_test_split(x_data, y_data, test_size=0.33, random_state=0)

    # sc = StandardScaler()
    # sc.fit(X_train)
    # X_train_std = sc.transform(X_train)
    # X_test_std = sc.transform(X_test)

    for epoch in range(training_epochs):
        _, c = sess.run([optimizer, cost], feed_dict={X: X_train, Y: Y_train})
        # if epoch % display_step == 0:
        #     print("Epoch:", '%04d' % (epoch + 1), "cost=", "{:.9f}".format(c))

    y = sess.run(y_pred, feed_dict={X: X_test})

    # for i in range(len(y)):
    #     for j in range(len(y[i])):
    #         if y[i][j] > 0.85:
    #             y[i][j] = 1
    #         else:
    #             y[i][j] = 0

    for i in range(len(X_test)):
        print(np.array(X_test)[i], y[i])
    # print(X_test, y)

    # l = sess.run(cost, feed_dict={X: X_test, Y: Y_test})

