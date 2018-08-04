import wx
import wx.propgrid as wxpg

class ProjectTree(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)

class ProjectPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.tree = ProjectTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS)
        self.root = self.tree.AddRoot('Project')
        self.tree.SetItemData(self.root, ('key', 'value'))
        os = self.tree.AppendItem(self.root, 'Camera')
        self.tree.Expand(self.root)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 1, wx.EXPAND)
        self.SetSizer(sizer)

class PropertyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.pg = wxpg.PropertyGridManager(self, style=wxpg.PG_SPLITTER_AUTO_CENTER |
                                                       wxpg.PG_AUTO_SORT |
                                                       wxpg.PG_TOOLBAR)

        self.pg.AddPage("Properties")
        self.pg.Append(wxpg.PropertyCategory("Basic"))
        self.pg.Append(wxpg.StringProperty("Name", value="Camera"))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pg, 1, wx.EXPAND)
        self.SetSizer(sizer)

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        # setup
        wx.Frame.__init__(self, parent, title=title, size=(1024,600))

        # status bar
        self.CreateStatusBar()

        # file menu
        fileMenu = wx.Menu()
        emi = fileMenu.Append(wx.ID_EXIT, "E&xit", "Close the application")

        # help menu
        helpMenu = wx.Menu()
        hmi = helpMenu.Append(wx.ID_ABOUT, "&About...", "About this application")

        # menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

        # panels
        projectPanel = ProjectPanel(self)
        propertyPanel = PropertyPanel(self)
        # clientPanel = GLFrame(self, wx.ID_ANY, 'GL Window')
        clientPanel = wx.Panel(self)

        # sizers
        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox.Add(projectPanel, 1, wx.EXPAND)
        vBox.Add(propertyPanel, 1, wx.EXPAND)

        hBox = wx.BoxSizer(wx.HORIZONTAL)
        hBox.Add(vBox, 1, wx.EXPAND)
        hBox.Add(clientPanel, 2, wx.EXPAND)

        self.SetSizer(hBox)
        self.SetAutoLayout(1)

        # binding/events
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
