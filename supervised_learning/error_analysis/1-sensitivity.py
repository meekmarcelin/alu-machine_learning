#!/usr/bin/env python3
"""Sensitivity"""
import numpy as np


def sensitivity(confusion):
    # Calculate true positives for each class
    true_positives = np.diag(confusion)
    
    # Calculate false negatives for each class
    false_negatives = np.sum(confusion, axis=1) - true_positives
    
    # Calculate sensitivity for each class
    sensitivity_scores = true_positives / (true_positives + false_negatives)
    
    return sensitivity_scores
