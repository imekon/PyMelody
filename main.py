try:
    from OpenGL.GL import *
except ImportError:
    raise ImportError, "Required dependency OpenGL not present"

try:
    import wx
    from wx import glcanvas
except ImportError:
    raise ImportError, "Required dependency wx.glcanvas not present"

import wx.propgrid as wxpg

class GLFrame(wx.Frame):
    def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
                 name='glframe'):
        style = wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE

        super(GLFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.GLinitialised = False
        attribList = (glcanvas.WX_GL_RGBA, glcanvas.WX_GL_DOUBLEBUFFER, glcanvas.WX_GL_DEPTH_SIZE, 24)

        self.canvas = glcanvas.GLCanvas(self, attribList=attribList)

        self.canvas.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.canvas.Bind(wx.EVT_SIZE, self.OnSize)
        self.canvas.Bind(wx.EVT_PAINT, self.OnPaint)

    def GetGLExtents(self):
        return self.canvas.GetClientSize()

    def SwapBuffer(self):
        self.canvas.SwapBuffers()

    def OnEraseBackground(self, event):
        pass

    def OnSize(self, event):
        if self.canvas.GetContext():
            self.Show()
            self.canvas.SetCurrent()
            size = self.GetGLExtents()
            self.OnReshape(size.width, size.height)
            self.canvas.Refresh(False)
        event.Skip()

    def OnPaint(self, event):
        self.canvas.SetCurrent()
        if not self.GLinitialised:
            self.OnInitGL()
            elf.GLinitialised = True

        self.OnDraw()
        event.Skip()

    def OnInitGL(self):
        glClearColor(1, 1, 1, 1)

    def OnReshape(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-0.5, 0.5, -0.5, 0.5, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def OnDraw(self, *args, **kwargs):
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_TRIANGLES)
        glColor(0, 0, 0)
        glVertex(-.25, -.25)
        glVertex(.25, -.25)
        glVertex(0, .25)
        glEnd()

        self.SwapBuffers()

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
