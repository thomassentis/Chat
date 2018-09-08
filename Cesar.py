# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:59:51 2018

@author: antoine
"""

alphabet = "è16àvûmFY>-=ùl04PkMöR<D@EâtK?g'h3n[I*o+°9GUu/Td£S7_ç]üW!CéA(jqbêxïz yB8~^w§%:QµONHV`îifX})|Lc#ëË&e{rôsp,a\\;J2Z.5"
size = len (alphabet)

def encode (m, k) :
    s = ""
    for i in m:
        if i in alphabet:
            s += alphabet [(alphabet.find (i) + k) % size]
        else:
            s += i
    return s

def decode (m, k) :
    s = ""
    for i in m:
        if i in alphabet:
            s += alphabet [(alphabet.find (i) - k) % size]
        else:
            s += i
    return s