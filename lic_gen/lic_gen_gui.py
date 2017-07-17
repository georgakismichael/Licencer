# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class lic_gen_frm
###########################################################################

class lic_gen_frm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CRS-Licence Generator", pos = wx.DefaultPosition, size = wx.Size( 364,187 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Expiry Date:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.Expiry_txt = wx.TextCtrl( self, wx.ID_ANY, u"2017-07-22", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Expiry_txt.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer4.Add( self.Expiry_txt, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND|wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"No. of uses: ", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer6.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.Usage_txt = wx.TextCtrl( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Usage_txt.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer6.Add( self.Usage_txt, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Generate Licence", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer1.Add( bSizer6, 1, wx.EXPAND|wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"© ProsoftCY 2017. All rights reserved.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer7.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer7, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.generate_licence_func )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def generate_licence_func( self, event ):
		event.Skip()
	

