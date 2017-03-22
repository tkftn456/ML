import tensorflow as tf
import os
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

w_test = 5
b_test = 2
size = 50
rate_list = [0.01,0.001,0.0001,0.00001]

x_train = []
y_train = []

for a in range(0,size,1):
    y = a * w_test + b_test
    x_train.append(a)
    y_train.append(y)

for rate in rate_list:
    W = tf.Variable(tf.random_normal([1]), name='weight')
    b = tf.Variable(tf.random_normal([1]), name='bias')

    hypothesis = x_train * W + b

    cost = tf.reduce_mean(tf.square(hypothesis - y_train))

    optimizer = tf.train.GradientDescentOptimizer(learning_rate= rate)
    train = optimizer.minimize(cost)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    print('step\tcost\tW\tb')
    for step in range(1000):
        sess.run(train)
        if step % 100 == 0:
            print(step, sess.run(cost), sess.run(W), sess.run(b))

    X = []
    Y = []

    for a in range(0,size,1):
        y = a * sess.run(W) + sess.run(b)
        X.append(a)
        Y.append(y)


    plt.plot(X, Y,label = rate)

plt.plot(x_train, y_train,label = 'origin')
plt.legend()
plt.show()