# !/usr/bin/env python

"""
Jeff's Fuel Credit Calculator
A handy calculator utility to help a business with vehicle rental.
Jeffrey Neil Willits  @jnwillits
"""


import json
import os
from decimal import Decimal, DecimalException

import wx

import fuel_credit_gui

set_credit_label_updated = True
credit_output_updated = True
vehicles_updated = True
credit_per_gal = 1
fuel_cap = 0
val_slider_1 = 8
val_slider_2 = 8
data_dict = {}
vehicles = []
selected_vehicle = ''


def update_vehicles():
    vehicles = list(data_dict.keys())
    # Strip 'credit' from list.
    temp_lst = []
    for i in range(0, len(vehicles)):
        if vehicles[i] != 'credit':
            temp_lst.append(vehicles[i])
    vehicles = temp_lst
    return vehicles


def read_data():
    global data_dict
    global vehicles
    if os.path.isfile('fuel-credit.json'):
        with open('fuel-credit.json') as f_obj:
            data_dict = json.load(f_obj)
    else:
        data_dict = {"credit": 2.00, "Pickup Truck (sample)": '30'}

    if data_dict['credit'] is None or len(data_dict) < 2:
        data_dict = {"credit": 2.00, "Pickup Truck (sample)": 30}

    credit_per_gal = float(data_dict['credit'])
    vehicles = update_vehicles()
    return credit_per_gal, vehicles, data_dict


def write_data(new_key, new_value):
    data_dict[new_key] = new_value
    with open('fuel-credit.json', 'w') as f_obj:
        json.dump(data_dict, f_obj)


class AddVehicle(fuel_credit_gui.Dialog_set_credit):
    def __init__(self, parent):
        fuel_credit_gui.Dialog_add_vehicle.__init__(self, parent)

    def on_button_add_vehicle(self, event):
        global vehicles
        global vehicles_updated
        vehicle_name = self.textCtrl_vehicle_name.GetValue()
        self.textCtrl_vehicle_name.SetValue(str(vehicles))

        try:
            fuel_cap = self.textCtrl_fuel_cap.GetValue()
            Decimal(fuel_cap)
            self.textCtrl_fuel_cap.SetValue(str(fuel_cap))
            self.Close()
        except DecimalException:
            wx.MessageBox('Enter a decimal amount.')

        write_data(vehicle_name, fuel_cap)
        vehicles = update_vehicles()
        vehicles_updated = False
        self.Close()


class DeleteVehicle(fuel_credit_gui.Dialog_set_credit):
    def __init__(self, parent):
        fuel_credit_gui.Dialog_delete_vehicle.__init__(self, parent)

        self.deleted_vehicle = ''

        self.ListBox_delete_vehicle.Set(vehicles)

    def on_delete_vehicle_selection(self, event):
        self.deleted_vehicle = vehicles[(
            self.ListBox_delete_vehicle.GetSelection())]

    def on_button_delete_vehicle(self, event):
        global data_dict
        global vehicles
        global vehicles_updated
        del data_dict[self.deleted_vehicle]
        vehicles = update_vehicles()
        with open('fuel-credit.json', 'w') as f_obj:
            json.dump(data_dict, f_obj)
        vehicles_updated = False
        self.Close()


class SetCredit(fuel_credit_gui.Dialog_set_credit):
    def __init__(self, parent):
        fuel_credit_gui.Dialog_set_credit.__init__(self, parent)

    def on_button_set_credit(self, event):
        global set_credit_label_updated
        global credit_output_updated
        global credit_per_gal
        global data_dict
        try:
            credit_per_gal = self.textCtrl_credit_per_gallon.GetValue()
            Decimal(credit_per_gal)
            write_data('credit', credit_per_gal)
            self.textCtrl_credit_per_gallon.SetValue(str(credit_per_gal))
            set_credit_label_updated = False
            credit_output_updated = False
            if float(credit_per_gal) < 0.01 or float(credit_per_gal) > 100:
                wx.MessageBox(
                    'You may wish to enter a more reasonable amount.')
            self.Close()
        except DecimalException:
            wx.MessageBox('Enter a decimal amount.')


