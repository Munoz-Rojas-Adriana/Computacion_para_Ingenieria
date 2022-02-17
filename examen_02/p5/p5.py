# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:01:43 2022

@author: ACER
"""

class Animal:
    
    def __init__(self, comer, caminar ):      
        self.comer = comer
        self.caminar = caminar
       
        
    @property
    def getcomer(self):
        return self.comer
    
    def getcaminar(self):
        return self.caminar
    
    def setcomer(self, new_comer):
        self.comer = new_comer
    
    def setfcaminar(self, new_caminar):
        self.caminar = new_caminar
        
    