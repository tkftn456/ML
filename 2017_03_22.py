import tensorflow as tf
import os
import numpy as np
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

w_test = 5
b_test = 2
size = 10

x_data = []
y_data = []



for a in range(0,size,1):
    y = a * w_test + b_test
    x_data.append(np.float32(a))
    y_data.append(np.float32(y))

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = X * W + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())


for step in range(2001):
    cost_val , _ = sess.run([cost,train],feed_dict={X: x_data, Y: y_data})



#print(cost_val)
#print(sess.run(hypothesis,feed_dict={X: 30.}))
plt.plot(30,sess.run(hypothesis,feed_dict={X: 30.}),'bs',label = 'cost = %s' % cost_val)


X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = X * W + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.005)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())


for step in range(2001):
    cost_val , _ = sess.run([cost,train],feed_dict={X: x_data, Y: y_data})



#print(cost_val)
#print(sess.run(hypothesis,feed_dict={X: 30.}))
plt.plot(30,sess.run(hypothesis,feed_dict={X: 30.}),'g^',label = 'cost = %s' % cost_val)


plt.plot(30,30. * w_test + b_test,'ro',label = 'origin')

plt.legend()
plt.show()