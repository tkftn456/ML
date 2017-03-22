import tensorflow as tf
import os
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

w_test = 5
b_test = 2
size = 10
step_list = [3,5,10,20,30,40,50,60,70,80,90,100,200,300]

x_train = []
y_train = []

print("step -- cost ")

for step in step_list:
    for a in range(0,size,1):
        y = a * w_test + b_test
        x_train.append(a)
        y_train.append(y)




    W = tf.Variable(tf.random_normal([1]), name='weight')
    b = tf.Variable(tf.random_normal([1]), name='bias')

    hypothesis = x_train * W + b

    cost = tf.reduce_mean(tf.square(hypothesis - y_train))

    optimizer = tf.train.GradientDescentOptimizer(learning_rate= 0.0001)
    train = optimizer.minimize(cost)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for s in range(step):
        sess.run(train)

    X = []
    Y = []

    print("%s -- %s " %(step,sess.run(cost)))
    for a in range(0,size,1):
        y = a * sess.run(W) + sess.run(b)
        X.append(a)
        Y.append(y)

    plt.plot(X, Y,label = step)

plt.plot(x_train, y_train,label = 'origin')
plt.legend()
plt.show()