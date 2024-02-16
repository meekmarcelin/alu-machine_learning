#!/usr/bin/env python3
"""Precision"""
import numpy as np


def precision(confusion):
    # Calculate true positives for each class
    true_positives = np.diag(confusion)
    
    # Calculate false positives for each class
    false_positives = np.sum(confusion, axis=0) - true_positives
    
    # Calculate precision for each class
    precision_scores = true_positives / (true_positives + false_positives)
    
    return precision_scores
