import wx
class myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, size=(325,530))
        

        #SCHEME PANELS
        self.scheme1 = wx.Panel(self, size=(60, 60))
        self.scheme1.SetBackgroundColour((0,0,0))

        self.scheme2 = wx.Panel(self, size=(60, 60))
        self.scheme2.SetBackgroundColour((0,0,0))

        self.scheme3=wx.Panel(self, size=(60, 60))
        self.scheme3.SetBackgroundColour((0,0,0))

        self.scheme4=wx.Panel(self, size=(60, 60))
        self.scheme4.SetBackgroundColour((0,0,0))
        
        self.scheme5=wx.Panel(self, size=(60, 60))
        self.scheme5.SetBackgroundColour((0,0,0))
            

        #GRID SETUP
        self.myGridSizer = wx.GridBagSizer(2, 2) #args = gap spacing
        self.myGridSizer.SetEmptyCellSize((0, 0))

        #SCHEME PANEL POSITIONING
        self.myGridSizer.Add(self.scheme1, pos=(0, 0))#, span=(10,10), flag=wx.EXPAND)
        self.myGridSizer.Add(self.scheme2, pos=(0, 1))#, span=(4,4), flag=wx.ALL)
        self.myGridSizer.Add(self.scheme3, pos=(0, 2))#, span=(4,4), flag=wx.ALL)
        self.myGridSizer.Add(self.scheme4, pos=(0, 3))#, span=(4,4), flag=wx.ALL)
        self.myGridSizer.Add(self.scheme5, pos=(0, 4))#, span=(4,4), flag=wx.ALL)
        

        #AVERAGE PANEL
        self.average1=wx.Panel(self, size=(308, 308)) #"8" compensates for 2p gap between colors
        self.average1.SetBackgroundColour((0,0,0))

        #PRIMARY PANEL POSITIONING
        self.myGridSizer.Add(self.average1, pos=(1, 0), span=(5,5))#, flag=wx.ALL)
        
        
        #?
        self.SetSizer(self.myGridSizer)
        

        #TEXT
        #Color 1 ground panel
        self.textRGB=wx.Panel(self, size=(60, 22))
        self.textRGB.SetBackgroundColour("grey")
        self.myGridSizer.Add(self.textRGB, pos=(6, 0))#, span=(4,4), flag=wx.ALL)
        
        #text application
        self.text1 = wx.StaticText(self.textRGB, label="Color 1", style=2, size=(50, -1))
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.BOLD, wx.NORMAL)
        self.text1.SetFont(font)

        self.titleSizer = wx.BoxSizer()
        self.titleSizer.Add(self.text1, flag=wx.CENTER|wx.LEFT|wx.ALIGN_RIGHT, border=10)
        self.textRGB.SetSizer(self.titleSizer)

        self.SetSizer(self.myGridSizer)

        #Color 2 ground panel
        self.textRGB=wx.Panel(self, size=(60, 22))
        self.textRGB.SetBackgroundColour("grey")
        self.myGridSizer.Add(self.textRGB, pos=(7, 0))#, span=(4,4), flag=wx.ALL)
        
        #text application
        self.text1 = wx.StaticText(self.textRGB, label="Color 2", style=2, size=(50, -1))
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.BOLD, wx.NORMAL)
        self.text1.SetFont(font)

        self.titleSizer = wx.BoxSizer()
        self.titleSizer.Add(self.text1, flag=wx.CENTER|wx.LEFT|wx.ALIGN_RIGHT, border=10)
        self.textRGB.SetSizer(self.titleSizer)

        self.SetSizer(self.myGridSizer)

        #Color 3 ground panel
        self.textRGB=wx.Panel(self, size=(60, 22))
        self.textRGB.SetBackgroundColour("grey")
        self.myGridSizer.Add(self.textRGB, pos=(8, 0))#, span=(4,4), flag=wx.ALL)
        
        #text application
        self.text1 = wx.StaticText(self.textRGB, label="Color 3", style=2, size=(50, -1))
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.BOLD, wx.NORMAL)
        self.text1.SetFont(font)

        self.titleSizer = wx.BoxSizer()
        self.titleSizer.Add(self.text1, flag=wx.CENTER|wx.LEFT|wx.ALIGN_RIGHT, border=10)
        self.textRGB.SetSizer(self.titleSizer)

        self.SetSizer(self.myGridSizer)

        #Color 4 ground panel
        self.textRGB=wx.Panel(self, size=(60, 22))
        self.textRGB.SetBackgroundColour("grey")
        self.myGridSizer.Add(self.textRGB, pos=(9, 0))#, span=(4,4), flag=wx.ALL)
        
        #text application
        self.text1 = wx.StaticText(self.textRGB, label="Color 4", style=2, size=(50, -1))
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.BOLD, wx.NORMAL)
        self.text1.SetFont(font)

        self.titleSizer = wx.BoxSizer()
        self.titleSizer.Add(self.text1, flag=wx.CENTER|wx.LEFT|wx.ALIGN_RIGHT, border=10)
        self.textRGB.SetSizer(self.titleSizer)

        self.SetSizer(self.myGridSizer)
        
        #Color 5 ground panel
        self.textRGB=wx.Panel(self, size=(60, 22))
        self.textRGB.SetBackgroundColour("grey")
        self.myGridSizer.Add(self.textRGB, pos=(10, 0))#, span=(4,4), flag=wx.ALL)
        
        #text application
        self.text1 = wx.StaticText(self.textRGB, label="Color 5", style=2, size=(50, -1))
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.BOLD, wx.NORMAL)
        self.text1.SetFont(font)

        self.titleSizer = wx.BoxSizer()
        self.titleSizer.Add(self.text1, flag=wx.CENTER|wx.LEFT|wx.ALIGN_RIGHT, border=10)
        self.textRGB.SetSizer(self.titleSizer)

        self.SetSizer(self.myGridSizer)

        '''
        #Average ground panel
        self.textRGB=wx.Panel(self, size=(60, 22))
        self.textRGB.SetBackgroundColour("grey")
        self.myGridSizer.Add(self.textRGB, pos=(6, 4), span=(1,1))#, flag=wx.ALL)
        
        #text application
        self.text1 = wx.StaticText(self.textRGB, label="Color 1", style=2, size=(50, -1))
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.BOLD, wx.NORMAL)
        self.text1.SetFont(font)

        self.titleSizer = wx.BoxSizer()
        self.titleSizer.Add(self.text1, flag=wx.CENTER|wx.LEFT|wx.ALIGN_RIGHT, border=10)
        self.textRGB.SetSizer(self.titleSizer)

        self.SetSizer(self.myGridSizer)
        '''

        #DATA ENTRY
        #Color 1 entry
        self.entry1 = wx.TextCtrl(self,-1,value=u"13,13,13")
        self.myGridSizer.Add(self.entry1, pos=(6,1), span=(1,4))#, wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry1)
           
        #Color 2 entry
        self.entry2 = wx.TextCtrl(self,-1,value=u"242,242,242")
        self.myGridSizer.Add(self.entry2, pos=(7,1), span=(1,4))#, wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry2)

        #Color 3 entry
        self.entry3 = wx.TextCtrl(self,-1,value=u"191,144,4")
        self.myGridSizer.Add(self.entry3, pos=(8,1), span=(1,4))#, wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry3)

        #Color 4 entry
        self.entry4 = wx.TextCtrl(self,-1,value=u"217,103,4")
        self.myGridSizer.Add(self.entry4, pos=(9,1), span=(1,4))#, wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry4)

        #Color 5 entry
        self.entry5 = wx.TextCtrl(self,-1,value=u"191,4,4")
        self.myGridSizer.Add(self.entry5, pos=(10,1), span=(1,4))#, wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry5)

        self.Show(True)


    #UPDATE METHODS        
    def OnButtonClick(self, event):
        #self.label.SetLabel(self.entry.GetValue() + "(A)")
        #self.entry.SetFocus()
        #self.entry.SetSetSelection(-1, -1)
        #self.set_Color1(0,0,0)
        #self.set_Color1(0,0,0)
        #self.Refresh()
        print "button called"

    def OnPressEnter(self,event):
        self.set_Color1Value()
        self.set_Color2Value()
        self.set_Color3Value()
        self.set_Color4Value()
        self.set_Color5Value()
        self.Refresh()
        print "Enter Call"


    #COLOR 1 METHOD
    def set_Color1Value(self):
        value = str(self.entry1.GetValue())
        valueList = value.split(",")
        R = int(valueList[0])
        G = int(valueList[1])
        B = int(valueList[2])

        self.scheme1.SetBackgroundColour((R,G,B))

        return R, G, B
        #print "this was called"

    #COLOR 2 METHOD
    def set_Color2Value(self):
        value = str(self.entry2.GetValue())
        valueList = value.split(",")
        R = int(valueList[0])
        G = int(valueList[1])
        B = int(valueList[2])

        self.scheme2.SetBackgroundColour((R,G,B))

        return R, G, B
        #print "this was called"

    #COLOR 3 METHOD
    def set_Color3Value(self):
        value = str(self.entry3.GetValue())
        valueList = value.split(",")
        R = int(valueList[0])
        G = int(valueList[1])
        B = int(valueList[2])

        self.scheme3.SetBackgroundColour((R,G,B))

        return R, G, B
        #print "this was called"

    #COLOR 4 METHOD
    def set_Color4Value(self):
        value = str(self.entry4.GetValue())
        valueList = value.split(",")
        R = int(valueList[0])
        G = int(valueList[1])
        B = int(valueList[2])

        self.scheme4.SetBackgroundColour((R,G,B))

        return R, G, B
        #print "this was called"

    #COLOR 5 METHOD
    def set_Color5Value(self):
        value = str(self.entry5.GetValue())
        valueList = value.split(",")
        R = int(valueList[0])
        G = int(valueList[1])
        B = int(valueList[2])

        self.scheme5.SetBackgroundColour((R,G,B))

        return R, G, B
        #print "this was called"

    def set_AvgColor(self):
        R_Avg = (region.set_Color1Value()[0] + region.set_Color2Value()[0] + region.set_Color3Value()[0] + region.set_Color4Value()[0] + region.set_Color5Value()[0]) / 5
        print R_Avg
        print type(R_Avg)

        G_Avg = (region.set_Color1Value()[1] + region.set_Color2Value()[1] + region.set_Color3Value()[1] + region.set_Color4Value()[1] + region.set_Color5Value()[1]) / 5
        print G_Avg
        print type(G_Avg)

        B_Avg = (region.set_Color1Value()[2] + region.set_Color2Value()[2] + region.set_Color3Value()[2] + region.set_Color4Value()[2] + region.set_Color5Value()[2]) / 5
        print B_Avg
        print type(B_Avg)

        self.average1.SetBackgroundColour((R_Avg,G_Avg,B_Avg))



#MAIN LOOP
if __name__ == "__main__":
    app = wx.App()
    region = myframe()
    region.Show()
    
    #set color calls
    region.set_Color1Value()
    region.set_Color2Value()
    region.set_Color3Value()
    region.set_Color4Value()
    region.set_Color5Value()

    #average call
    region.set_AvgColor()

    region.Refresh()
    app.MainLoop()