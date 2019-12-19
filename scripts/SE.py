#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import gui
import wx
from PIL import Image

# In[3]:


class Element:
    def __init__(self,position,name='',design=None):
        self.position = position
        self.name = name
        self.design = design

class Map:
    def __init__(self,name,size = [10,10],bg = None):
        self.name=name
        self.bg=bg
        self.elements = np.array([[Element([x,y]) for y in range(size[1])] for x in range(size[0])])
        
        
    def size(self):
        return self.elements.shape
    
    def resize(self,size):
        self.elements = np.array([[Element([x,y]) for y in range(size[1])] for x in range(size[0])])
        


# In[5]:


#for the gui
class MyFrame1_impl (MyFrame1):
    
    def __init__( self, parent ):
        MyFrame1.__init__(self, parent)
        self.current_map = Map("Empty")
        
    def create_new_map( self, event ):
        
        newmap(self).Show()


# In[56]:


#print(a.resize(10,20))


# In[4]:


#import unittest


if __name__=="__main__":

    app = wx.App()
    frame = MyFrame1_impl(None).Show()
    app.MainLoop()







