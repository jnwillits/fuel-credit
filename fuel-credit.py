# !/usr/bin/env python


import json
import os
from decimal import Decimal, DecimalException

import wx

import fuel_credit_gui

set_credit_label_updated = True
vehicles_updated = True
credit_per_gal = 1
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
        data_dict = {"credit": 2.00, "Pickup Truck (sample)": 30}

    if data_dict['credit'] == None or len(data_dict) < 2:
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
            fuel_capacity = self.textCtrl_fuel_capacity.GetValue()
            Decimal(fuel_capacity)
            self.textCtrl_fuel_capacity.SetValue(str(fuel_capacity))
            self.Close()
        except DecimalException:
            wx.MessageBox('Enter a decimal amount.')

        write_data(vehicle_name, fuel_capacity)
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
        global credit_per_gal
        global data_dict
        try:
            credit_per_gal = self.textCtrl_credit_per_gallon.GetValue()
            Decimal(credit_per_gal)
            write_data('credit', credit_per_gal)
            self.textCtrl_credit_per_gallon.SetValue(str(credit_per_gal))
            set_credit_label_updated = False
            if float(credit_per_gal) < 0.01 or float(credit_per_gal) > 100:
                wx.MessageBox(
                    'You may wish to enter a more reasonable amount.')
            self.Close()
        except DecimalException:
            wx.MessageBox('Enter a decimal amount.')


class Cruncher(fuel_credit_gui.MainFrame):
    def __init__(self, parent):
        fuel_credit_gui.MainFrame.__init__(self, parent)

        ico = wx.Icon('gauge.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        self.staticText_credit_setting_label.SetLabel(
            f'Credit is set for: ${float(credit_per_gal):2.2f}')

        self.vehicle_chooser.Set(vehicles)

    def on_update_ui(self, event):
        global set_credit_label_updated
        global vehicles_updated
        if not set_credit_label_updated:
            self.staticText_credit_setting_label.SetLabel(
                f'Credit is set for: ${float(credit_per_gal):2.2f}')
            set_credit_label_updated = True
        if not vehicles_updated:
            self.vehicle_chooser.Set(vehicles)
            vehicles_updated = True

    def on_vehicle_chooser(self, event):
        global selected_vehicle
        selected_vehicle = vehicles[(self.vehicle_chooser.GetSelection())]

    def on_menuItem_credit_amount(self, event):
        dlg = SetCredit(None)
        dlg.Show(True)

    def on_menuItem_add_vehicle(self, event):
        dlg = AddVehicle(None)
        dlg.Show(True)

    def on_menuItem_delete_vehicle(self, event):
        dlg = DeleteVehicle(None)
        dlg.Show(True)


if __name__ == '__main__':
    credit_per_gal, vehicles, data_dict = read_data()
    app = wx.App(False)
    frame = Cruncher(None)
    frame.Show(True)
    app.MainLoop()
