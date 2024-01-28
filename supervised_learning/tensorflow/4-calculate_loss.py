#!/usr/bin/env python3
"""Calculates the softmax cross-entropy loss of a prediction"""
import tensorflow as tf


def calculate_loss(y, y_pred):
    """
    Calculates the softmax cross-entropy loss of a prediction.
    """
    # Calculate softmax cross-entropy loss
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
        labels=y, logits=y_pred))

    return loss
