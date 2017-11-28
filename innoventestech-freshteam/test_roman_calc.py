#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:20:17 2017

@author: toran
"""

from roman_calc import roman_calc

class TestRomanCalc:
    """Test cases to test roman_calc() using pytest"""
    def test_addition_1(self):
        """Positive addition test"""
        assert roman_calc('I', '+', 'I') == 'II'
    
    def test_addition_2(self):
        """Positive addition test"""
        assert roman_calc('LXXXVIII', '+', 'MMMMMMMDCCCLXXXII') == 'MMMMMMMCMLXX'
    
    def test_addition_3(self):
        """Negative addition test"""
        assert roman_calc('I', '+', 'II') == 'V'
        
    def test_multiplication_1(self):
        """Positive multiplication test"""
        assert roman_calc('I', '*', 'I') == 'I'
    
    def test_multiplication_2(self):
        """Positive multiplication test"""
        assert roman_calc('XXV', '*', 'XXXV') == 'DCCCLXXV'
    
    def test_multiplication_3(self):
        """Negative multiplication test"""
        assert roman_calc('I', '*', 'II') == 'III'
        
    def test_substraction_1(self):
        """Positive substraction test"""
        assert roman_calc('II', '-', 'I') == 'I'
    
    def test_substraction_2(self):
        """Positive substraction test"""
        assert roman_calc('XXXV', '-', 'XXV') == 'X'
    
    def test_substraction_3(self):
        """Negative substraction test"""
        assert roman_calc('III', '-', 'II') == 'III'
    
    def test_division_1(self):
        """Positive division test"""
        assert roman_calc('II', '/', 'I') == 'II'
    
    def test_division_2(self):
        """Positive division test"""
        assert roman_calc('XXXV', '/', 'XXV') == 'I'
    
    def test_division_3(self):
        """Negative division test"""
        assert roman_calc('III', '/', 'II') == 'III'
        
    