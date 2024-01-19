# coding=utf-8
import sys
print(sys.path)

import tensorflow as tf
from tensorflow.keras.layers import Layer

inputs = tf.constant([[[1., 2., 4., 6.]], \
                      [[2., 10, 0.1, 0.4]], \
                      [[14., 0, -0.5, 0.4]]], dtype=tf.float32)

alphas = tf.constant([0.5, 0.1, 1., 2.], dtype=tf.float32)


# Batch Normalization
inputs_normed = tf.keras.layers.BatchNormalization(axis=-1, epsilon=1e-9, center=False, scale=False)\
    (inputs, training=True)

print(inputs_normed)
print("\n")


# Dice value
x_p = tf.sigmoid(inputs_normed)
result = alphas * (1.0 - x_p) * inputs + x_p * inputs
print(result)