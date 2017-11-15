import tensorflow as tf
import numpy as np


# Create Numpy variables
x1 = np.linspace(-1,1,101)
y1 = 2*x1 + np.random.randn(*x1.shape) * 0.33

#Create TensorFlow variables
X = tf.placeholder("float")
Y = tf.placeholder("float")

#Create a model function
def model(X, w):
    return tf.multiply(X,w)


# Create a variable name
w = tf.Variable(0.0, name="weights")
y_model = model(X,w)
# Create a cost function
cost = tf.square(Y - y_model)

train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# Create the graph
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for i in range(100):
        for(x,y) in zip(x1,y1):
            sess.run(train_op, feed_dict={X:x, Y:y})
    print(sess.run(w))

