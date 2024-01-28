#!/usr/bin/env python3
"""Layers for TensorFlow"""
import tensorflow as tf


def create_layer(prev, n, activation):
    """
    Creates a layer for a neural network.

    """
    # initializer
    initializer = tf.contrib.layers.variance_scaling_initializer(
        mode="FAN_AVG")

    # A layer with specific nodes
    layer = tf.layers.Dense(
        units=n,
        activation=activation,
        kernel_initializer=initializer,
        name='layer')

    # connectin a layer to the previous tensor
    output = layer(prev)

    return output
