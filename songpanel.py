import wx

SONG_LEFT_MARGIN = 80
SONG_TOP_MARGIN = 30
SONG_BLOCK_WIDTH = 30
SONG_BLOCK_HEIGHT = 22
SONG_BLOCK_GAP = 3

class SongPanel(wx.Panel):
    def __init__(self, parent, song):
        wx.Panel.__init__(self, parent)

        self.song = song
        self.font = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, 'Courier 10 Pitch')

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.SetFont(self.font)

        dc.SetPen(wx.Pen("#000000"))
        dc.SetBrush(wx.Brush("#FFFFFF"))

        for x in range(0, 32):
            dc.DrawLabel(str(x + 1),
                         wx.Rect(SONG_LEFT_MARGIN + (SONG_BLOCK_WIDTH + SONG_BLOCK_GAP) * x,
                         SONG_TOP_MARGIN - 22, SONG_BLOCK_WIDTH, SONG_BLOCK_HEIGHT), wx.ALIGN_CENTER | wx.ALIGN_TOP)

        for y in range(0, 16):
            track = self.song.FindTrack(y + 1)
            if track != None:
                dc.DrawLabel(track.name, wx.Rect(SONG_BLOCK_GAP, SONG_TOP_MARGIN + (SONG_BLOCK_HEIGHT + SONG_BLOCK_GAP) * y,
                                                 SONG_LEFT_MARGIN - SONG_BLOCK_GAP * 2, SONG_BLOCK_HEIGHT), wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
                
            for x in range(0, 32):
                dc.DrawRectangle(SONG_LEFT_MARGIN + (SONG_BLOCK_WIDTH + SONG_BLOCK_GAP) * x,
                                 SONG_TOP_MARGIN + (SONG_BLOCK_HEIGHT + SONG_BLOCK_GAP) * y,
                                 SONG_BLOCK_WIDTH,
                                 SONG_BLOCK_HEIGHT)

    def OnSize(self, e):
        self.Refresh()
