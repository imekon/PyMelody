import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1024,600))

        self.CreateStatusBar()

        fileMenu = wx.Menu()
        emi = fileMenu.Append(wx.ID_EXIT, "E&xit", "Close the application")
        
        helpMenu = wx.Menu()
        hmi = helpMenu.Append(wx.ID_ABOUT, "&About...", "About this application")

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, hmi)
        self.Bind(wx.EVT_MENU, self.OnExit, emi)
        
        self.Show(True)

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "Melody Mine music editor", "About Melody Mine", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close(True)

app = wx.App(False)
frame = MainWindow(None, "Melody Mine")
app.MainLoop()
