# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class AutoTesterFrm
###########################################################################

class AutoTesterFrm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AutoTester", pos = wx.DefaultPosition, size = wx.Size( 701,456 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.status_bar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.menubar = wx.MenuBar( 0 )
		self.mnu_file = wx.Menu()
		self.mnu_file_exit = wx.MenuItem( self.mnu_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_file.AppendItem( self.mnu_file_exit )
		
		self.menubar.Append( self.mnu_file, u"File" ) 
		
		self.mnu_help = wx.Menu()
		self.mnu_help_about = wx.MenuItem( self.mnu_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_help.AppendItem( self.mnu_help_about )
		
		self.menubar.Append( self.mnu_help, u"Help" ) 
		
		self.SetMenuBar( self.menubar )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.panel_left = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel_left_upper = wx.Panel( self.panel_left, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.lbl_serial_ports = wx.StaticText( self.panel_left_upper, wx.ID_ANY, u"Serial Ports", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_serial_ports.Wrap( -1 )
		self.lbl_serial_ports.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.lbl_serial_ports, 0, wx.ALL, 5 )
		
		ports_listChoices = []
		self.ports_list = wx.Choice( self.panel_left_upper, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ports_listChoices, 0 )
		self.ports_list.SetSelection( 0 )
		bSizer3.Add( self.ports_list, 0, wx.ALL, 5 )
		
		
		self.panel_left_upper.SetSizer( bSizer3 )
		self.panel_left_upper.Layout()
		bSizer3.Fit( self.panel_left_upper )
		bSizer2.Add( self.panel_left_upper, 0, wx.EXPAND, 1 )
		
		self.panel_left_lower = wx.Panel( self.panel_left, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.lbl_port_settings = wx.StaticText( self.panel_left_lower, wx.ID_ANY, u"Port Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_port_settings.Wrap( -1 )
		self.lbl_port_settings.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.lbl_port_settings, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.panel_left_lower, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer4.Add( self.m_staticline1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )
		
		self.lbl_baudrate = wx.StaticText( self.panel_left_lower, wx.ID_ANY, u"Baudrate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_baudrate.Wrap( -1 )
		gbSizer4.Add( self.lbl_baudrate, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		baudrate_listChoices = [ u"1200", u"2400", u"4800", u"9600", u"14400", u"19200", u"38400", u"43000", u"57600", u"76800", u"115200", u"12800" ]
		self.baudrate_list = wx.Choice( self.panel_left_lower, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, baudrate_listChoices, 0 )
		self.baudrate_list.SetSelection( 5 )
		gbSizer4.Add( self.baudrate_list, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lbl_parity = wx.StaticText( self.panel_left_lower, wx.ID_ANY, u"Parity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_parity.Wrap( -1 )
		gbSizer4.Add( self.lbl_parity, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		parity_listChoices = [ u"N", u"E", u"O", u"M", u"S" ]
		self.parity_list = wx.Choice( self.panel_left_lower, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, parity_listChoices, 0 )
		self.parity_list.SetSelection( 0 )
		gbSizer4.Add( self.parity_list, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lbl_databit = wx.StaticText( self.panel_left_lower, wx.ID_ANY, u"DataBit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_databit.Wrap( -1 )
		gbSizer4.Add( self.lbl_databit, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		databit_listChoices = [ u"5", u"6", u"7", u"8" ]
		self.databit_list = wx.Choice( self.panel_left_lower, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, databit_listChoices, 0 )
		self.databit_list.SetSelection( 3 )
		gbSizer4.Add( self.databit_list, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.lbl_stopbit = wx.StaticText( self.panel_left_lower, wx.ID_ANY, u"StopBit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_stopbit.Wrap( -1 )
		gbSizer4.Add( self.lbl_stopbit, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		stopbit_listChoices = [ u"1", u"1.5", u"2" ]
		self.stopbit_list = wx.Choice( self.panel_left_lower, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, stopbit_listChoices, 0 )
		self.stopbit_list.SetSelection( 0 )
		gbSizer4.Add( self.stopbit_list, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.panel_left_lower.SetSizer( gbSizer4 )
		self.panel_left_lower.Layout()
		gbSizer4.Fit( self.panel_left_lower )
		bSizer2.Add( self.panel_left_lower, 0, wx.EXPAND |wx.ALL, 1 )
		
		self.tgl_btn_open = wx.ToggleButton( self.panel_left, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.tgl_btn_open, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		
		self.panel_left.SetSizer( bSizer2 )
		self.panel_left.Layout()
		bSizer2.Fit( self.panel_left )
		bSizer1.Add( self.panel_left, 0, wx.EXPAND, 5 )
		
		self.panel_right = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel_right_quick_keys = wx.Panel( self.panel_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.lbl_quick_keys = wx.StaticText( self.panel_right_quick_keys, wx.ID_ANY, u"Quick Keys", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_quick_keys.Wrap( -1 )
		self.lbl_quick_keys.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer7.Add( self.lbl_quick_keys, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.panel_right_quick_keys, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer7.Add( self.m_staticline2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 5 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button2, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button3, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button4, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button5, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button6, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button7, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button8, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button9, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button10 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button10, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button11 = wx.Button( self.panel_right_quick_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_button11, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.panel_right_quick_keys.SetSizer( gbSizer7 )
		self.panel_right_quick_keys.Layout()
		gbSizer7.Fit( self.panel_right_quick_keys )
		bSizer4.Add( self.panel_right_quick_keys, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panel_right_command_keys = wx.Panel( self.panel_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.lbl_cmd_keys = wx.StaticText( self.panel_right_command_keys, wx.ID_ANY, u"Command Keys", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_cmd_keys.Wrap( -1 )
		self.lbl_cmd_keys.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer8.Add( self.lbl_cmd_keys, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.panel_right_command_keys, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer8.Add( self.m_staticline3, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 5 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_button12 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button12, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button13 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button13, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button14, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button15, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button16, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button17 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button17, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button18 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button18, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button19 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button19, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button20 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button20, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button21 = wx.Button( self.panel_right_command_keys, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.m_button21, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.panel_right_command_keys.SetSizer( gbSizer8 )
		self.panel_right_command_keys.Layout()
		gbSizer8.Fit( self.panel_right_command_keys )
		bSizer4.Add( self.panel_right_command_keys, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panel_right_scripts = wx.Panel( self.panel_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.panel_right_scripts, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panel_right.SetSizer( bSizer4 )
		self.panel_right.Layout()
		bSizer4.Fit( self.panel_right )
		bSizer1.Add( self.panel_right, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

