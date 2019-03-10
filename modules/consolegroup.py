import c4d, os
from c4d import gui, plugins, bitmaps
import json
import urllib2


PLUGIN_ID = 1051394
class Console_Group(c4d.gui.GeUserArea):
	
	def __init__(self):
		self.bc = c4d.BaseContainer()
		self.Color_G = c4d.Vector(59, 59, 61)
		self.Color_R = c4d.Vector(68, 68, 70)
		#self.Color_B = c4d.Vector(173, 196, 214)
		self.Color_W = c4d.Vector(232, 241, 248)
		self.Color_D = c4d.Vector(102, 161, 175)
		self.Color_S = c4d.Vector(2, 166, 118)
		self.w = self.GetWidth()
		self.h = self.GetHeight()
		self.drawMap = bitmaps.GeClipMap()
	
	def Sized(self, w, h):
		self.w, self.h = w, h
		self.drawMap.Destroy()
		self.drawMap.Init(self.w, self.h)
		return
    
	def GetMinSize(self):
		return self.w, self.h

	def Cinema_version_Area(self):
		version = ["Cinema 4D Prime", "Bodypaint 3D", "Cinema 4D Studio"]
		os_version  = ["Windows", "Unix", "OSX"]

		_version = c4d.GetC4DVersion()
		_cinema_type = c4d.GeGetVersionType()
		_os_version = c4d.GeGetCurrentOS()

		self.drawMap.SetFont(self.bc, 14)

		self.drawMap.SetColor(self.Color_G.x, self.Color_G.y, self.Color_G.z)
		self.drawMap.FillRect(5, 0, self.GetWidth(), 25)

		self.drawMap.SetColor(self.Color_D.x, self.Color_D.y, self.Color_D.z)
		self.drawMap.FillRect(0, 0, 5, 25)

		self.drawMap.SetColor(self.Color_W.x, self.Color_W.y, self.Color_W.z)
		
		self.drawMap.TextAt(25,7,  version[_cinema_type] + " R" +  str(_version) + " " + os_version[_os_version])

		self.drawMap.SetOffset(0, 28)

	def Render_Engine_Area(self):
		d = c4d.documents.GetActiveDocument()
		rd = d.GetActiveRenderData()
		render_engine = rd[c4d.RDATA_RENDERENGINE]

		self.drawMap.SetFont(self.bc, 14)

		self.drawMap.SetColor(self.Color_R.x, self.Color_R.y, self.Color_R.z)		
		self.drawMap.FillRect(5, 0, self.GetWidth(), 25)

		self.drawMap.SetColor(self.Color_D.x, self.Color_D.y, self.Color_D.z)
		self.drawMap.FillRect(0, 0, 5, 25)

		if render_engine == 0:
			_render_Engine = "Standerd "
		elif render_engine == 1023342:
			_render_Engine = "Physical "
		elif render_engine == 1:
			_render_Engine = "Sofrware OpenGL "
		elif render_engine == 300001061:
			_render_Engine = "Hardware OpenGL "
		elif render_engine == 1037639:
			_render_Engine = "ProRender "
		elif render_engine == 1016630:
			_render_Engine = "CineMan "

		CurrentRender_wight = self.drawMap.TextWidth("Current render engine : ")
		self.drawMap.SetColor(self.Color_W.x, self.Color_W.y, self.Color_W.z)
		self.drawMap.TextAt(25, 7 -28,  "Current render engine : " )
		self.drawMap.SetFont(self.bc, 18)
		self.drawMap.SetColor(self.Color_D.x, self.Color_D.y, self.Color_D.z)

		self.drawMap.TextAt(25 + CurrentRender_wight, 5 -28, _render_Engine)###str(render_engine))
		Support_wight = self.drawMap.TextWidth(_render_Engine)
		self.drawMap.SetFont(self.bc, 16)
		self.drawMap.SetColor(self.Color_S.x, self.Color_S.y, self.Color_S.z)
		self.drawMap.TextAt(25 + CurrentRender_wight + Support_wight, 5 -28, "Supported ")###str(render_engine))

		self.drawMap.SetOffset(0, 56)

	def Render_Resolution(self):
		d = c4d.documents.GetActiveDocument()
		rd = d.GetActiveRenderData()
		render_Resolution_X = rd[c4d.RDATA_XRES_VIRTUAL]
		render_Resolution_Y = rd[c4d.RDATA_YRES_VIRTUAL]

		self.drawMap.SetColor(self.Color_G.x, self.Color_G.y, self.Color_G.z)
		self.drawMap.FillRect(5, 0, self.GetWidth(), 25)

		self.drawMap.SetColor(self.Color_D.x, self.Color_D.y, self.Color_D.z)
		self.drawMap.FillRect(0, 0, 5, 25)
		
		self.drawMap.SetFont(self.bc, 14)
		_V = str(render_Resolution_X)[:-2] 
		_H = str(render_Resolution_Y)[:-2]

		Resolution_wight = self.drawMap.TextWidth("render resolution : ")
		self.drawMap.SetColor(self.Color_W.x, self.Color_W.y, self.Color_W.z)
		self.drawMap.TextAt(25, 7 -56 ,  "render resolution : " )##+ _V + " X " + _H + " Pixels" )
		
		self.drawMap.SetFont(self.bc, 18)
		self.drawMap.SetColor(self.Color_D.x, self.Color_D.y, self.Color_D.z)
		self.drawMap.TextAt(25 + Resolution_wight, 5 -56, _V + " X " + _H)##+ _V + " X " + _H + " Pixels" )

		ResV_wight = self.drawMap.TextWidth(_V)
		ResH_wight = self.drawMap.TextWidth(_H)
		ResX_wight = self.drawMap.TextWidth(" X ")
		ResTotal = Resolution_wight + ResV_wight + ResH_wight + ResX_wight
		self.drawMap.SetFont(self.bc, 14)
		self.drawMap.SetColor(self.Color_W.x, self.Color_W.y, self.Color_W.z)
		self.drawMap.TextAt(25 + ResTotal, 7 -56 ,  " Pixels" )##+ _V + " X " + _H + " Pixels" )
		
		self.drawMap.SetOffset(0, 84)

	def FrameRange(self):
		d = c4d.documents.GetActiveDocument()
		rd = d.GetActiveRenderData()
		frame_range = rd[c4d.RDATA_FRAMESEQUENCE]

		sequence = ""
		if frame_range == 0:
			sequence = "Manual"
		elif frame_range == 1:
			sequence = "Current frame"
		elif frame_range == 2:
			sequence = "All frame"

		self.drawMap.SetColor(self.Color_R.x, self.Color_R.y, self.Color_R.z)	
		self.drawMap.FillRect(5, 0, self.GetWidth(), 25)

		self.drawMap.SetColor(self.Color_D.x, self.Color_D.y, self.Color_D.z)
		self.drawMap.FillRect(0, 0, 5, 25)

		frame_range_wight = self.drawMap.TextWidth("Frame range : " )
		self.drawMap.SetColor(self.Color_W.x, self.Color_W.y, self.Color_W.z)
		self.drawMap.TextAt(25, 7 -84 ,  "Frame range : " )
		
		self.drawMap.SetFont(self.bc, 18)
		self.drawMap.SetColor(self.Color_D.x, self.Color_D.y, self.Color_D.z)
		self.drawMap.TextAt(25 + frame_range_wight, 5 -84, sequence)

		self.drawMap.SetOffset(0, 112)

	def OutPoutName(self):
		d = c4d.documents.GetActiveDocument()
		rd = d.GetActiveRenderData()
		outpout_save = rd[c4d.RDATA_PATH]

		outpout = ""
		if outpout_save == "":
			outpout = " /"
		elif outpout_save != None:
			outpout = outpout_save

		self.drawMap.SetColor(self.Color_G.x, self.Color_G.y, self.Color_G.z)	
		self.drawMap.FillRect(5, 0, self.GetWidth(), 25)

		self.drawMap.SetColor(self.Color_D.x, self.Color_D.y, self.Color_D.z)
		self.drawMap.FillRect(0, 0, 5, 25)

		save_path_wight = self.drawMap.TextWidth("Save path : ")
		self.drawMap.SetColor(self.Color_W.x, self.Color_W.y, self.Color_W.z)
		self.drawMap.SetFont(self.bc, 14)
		self.drawMap.TextAt(25, 7 -112 ,  "Save path : " )
		
		self.drawMap.SetFont(self.bc, 18)
		self.drawMap.SetColor(self.Color_D.x, self.Color_D.y, self.Color_D.z)
		self.drawMap.TextAt(save_path_wight, 5 -112, outpout)



	def DrawMsg(self, x1, y1, x2, y2, msg):
		self.DrawSetTextCol(self.Color_G, self.Color_R)
		self.OffScreenOn()
		self.drawMap.BeginDraw()
		self.drawMap.SetColor(80, 80, 80)
		self.drawMap.FillRect(0, 0, self.GetWidth(), self.GetHeight())

		self.drawMap.BeginDraw()

		self.Cinema_version_Area()
		self.Render_Engine_Area()
		self.Render_Resolution()
		self.FrameRange()
		self.OutPoutName()

		self.drawMap.EndDraw()

		self.DrawBitmap(self.drawMap.GetBitmap(), 0, 0, self.GetWidth(), self.GetHeight(),0, 0, self.GetWidth(), self.GetHeight(),c4d.BMP_NORMAL)
