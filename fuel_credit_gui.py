# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fuel Credit Calculator", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 610,550 ), wx.Size( 610,550 ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu5 = wx.Menu()
		self.menuItem_credit_amount = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Credit Amount", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuItem_credit_amount.SetBitmap( wx.Bitmap( u"dollar_40.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu5.Append( self.menuItem_credit_amount )

		self.m_menu1 = wx.Menu()
		self.menuItem_add_vehicle = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Add Vehicle", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuItem_add_vehicle )

		self.menuItem_delete_vehicle = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Delete Vehicle", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuItem_delete_vehicle )

		self.m_menu5.AppendSubMenu( self.m_menu1, u"Vehicles" )

		self.m_menubar1.Append( self.m_menu5, u"Setup" )

		self.menu_about = wx.Menu()
		self.menuItem_about_usage = wx.MenuItem( self.menu_about, wx.ID_ANY, u"Usage", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_about.Append( self.menuItem_about_usage )

		self.menuItem_about_software = wx.MenuItem( self.menu_about, wx.ID_ANY, u"Software", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_about.Append( self.menuItem_about_software )

		self.m_menubar1.Append( self.menu_about, u"About" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer261 = wx.BoxSizer( wx.VERTICAL )

		bSizer271 = wx.BoxSizer( wx.HORIZONTAL )

		self.staticText_credit_setting_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_credit_setting_label.Wrap( -1 )

		bSizer271.Add( self.staticText_credit_setting_label, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 25 )

		sbSizer1211 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Fuel Credit" ), wx.VERTICAL )

		sbSizer1211.SetMinSize( wx.Size( 100,50 ) )
		self.static_credit_output_label = wx.StaticText( sbSizer1211.GetStaticBox(), wx.ID_ANY, u"$X.XX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_credit_output_label.Wrap( -1 )

		self.static_credit_output_label.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		sbSizer1211.Add( self.static_credit_output_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer271.Add( sbSizer1211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 50 )


		bSizer261.Add( bSizer271, 0, wx.EXPAND, 5 )


		bSizer7.Add( bSizer261, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText77 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"1. Select a vehicle: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		self.m_staticText77.SetMaxSize( wx.Size( 100,-1 ) )

		bSizer24.Add( self.m_staticText77, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10 )

		vehicle_chooserChoices = [ u"trucks" ]
		self.vehicle_chooser = wx.Choice( self.m_panel2, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( -1,-1 ), vehicle_chooserChoices, 0 )
		self.vehicle_chooser.SetSelection( 0 )
		self.vehicle_chooser.SetMinSize( wx.Size( 300,-1 ) )
		self.vehicle_chooser.SetMaxSize( wx.Size( 300,500 ) )

		bSizer24.Add( self.vehicle_chooser, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )


		bSizer24.Add( bSizer25, 1, wx.EXPAND, 5 )


		bSizer23.Add( bSizer24, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer7.Add( bSizer23, 0, wx.EXPAND, 5 )

		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

		self.staticText_slider_1_nums = wx.StaticText( self.m_panel2, wx.ID_ANY, u"                                 E         ⅛        ¼         ⅜        ½         ⅝        ¾        ⅞          F", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_slider_1_nums.Wrap( -1 )

		self.staticText_slider_1_nums.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer121.Add( self.staticText_slider_1_nums, 0, wx.ALIGN_BOTTOM, 0 )


		bSizer7.Add( bSizer121, 0, wx.TOP, 50 )

		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText261 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"2. Fuel at check out:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText261.Wrap( -1 )

		bSizer711.Add( self.m_staticText261, 0, wx.ALL, 10 )

		self.slider_1 = wx.Slider( self.m_panel2, wx.ID_ANY, 8, 0, 16, wx.DefaultPosition, wx.Size( 400,-1 ), wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_TOP )
		bSizer711.Add( self.slider_1, 0, wx.BOTTOM, 50 )

		self.staticText_slider_1_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"1/2", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.staticText_slider_1_label.Wrap( -1 )

		self.staticText_slider_1_label.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.staticText_slider_1_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer711.Add( self.staticText_slider_1_label, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer711, 0, wx.EXPAND, 10 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.staticText_slider_1_nums1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"                                E         ⅛        ¼         ⅜        ½         ⅝        ¾        ⅞          F", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_slider_1_nums1.Wrap( -1 )

		self.staticText_slider_1_nums1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer12.Add( self.staticText_slider_1_nums1, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer12, 0, 0, 0 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText26 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"3. Fuel at check in:  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer71.Add( self.m_staticText26, 0, wx.ALL, 10 )

		self.slider_2 = wx.Slider( self.m_panel2, wx.ID_ANY, 8, 0, 16, wx.DefaultPosition, wx.Size( 400,-1 ), wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_TOP )
		bSizer71.Add( self.slider_2, 0, wx.BOTTOM, 50 )

		self.staticText_slider_2_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"1/2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_slider_2_label.Wrap( -1 )

		self.staticText_slider_2_label.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.staticText_slider_2_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer71.Add( self.staticText_slider_2_label, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer71, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer7 )
		self.m_panel2.Layout()
		bSizer7.Fit( self.m_panel2 )
		bSizer6.Add( self.m_panel2, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_menuItem_credit_amount, id = self.menuItem_credit_amount.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menuItem_add_vehicle, id = self.menuItem_add_vehicle.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menuItem_delete_vehicle, id = self.menuItem_delete_vehicle.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menuItem_about_usage, id = self.menuItem_about_usage.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menuItem_about_software, id = self.menuItem_about_software.GetId() )
		self.m_panel2.Bind( wx.EVT_UPDATE_UI, self.on_update_ui )
		self.vehicle_chooser.Bind( wx.EVT_CHOICE, self.on_vehicle_chooser )
		self.slider_1.Bind( wx.EVT_SCROLL, self.on_slider_1 )
		self.slider_2.Bind( wx.EVT_SCROLL, self.on_slider_2 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_menuItem_credit_amount( self, event ):
		event.Skip()

	def on_menuItem_add_vehicle( self, event ):
		event.Skip()

	def on_menuItem_delete_vehicle( self, event ):
		event.Skip()

	def on_menuItem_about_usage( self, event ):
		event.Skip()

	def on_menuItem_about_software( self, event ):
		event.Skip()

	def on_update_ui( self, event ):
		event.Skip()

	def on_vehicle_chooser( self, event ):
		event.Skip()

	def on_slider_1( self, event ):
		event.Skip()

	def on_slider_2( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_delete_vehicle
###########################################################################

class Dialog_delete_vehicle ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Delete a vehicle...", pos = wx.DefaultPosition, size = wx.Size( 328,199 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		ListBox_delete_vehicleChoices = [ u"x" ]
		self.ListBox_delete_vehicle = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ListBox_delete_vehicleChoices, 0 )
		self.ListBox_delete_vehicle.SetMinSize( wx.Size( -1,100 ) )

		bSizer27.Add( self.ListBox_delete_vehicle, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer5.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.button_delete_vehicle = wx.Button( self.m_panel2, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.button_delete_vehicle, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.ListBox_delete_vehicle.Bind( wx.EVT_LISTBOX, self.on_delete_vehicle_selection )
		self.button_delete_vehicle.Bind( wx.EVT_BUTTON, self.on_button_delete_vehicle )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_delete_vehicle_selection( self, event ):
		event.Skip()

	def on_button_delete_vehicle( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_add_vehicle
###########################################################################

class Dialog_add_vehicle ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add a vehicle...", pos = wx.DefaultPosition, size = wx.Size( 328,199 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		gSizer4 = wx.GridSizer( 1, 2, 0, 0 )

		self.staticText_vehicle_name = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Vehicle Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_vehicle_name.Wrap( -1 )

		gSizer4.Add( self.staticText_vehicle_name, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textCtrl_vehicle_name = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.textCtrl_vehicle_name, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer41 = wx.GridSizer( 1, 2, 0, 0 )

		self.staticText_fuel_capacity = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Fuel Capacity (gallons):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_fuel_capacity.Wrap( -1 )

		gSizer41.Add( self.staticText_fuel_capacity, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textCtrl_fuel_capacity = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer41.Add( self.textCtrl_fuel_capacity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( gSizer41, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.button_add_vehicle = wx.Button( self.m_panel2, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.button_add_vehicle, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_add_vehicle.Bind( wx.EVT_BUTTON, self.on_button_add_vehicle )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_add_vehicle( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_set_credit
###########################################################################

class Dialog_set_credit ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Set the credit amount...", pos = wx.DefaultPosition, size = wx.Size( 328,199 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		gSizer4 = wx.GridSizer( 1, 2, 0, 0 )

		self.m_staticText25 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Credit per gallon ($):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		gSizer4.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textCtrl_credit_per_gallon = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.textCtrl_credit_per_gallon, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( gSizer4, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.button_set_credit = wx.Button( self.m_panel2, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.button_set_credit, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_set_credit.Bind( wx.EVT_BUTTON, self.on_button_set_credit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_set_credit( self, event ):
		event.Skip()


