# Author: Kyle Brooks
# Created/Modified: 09/12/21

import uictrl as ui

def set_direc_display(idgrp):
    # Sets the directivity bar to zero meaning it no longer shows. Cannot toggle it back on
    grpsrc=ui.element(idgrp)
    all_property=grpsrc.getallelementbytype(ui.element_type.ELEMENT_TYPE_SCENE_RECEPTEURSP_RECEPTEUR_PROPRIETES) 
    for prop in all_property:
        # edits "Direction X"-u, "Direction Y"-v & "Direction Z"-w
        ui.element(prop).updatedecimalconfig("u",0) #X
        ui.element(prop).updatedecimalconfig("v",0) #Y
        ui.element(prop).updatedecimalconfig("w",0) #Z

def set_reciever_activation(idgrp,newstate):
    grpsrc=ui.element(idgrp) # get the punctual receiver folder
    all_property=grpsrc.getallelementbytype(ui.element_type.ELEMENT_TYPE_SCENE_RECEPTEURSP_RECEPTEUR_RENDU) # get the rendering properties
    for prop in all_property: # for each receiver 
        ui.element(prop).updateboolconfig("showlabel",newstate) # update the boolean config "showlabel" to be True or False

class manager:
    def __init__(self):
        # register each function within I-SIMPA
        self.enable_reciever_namesid=ui.application.register_event(self.enable_reciever_names)
        self.disable_reciever_namesid=ui.application.register_event(self.disable_reciever_names)
        self.disable_direc_dispid=ui.application.register_event(self.disable_direc_disp)

    def getmenu(self,typeel,idel,menu):
        # Create the menu additions, has to return True
        submenu=[]
        submenu.append((u"Enable Names", self.enable_reciever_namesid))
        submenu.append((u"Disable Names", self.disable_reciever_namesid))
        menu.insert(2,(u"Reciever Names", submenu))
        menu.insert(3,(u"Remove Directivity Lines", self.disable_direc_dispid))
        return True

    # call function for buttons
    def enable_reciever_names(self, idgrp):
        set_reciever_activation(idgrp, True)

    def disable_reciever_names(self, idgrp):
        set_reciever_activation(idgrp, False)

    def disable_direc_disp(self, idgrp):
        set_direc_display(idgrp)

ui.application.register_menu_manager(ui.element_type.ELEMENT_TYPE_SCENE_RECEPTEURSP, manager())