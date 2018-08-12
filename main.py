import mido

import wx
import wx.aui as wxaui
import wx.propgrid as wxpg

from song import *

from songpanel import *
from patternpanel import *

class ProjectTree(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)

class ProjectPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.tree = ProjectTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS)
        self.root = self.tree.AddRoot('Project')
        self.tree.SetItemData(self.root, ('key', 'value'))
        os = self.tree.AppendItem(self.root, 'Tracks')
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
        self.pg.Append(wxpg.StringProperty("Name", value="Lead"))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pg, 1, wx.EXPAND)
        self.SetSizer(sizer)

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        # setup
        wx.Frame.__init__(self, parent, title=title, size=(1280, 800))

        # song
        self.song = Song()
        
        # icon
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("melody_mine.gif", wx.BITMAP_TYPE_GIF))
        self.SetIcon(icon)

        # status bar
        self.CreateStatusBar()

        # file menu
        fileMenu = wx.Menu()
        newItem = fileMenu.Append(wx.ID_NEW, "&New", "Create new document")
        openItem = fileMenu.Append(wx.ID_OPEN, "&Open...", "Open existing document")
        fileMenu.AppendSeparator()
        importItem = fileMenu.Append(wx.ID_ANY, "&Import...", "Import MIDI file")
        exportItem = fileMenu.Append(wx.ID_ANY, "&Export...", "Export MIDI file")
        fileMenu.AppendSeparator()
        saveItem = fileMenu.Append(wx.ID_SAVE, "&Save", "Save document")
        saveAsItem = fileMenu.Append(wx.ID_SAVEAS, "Save &As...", "Save document with name")
        exitItem = fileMenu.Append(wx.ID_EXIT, "E&xit", "Close the application")

        # edit menu
        editMenu = wx.Menu()
        cutItem = editMenu.Append(wx.ID_CUT, "C&ut")
        copyItem = editMenu.Append(wx.ID_COPY, "&Copy")
        pasteItem = editMenu.Append(wx.ID_PASTE, "&Paste")
        editMenu.AppendSeparator()
        deleteItem = editMenu.Append(wx.NewId(), "&Delete")

        # help menu
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT, "&About...", "About this application")

        # menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(editMenu, "&Edit")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

        # panels
        projectPanel = ProjectPanel(self)
        propertyPanel = PropertyPanel(self)

        # Tag pages
        songPanel = SongPanel(self, self.song)
        patternPanel= PatternPanel(self)
        
        tabPanel = wxaui.AuiNotebook(self)
        tabPanel.AddPage(songPanel, "Song")
        tabPanel.AddPage(patternPanel, "Patterns")

        # sizers
        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox.Add(projectPanel, 1, wx.EXPAND)
        vBox.Add(propertyPanel, 1, wx.EXPAND)

        hBox = wx.BoxSizer(wx.HORIZONTAL)
        hBox.Add(vBox, 1, wx.EXPAND)
        hBox.Add(tabPanel, 5, wx.EXPAND)

        self.SetSizer(hBox)
        self.SetAutoLayout(1)

        # binding/events
        self.Bind(wx.EVT_MENU, self.OnImport, importItem)
        self.Bind(wx.EVT_MENU, self.OnExport, exportItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        
        self.Show(True)

    def OnImport(self, event):
        with wx.FileDialog(self, "Open MIDI file", wildcard="MIDI files (*.mid)|*.mid",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            pathname = fileDialog.GetPath()
            self.song.Import(pathname)

    def OnExport(self, event):
        with wx.FileDialog(self, "Export MIDI file", wildcard="MIDI files (*.mid)|*.mid",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            pathname = fileDialog.GetPath()
            self.song.Export(pathname)

    def OnAbout(self, event):
        with wx.MessageDialog(self, "Melody Mine music editor", "About Melody Mine", wx.OK) as dlg:
            dlg.ShowModal()

    def OnExit(self, e):
        self.Close(True)

app = wx.App(False)
frame = MainWindow(None, "Melody Mine")
app.MainLoop()
