import wx

PATTERN_LEFT_MARGIN = 30
PATTERN_TOP_MARGIN = 25
PATTERN_CELL_WIDTH = 24
PATTERN_CELL_HEIGHT = 14
PATTERN_CELL_STEPS = 32
PATTERN_CELL_NOTES = 35

class PatternPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, e):
        dc = wx.PaintDC(self)

        darkGray = wx.Pen("#AAAAAA")
        lightGray = wx.Pen("#CCCCCC")

        
        for y in range(0, PATTERN_CELL_NOTES + 1):
            
            if y % 7 == 0:
                dc.SetPen(darkGray)
            else:        
                dc.SetPen(lightGray)
                
            dc.DrawLine(PATTERN_LEFT_MARGIN,
                        PATTERN_TOP_MARGIN + y * PATTERN_CELL_HEIGHT,
                        PATTERN_LEFT_MARGIN + PATTERN_CELL_STEPS * PATTERN_CELL_WIDTH,
                        PATTERN_TOP_MARGIN + y * PATTERN_CELL_HEIGHT)

        for x in range(0, PATTERN_CELL_STEPS + 1):

            if x % 4 == 0:
                dc.SetPen(darkGray)
            else:        
                dc.SetPen(lightGray)
                
            dc.DrawLine(PATTERN_LEFT_MARGIN + x * PATTERN_CELL_WIDTH,
                        PATTERN_TOP_MARGIN,
                        PATTERN_LEFT_MARGIN + x * PATTERN_CELL_WIDTH,
                        PATTERN_TOP_MARGIN + PATTERN_CELL_NOTES * PATTERN_CELL_HEIGHT)
                
    def OnSize(self, e):
        self.Refresh()
        
