#!/usr/bin/env python3
"""TensorFlow Layers"""
import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Creates the forward propagation graph for the neural networks

    """
    # Ensure the number of layers and activations match
    assert len(layer_sizes) == len(
        activations), "Number of layers and activations must be the same"

    # input tensor
    prev = x

    for i in range(len(layer_sizes)):
        # created function fr each layer
        prev = create_layer(prev, layer_sizes[i], activations[i])

    return prev
