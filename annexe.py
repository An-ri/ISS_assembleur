#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:35:17 2019

@author: ramiduye
"""

def dec2bin(d,nb=8):
    """Représentation d'un nombre entier en chaine binaire (nb: nombre de bits du mot)"""
    if d == 0:
        return "0".zfill(nb)
    if d<0:
        d += 1<<nb
    b=""
    while d != 0:
        d, r = divmod(d, 2)
        b = "01"[r] + b
    return b.zfill(nb)

def bin2dec(b):
	i=0
	n=len(b)
	puissance=0
	index=-1
	while index>=-n:
		if b[index]=='1':
			i= i + 2**puissance
		elif b[index]!='0' :
			return None
		puissance= puissance +1
		index=index-1
	return i



