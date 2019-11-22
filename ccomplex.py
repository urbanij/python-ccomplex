#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Nov 10 11:00:27 CET 2019

@author(s)   : Francesco Urbani
@file        : ccomplex.py
@descritpion : better representation of complex numbers, e.g.:
               (2.0+4.1j)   ->    2+j4.1
               (23-0j)      ->    23
               (0-32j)      ->    -j32

"""

class ccomplex(complex):
    def __str__(self):   
        repr_real_part = int(self.real) if self.real == int(self.real) else self.real
        repr_imag_part = int(self.imag) if self.imag == int(self.imag) else self.imag

        repr_real_part = 0 if abs(repr_imag_part) > 1e9*abs(repr_real_part) else repr_real_part
        repr_imag_part = 0 if abs(repr_real_part) > 1e9*abs(repr_imag_part) else repr_imag_part

        
        if   repr_real_part == 0 and repr_imag_part == 0: return '0'

        elif repr_real_part == 0 and repr_imag_part  > 0: return f"j{repr_imag_part}"
        elif repr_real_part == 0 and repr_imag_part  < 0: return f"-j{-repr_imag_part}"
        
        elif                         repr_imag_part == 0: return str(repr_real_part)

        elif                         repr_imag_part > 0:  return f"{repr_real_part}+j{repr_imag_part}"
        elif                         repr_imag_part < 0:  return f"{repr_real_part}-j{-repr_imag_part}"

        else:                                             return f"{complex(self)}"     # should never be reached 


