# KICAD Trace Length

## [PCB Editor | 8.0 | English | Documentation | KiCad](https://docs.kicad.org/8.0/en/pcbnew/pcbnew.html#scripting)

```python
import pcbnew
import re
import datetime

class text_by_date(pcbnew.ActionPlugin):
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
        self.description should be a comprehensive description
          of the plugin
        """
        self.name = "Add date on PCB"
        self.category = "Modify PCB"
        self.description = "Automatically add date on an existing PCB"

    def Run(self):
        pcb = pcbnew.GetBoard()
        for item in pcb.GetDrawings():
            if item.GetClass() == "PCB_TEXT":
                txt = re.sub("\$date\$ [0-9]{4}-[0-9]{2}-[0-9]{2}",
                                 "$date$", item.GetText())
                if txt == "$date$":
                    item.SetText("$date$ %s" % datetime.date.today())


text_by_date().register()
```

[KiCAD bus length matching script which also adds in the &quot;Pad to die length&quot; into the calculations · GitHub](https://gist.github.com/korken89/999c5cdd67d773589fce77b21ee5ed60)

## Kicad Trace Length Plugin (Bruce T)

[ref](https://www.youtube.com/@brucet7789) 

[Kicad Trace Length Plugin - YouTube](https://www.youtube.com/watch?v=WjDrvnIFPVY)

Kicad Plugin:  Get the Length of Traces on PCB

Click the Cog in Play Window for Speed Controls
Code is in the Video

UPDATE: Sept 9, 2022.  Added Code for both Inductance and Resistance (code below)

How To Do It:

- What You Will Need:
  • Knowledge from this Link: https://dev-docs.kicad.org/en/python/...
  
  • A Text Editor or Python/other Code Software (many are Free. I use IDLE )

Note's:
• Python is Very Picky about Indentation, Spacing and Tabs. The Code works great so, if you have trouble, methodically check your coding (Python = Trouble... I have nothing good to say about Python)
• The " i " in the code is not needed but, if wanting a Counter (to count the Traces Changed)... You know what to do...
• Here's a Code Change to display Track Length (4 decimal places) and the Number of Measured Tracks and Track Resistance (just Copy & Paste it (replacing the previous code):

```python
    def Run(self):        
        board = GetBoard() # This is to load the board inside kicad python console
        tracks = board.GetTracks()
        i = 0
        total = 0
        Xtotal = 0
        each = 0
        h = 0.035/25.4                         # to inches
        w = 0.0
        imp = 0
        ARG1 = 0
        ARG2 = 0

        for track in board.GetTracks():
            if track.IsSelected():
               each = track.GetLength()
               total = each/1000000 + total            # to mm
               w = track.GetWidth()/1000000 / 25.4     # M to mm to inches
               i = i + 1

               Xtotal = total/25.4                     # to inches

               ARG1 = (2 * Xtotal)/(w + h)
               ARG2 = 0.2235 * (w + h) / Xtotal
               imp = 0.00508 * Xtotal * (math.log(ARG1) + 0.5 + ARG2)
               #'Log' defaults to Natural Log.  Log10 is base 10 log

        wx.MessageBox('Track(s) Length =  %.4f' % total + ' mm' + '\n' + '\n' + str(i) + ' Track(s) Measured'+'\n'+ '\n'+'Inductance =  %.5f' % (imp) + ' uH', 'Info',  wx.OK | wx.ICON_INFORMATION)
```

The Basic Scheme Of Doing It:
  • Learn where to put the  .py  code and Icon file (use the Kicad Forum)
  • Type the Code shown in Video and Save as  .py
  • Boot up Kicad and set your Plugins to display the Plugins of interest

If you properly placed the Files, Set Plugin for visibility and No Errors in Code, the Icon will display in the PCB's Top Bar

# [track_length_plugin_kicad](https://github.com/charkster/track_length_plugin_kicad)

This Kicad PCB Editor python plugin measures the selected track segments lengths and gives the total length in mm. It also estimates resistance for 1 Oz copper and T = 25C.

This guide was used: https://dev-docs.kicad.org/en/python/pcbnew/

This Youtube view was my inspiration: https://www.youtube.com/watch?v=WjDrvnIFPVY

This on-line resistance calculation tool was used to ensure the plugin's results are accurate:
https://www.allaboutcircuits.com/tools/trace-resistance-calculator/
