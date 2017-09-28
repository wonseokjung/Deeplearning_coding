import numpy as np
import tensorflow as tf

#session
sess=tf.Session()

#constant

x=tf.constant("hi")
print(sess.run(x))

b=tf.constant(1212)

sess.run(b)

print(sess.run(b))

add=tf.add(2,3)

add_check=sess.run(add)

print(add_check)

muli=tf.multiply(54,32)

mul_check=sess.run(muli)

print(mul_check)

#varible

v=tf.Variable(tf.random_normal([5,2],stddev=0.1))
init=tf.global_variables_initializer()

sess.run(init)
print(sess.run(v))


#place holder


place_holder=tf.placeholder(tf.float32, [None, 5])

print(place_holder)


def print_tf(x):
      out=sess.run(x)
      print(sess.run(out))

#operatin with variables and placeholders


operation=tf.matmul(place_holder,v)
print(operation)