class Usage(fuel_credit_gui.Dialog_usage):
    def __init__(self, parent):
        fuel_credit_gui.Dialog_usage.__init__(self, parent)

    def on_button_usage_close(self, event):
        self.Close()


class Software(fuel_credit_gui.Dialog_software):
    def __init__(self, parent):
        fuel_credit_gui.Dialog_software.__init__(self, parent)

    def on_button_software_close(self, event):
        self.Close()


class Cruncher(fuel_credit_gui.MainFrame):
    def __init__(self, parent):
        fuel_credit_gui.MainFrame.__init__(self, parent)

        # Disabling the icon for now...
        # ico = wx.Icon('gauge.ico', wx.BITMAP_TYPE_ICO)
        # self.SetIcon(ico)

        self.staticText_credit_setting_label.SetLabel(
            f'Credit is set for ${float(credit_per_gal):2.2f}.')

        self.vehicle_chooser.Set(vehicles)

    def calculate_credit(self):
        return ((val_slider_2 - val_slider_1) / 16) * fuel_cap * float(credit_per_gal)

    def on_update_ui(self, event):
        global set_credit_label_updated
        global credit_output_updated
        global vehicles_updated
        if not set_credit_label_updated:
            self.staticText_credit_setting_label.SetLabel(
                f'Credit is set for ${float(credit_per_gal):2.2f}.')
            set_credit_label_updated = True
        if not vehicles_updated:
            self.vehicle_chooser.Set(vehicles)
            vehicles_updated = True
        if not credit_output_updated:
            if self.calculate_credit() > 0:
                self.static_credit_output_label.SetLabel(
                    f'${self.calculate_credit():2.2f}')
            else:
                self.static_credit_output_label.SetLabel('No Credit')
            credit_output_updated = True

    def slider_label(self, val_slider):
        labs = ['E', '1/16', '1/8', '3/16', '1/4', '5/16', '3/8', '7/16',
                '1/2', '9/16', '5/8', '11/16', '3/4', '13/16']
        return labs[val_slider]

    def on_slider_1(self, event):
        global val_slider_1
        global credit_output_updated
        credit_output_updated = False
        obj = event.GetEventObject()
        val_slider_1 = obj.GetValue()
        self.staticText_slider_1_label.SetLabel(
            self.slider_label(val_slider_1))

    def on_slider_2(self, event):
        global val_slider_2
        global credit_output_updated
        credit_output_updated = False
        obj = event.GetEventObject()
        val_slider_2 = obj.GetValue()
        self.staticText_slider_2_label.SetLabel(
            self.slider_label(val_slider_2))

    def on_vehicle_chooser(self, event):
        global selected_vehicle
        global credit_output_updated
        global fuel_cap
        credit_output_updated = False
        selected_vehicle = vehicles[(self.vehicle_chooser.GetSelection())]
        fuel_cap = float(data_dict[selected_vehicle])

    def on_menuItem_credit_amount(self, event):
        dlg = SetCredit(None)
        dlg.Show(True)

    def on_menuItem_add_vehicle(self, event):
        dlg = AddVehicle(None)
        dlg.Show(True)

    def on_menuItem_delete_vehicle(self, event):
        global fuel_cap
        dlg = DeleteVehicle(None)
        dlg.Show(True)
        self.static_credit_output_label.SetLabel('No Credit')
        fuel_cap = 0

    def on_menuItem_software(self, event):
        dlg = Software(None)
        dlg.Show(True)

    def on_menuItem_usage(self, event):
        dlg = Usage(None)
        dlg.Show(True)
        print('usage firing')


if __name__ == '__main__':
    credit_per_gal, vehicles, data_dict = read_data()
    app = wx.App(False)
    frame = Cruncher(None)
    frame.Show(True)
    app.MainLoop()
