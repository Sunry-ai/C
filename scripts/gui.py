# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 697,397 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        self.m_toolBar20 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
        self.newmap = self.m_toolBar20.AddLabelTool( wx.ID_ANY, u"new", wx.Bitmap( u"../images/fileicon.bmp", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"create a new map", wx.EmptyString, None ) 
        
        self.m_toolBar20.AddSeparator()
        
        self.open = self.m_toolBar20.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"../images/open.bmp", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"open....", wx.EmptyString, None ) 
        
        self.m_toolBar20.AddSeparator()
        
        self.save = self.m_toolBar20.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"../images/save.bmp", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"save as...", wx.EmptyString, None ) 

        self.m_toolBar20.AddSeparator()

        self.temporary = self.m_toolBar20.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"../images/e.bmp", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 

        self.m_toolBar20.AddSeparator()
        
        self.elements = self.m_toolBar20.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"../images/e.bmp", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
        
        self.m_toolBar20.AddSeparator()
        
        self.m_toolBar20.Realize() 
        
        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
        gbSizer3.Add( self.m_listCtrl2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_listCtrl3 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
        gbSizer3.Add( self.m_listCtrl3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_listCtrl4 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
        gbSizer3.Add( self.m_listCtrl4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        m_listBox2Choices = []
        self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
        gbSizer3.Add( self.m_listBox2, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        m_listBox3Choices = []
        self.m_listBox3 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, 0 )
        gbSizer3.Add( self.m_listBox3, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        m_choice3Choices = []
        self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        gbSizer3.Add( self.m_choice3, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        m_choice4Choices = []
        self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
        self.m_choice4.SetSelection( 0 )
        gbSizer3.Add( self.m_choice4, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        #gbSizer3.AddGrowableCol( 1 )
        #gbSizer3.AddGrowableRow( 1 )
        
        self.SetSizer( gbSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
# Connect Events
        self.Bind( wx.EVT_TOOL, self.create_new_map, id = self.newmap.GetId() )
        self.Bind( wx.EVT_TOOL, self.open_map, id = self.open.GetId() )
        self.Bind( wx.EVT_TOOL, self.return_laststep, id = self.temporary.GetId() )
        self.Bind( wx.EVT_TOOL, self.load_element, id = self.elements.GetId() )
        
    def __del__( self ):
        pass


# Virtual event handlers, overide them in your derived class
    def create_new_map( self, event ):
        pass

    def open_map( self, event ):
        pass

    def return_laststep( self, event ):
        pass

    def load_element( self, event ):
        pass


###########################################################################
## Class open
###########################################################################

class open ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"open file", pos = wx.DefaultPosition, size = wx.Size( 273,108 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.pick_file = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer6.Add( self.pick_file, 0, wx.ALL, 5 )
        
        self.input_button = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.input_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer6 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
# Connect Events
        self.input_button.Bind( wx.EVT_BUTTON, self.input_file )
        
    def __del__( self ):
        pass


# Virtual event handlers, overide them in your derived class
    def input_file( self, event ):
        pass


###########################################################################
## Class save
###########################################################################

class save ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 252,113 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.savedir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        bSizer7.Add( self.savedir, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.save_button = wx.Button( self, wx.ID_ANY, u"save", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.save_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer7 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
# Connect Events
        self.save_button.Bind( wx.EVT_BUTTON, self.save_map )

    def __del__( self ):
        pass


# Virtual event handlers, overide them in your derived class
    def save_map( self, event ):
        pass


###########################################################################
## Class elements
###########################################################################

class elements ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar2 = wx.MenuBar( 0 )
        self.add_E = wx.Menu()
        self.add_1 = wx.MenuItem( self.add_E, wx.ID_ANY, u"Open...", wx.EmptyString, wx.ITEM_NORMAL )
        self.add_E.AppendItem( self.add_1 )
        
        self.add_E.AppendSeparator()
        
        self.add_2 = wx.MenuItem( self.add_E, wx.ID_ANY, u"Common elements...", wx.EmptyString, wx.ITEM_NORMAL )
        self.add_E.AppendItem( self.add_2 )
        
        self.m_menubar2.Append( self.add_E, u"add..." ) 
        
        self.Clipping = wx.Menu()
        self.clipping = wx.MenuItem( self.Clipping, wx.ID_ANY, u"Clipping", wx.EmptyString, wx.ITEM_NORMAL )
        self.Clipping.AppendItem( self.clipping )
        
        self.rotate = wx.MenuItem( self.Clipping, wx.ID_ANY, u"Rotate", wx.EmptyString, wx.ITEM_NORMAL )
        self.Clipping.AppendItem( self.rotate )
        
        self.m_menubar2.Append( self.Clipping, u"Clipping" ) 
        
        self.Rotate = wx.Menu()
        self.m_menubar2.Append( self.Rotate, u"Rotate" ) 
        
        self.Copy = wx.Menu()
        self.copy = wx.MenuItem( self.Copy, wx.ID_ANY, u"Copy", wx.EmptyString, wx.ITEM_NORMAL )
        self.Copy.AppendItem( self.copy )
        
        self.m_menubar2.Append( self.Copy, u"Copy" ) 
        
        self.Paste = wx.Menu()
        self.Paste = wx.MenuItem( self.Paste, wx.ID_ANY, u"Paste", wx.EmptyString, wx.ITEM_NORMAL )
        self.Paste.AppendItem( self.Paste )
        
        self.m_menubar2.Append( self.Paste, u"Paste" ) 
        
        self.Set = wx.Menu()
        self.big = wx.MenuItem( self.Set, wx.ID_ANY, u"Magnify +", wx.EmptyString, wx.ITEM_NORMAL )
        self.Set.AppendItem( self.big )
        
        self.Set.AppendSeparator()
        
        self.small = wx.MenuItem( self.Set, wx.ID_ANY, u" Shrink -", wx.EmptyString, wx.ITEM_NORMAL )
        self.Set.AppendItem( self.small )
        
        self.Set.AppendSeparator()
        
        self.m_menubar2.Append( self.Set, u"Settings" ) 
        
        self.save = wx.Menu()
        self.savedir = wx.MenuItem( self.save, wx.ID_ANY, u"save dir", wx.EmptyString, wx.ITEM_NORMAL )
        self.save.AppendItem( self.savedir )
        
        self.m_menubar2.Append( self.save, u"Save as..." ) 
        
        self.SetMenuBar( self.m_menubar2 )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.E_back = wx.Button( self, wx.ID_ANY, u"use", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.E_back, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer9 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
# Connect Events
        self.Bind( wx.EVT_MENU, self.Open_E, id = self.add_1.GetId() )
        self.Bind( wx.EVT_MENU, self.Common_E, id = self.add_2.GetId() )
        self.Bind( wx.EVT_MENU, self.Clipping_E, id = self.clipping.GetId() )
        self.Bind( wx.EVT_MENU, self.Rotate_E, id = self.rotate.GetId() )
        self.Bind( wx.EVT_MENU, self.Copy_E, id = self.copy.GetId() )
        self.Bind( wx.EVT_MENU, self.Paste_E, id = self.Paste.GetId() )
        self.Bind( wx.EVT_MENU, self.Magify_E, id = self.big.GetId() )
        self.Bind( wx.EVT_MENU, self.Shrink_E, id = self.small.GetId() )
        self.Bind( wx.EVT_MENU, self.save_E, id = self.savedir.GetId() )
        self.E_back.Bind( wx.EVT_BUTTON, self.E_back_Frame )
        
    def __del__( self ):
        pass


# Virtual event handlers, overide them in your derived class
    def Open_E( self, event ):
        pass

    def Common_E( self, event ):
        pass

    def Clipping_E( self, event ):
        pass

    def Rotate_E( self, event ):
        pass

    def Copy_E( self, event ):
        pass

    def Paste_E( self, event ):
        pass

    def Magify_E( self, event ):
        pass

    def Shrink_E( self, event ):
        pass

    def save_E( self, event ):
        pass

    def E_back_Frame( self, event ):
        pass


###########################################################################
## Class newmap
###########################################################################

class newmap ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"please select your map size", pos = wx.DefaultPosition, size = wx.Size( 373,265 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"length", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer1.Add( self.m_staticText1, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.length = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.length, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"width", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.width = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.width, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.bg = wx.StaticText( self, wx.ID_ANY, u"background", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bg.Wrap( -1 )
        bSizer1.Add( self.bg, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_colourPicker1 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        bSizer1.Add( self.m_colourPicker1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.size = wx.Button( self, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.size, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
# Connect Events
        self.Bind( wx.EVT_INIT_DIALOG, self.save_map )
        self.length.Bind( wx.EVT_TEXT, self.make_size )
        self.length.Bind( wx.EVT_TEXT_ENTER, self.value_len )
        self.width.Bind( wx.EVT_TEXT, self.make_size )
        self.width.Bind( wx.EVT_TEXT_ENTER, self.value_wid )
        self.m_colourPicker1.Bind( wx.EVT_COLOURPICKER_CHANGED, self.bg_colour )
        self.size.Bind( wx.EVT_BUTTON, self.return_Frame1 )

    def __del__( self ):
        pass


# Virtual event handlers, overide them in your derived class
    def save_map( self, event ):
        pass

    def make_size( self, event ):
        pass

    def value_len( self, event ):
        pass


    def value_wid( self, event ):
        pass

    def bg_colour( self, event ):
        pass

    def return_Frame1( self, event ):
        pass


