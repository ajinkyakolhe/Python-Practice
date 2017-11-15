import tensorflow as tf

a = tf.placeholder("float") # Create some variable
b = tf.placeholder("float") # Create second variable

y = tf.multiply(a,b) # Write an operation to be performed on these variables

# the with statement allows the execution of initialization and finalization code around a block of code.
with tf.Session() as sess:
    print("%f should equal 15" %sess.run(y, feed_dict={a:3,b:5}))

