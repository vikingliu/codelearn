# coding=utf-8

import numpy as np
import math
import sys

sys.path.append('../../../')
from utils import nn_utils



# attention(Q,K,V) = Σsoftmax(f(Q, Ki))Vi
# f(Q, Ki) = Q.T · Ki                   dot
#          = Q.T · Wα · Ki              general
#          = Wα · [Q.T; Ki]             concat
#          = Vα.T · tanh(Wα·Q + Uα·Ki)  perceptron

# basic attention structure
# soft Attention 与Hard Attention
# Global Attention 和 Local Attention
# Self Attention

# combination structure
# Hierarchical Attention
# Attention over Attention
# Multi-Step Attention

def f_dot(Q, K):
    return np.matmul(Q, K)


def f_general(Q, K, W_alpha):
    return np.matmul(np.matmul(Q, W_alpha), K)


def f_concat(Q, K, W_alpha):
    return np.matmul(W_alpha, np.concatenate((Q.T, K), axis=0))


def f_perceptron(Q, K, W_alpha, U_alpha, V_alpha):
    return np.matmul(V_alpha, nn_utils.tanh(np.matmul(W_alpha, Q) + np.matmul(U_alpha, K)))


def attention(Q, K, V, f, d_k=1):
    col = [i for i in range(len(K.shape))]
    col[-2], col[-1] = col[-1], col[-2]
    return nn_utils.softmax(f(Q, K.transpose(tuple(col))) / d_k).dot(V)


def self_attention(query, key, value, W_Q, W_K, W_V):
    Q = np.matmul(query, W_Q)
    K = np.matmul(key, W_K)
    V = np.matmul(value, W_V)
    # d_k 对输入向量长度开根号
    d_k = math.sqrt(query.shape[-1])
    Z = attention(Q, K, V, f_dot, d_k)
    return Z


def multi_headed_attenton(queries, keys, values, Ws, W_O):
    """

    :param queries:  query split to headed queries
    :param keys: key split to headed keys
    :param values: value split to headed values
    :param Ws: [(W_Q0, W_K0, W_V0),......]
    :param W_O:
    :return:
    """
    Z = []
    for i in xrange(len(Ws)):
        W_Q, W_K, W_V = Ws[i]
        Zi = self_attention(queries[i], keys[i], values[1], W_Q, W_K, W_V)
        Z.append(Zi)
    Z = np.concatenate(Z, axis=0)
    return Z.dot(W_O)
