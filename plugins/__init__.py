import re
import datetime
import logging
import os
import sys
from pathlib import Path
from typing import Tuple

import pcbnew
import wx

class TraceLengthAction(pcbnew.ActionPlugin):
    """
    test_by_date: A sample plugin as an example of ActionPlugin
    Add the date to any text field of the board containing '$date$'
    How to use:
    - Add a text on your board with the content '$date$'
    - Call the plugin
    - The text will automatically be updated with the date (format YYYY-MM-DD)
    """

    def defaults(self):
        """
        Method defaults must be redefined
        self.name should be the menu label to use
        self.category should be the category (not yet used)
        self.description should be a comprehensive description of the plugin
        """
        self.name = "Trace Length"
        self.category = "Measure PCB"
        self.description = "Measure Length of the selected trace"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "icon.png")
        
    def Run(self):
        pcb = pcbnew.GetBoard()
        trace = pcb.GetTracks()
        r = 1.68/100000      # copper resistivity [Ohm * mm^2 / m]
        a = 4.29/1000        # resistivity temperature coefficient     
        trace_length = 0
        R_trace = 0
        h = 0.035			# coper track segment heigth in mm 
        w = 0.0				# coper track segment width in mm 

        for item in pcb.GetDrawings():
            if item.GetClass() == "PCB_TEXT":
                txt = re.sub("\$date\$ [0-9]{4}-[0-9]{2}-[0-9]{2}",
                                 "$date$", item.GetText())
                if txt == "$date$":
                    item.SetText("%s" % datetime.date.today())
                    
        for track in pcb.GetTracks():
            if track.IsSelected():
                track_length = track.GetLength()/1000000
                trace_length = trace_length + track_length
                w = track.GetWidth()/1000000 
                A = w*h
                R_track = r * track_length /A
                R_trace = R_trace + R_track
        
        #R_trace = r * trace_length / A       
        wx.MessageBox(	'Copper trace tickness: %.3f' % h 		+ ' mm \n '
        				'Trace Length =  %.4f' % trace_length 	+ ' mm \n ' 
        				'Trace Width  =  %.3f' % w 				+ ' mm \n ' 
        				'Trace Res    =  %.3f' % R_trace 		+ ' Ohm \n ', 
        				'Info',  wx.OK | wx.ICON_INFORMATION)
		# 'Copper trace hegth: %.4f'% h + ' mm' +,
TraceLengthAction().register()
