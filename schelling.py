#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 01:06:02 2017

@author: quien
"""

import numpy as np;
import numpy.random as rd;
import matplotlib.pyplot as plt;

def simulate(A_init,p,B,T):
    dirs = [];
    for k in range(-B,B+1):
        for l in range(-B,B+1):
            if not (k == 0 and l == 0):
                dirs = dirs + [[k,l]];
    A = -np.ones((T,A_init.shape[0],A_init.shape[1]),dtype=int);
    A[0,:,:] = np.copy(A_init);
    for t in range(1,T):
        print t;
        N = np.zeros(A.shape[1:]);
        B = np.zeros(A.shape[1:]);
        for i in range(A.shape[1]):
            for j in range(A.shape[2]):
                if A[t-1,i,j] >= 0:
                    for [k,l] in dirs:
                            if 0 <= i+k < A.shape[1] and 0 <= j+l < A.shape[2]:
                                N[i,j] = N[i,j] + (1 if A[t-1,i+k,j+l] >= 0 else 0);
                                B[i,j] = B[i,j] + (1 if A[t-1,i+k,j+l] == A[t-1,i,j] else 0);
        for i in range(A.shape[1]):
            for j in range(A.shape[2]):
                if A[t-1,i,j] >= 0:
                    if B[i,j] >= p[A[t-1,i,j]]*N[i,j] or N[i,j] == len(dirs):
                        A[t,i,j] = A[t-1,i,j];
        for i in range(A.shape[1]):
            for j in range(A.shape[2]):
                k = 0;
                l = 0;
                if A[t-1,i,j] >= 0:
                    if B[i,j] <= p[A[t-1,i,j]]*N[i,j] or N[i,j] == 0:
                        s = rd.randint(8);
                        for m in range(len(dirs)):
                            k_,l_ = dirs[(s+m)%len(dirs)];
                            if 0 <= i+k_ < A.shape[1] and 0 <= j+l_ < A.shape[2] and A[t,i+k_,j+l_] < 0:
                                k = k_;
                                l = l_;
                                break;
                A[t,i+k,j+l] = A[t-1,i,j];
    return A;

A_init = rd.randint(-1,2,size=(128,128));

A = simulate(A_init,[0.5,0.5],2,20);