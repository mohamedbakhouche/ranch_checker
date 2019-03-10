import c4d, os , sys
from c4d import gui, plugins, bitmaps
import json
import urllib2

sys.path.append(os.path.dirname(__file__))
from modules.consolegroup import Console_Group

PLUGIN_ID = 1051394


GET_RENDER_ENGINE = 10000
GRP_SUB = 10001
GRP_SUB2 = 10002
GRP_DYNAMIC = 10003
IDS_SETTINS = 10004
IDS_RENDERSUPPORT = 10006
GRP_SUBGROUP = 10005
IDS_ARCHIVE = 10007
GRP_LOGO = 10008
IDS_PLUGINSUPPORT = 10009
IDS_ARNOLD_SUPPORT = 10010
IDS_CORONA_SUPPORT = 10011
IDS_VRAY_SUPPORT = 10012
IDS_OCTANE_SUPPORT = 10013
IDS_PRORENDER_SUPPORT = 10014
IDS_HDRISTUDIORIG_SUPPORT = 10015
IDS_XPARTICLCES_SUPPORT = 10016
IDS_REALFLOW_SUPPORT = 10017
IDS_STUDIORIG_SUPPORT = 10018   
IDS_REDSHIFT_SUPPORT = 10019  
IDS_CONSOLE = 10020
IDS_BTN_LOGIN = 10021
GRP_LOGIN = 10022
IDS_BTN_RANCH = 10023
GRP_DYNAMIC_LOGIN = 10024
LOGIN_USER_PASSWORD = 10025
IDS_SUBMIT_LOGIN = 10026



class Check_Group(c4d.gui.GeUserArea):
	g_HDialog = False
	
	def __init__(self, RV, cicon, fixe):

		self.RV = RV
		self.cicon = cicon
		self.fixe = fixe
		self.bc = c4d.BaseContainer()
		self.Color_D = c4d.Vector(218/255, 43/255, 43/255)# Red
		self.Color_R = c4d.Vector(68, 68, 70)
		#self.Color_B = c4d.Vector(173, 196, 214)
		self.Color_W = c4d.Vector(232/255, 241/255, 248/255)
		self.Color_G = c4d.Vector(59, 59, 61)
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

	

	def DrawMsg(self, x1, y1, x2, y2, msg):

		self.OffScreenOn() 
		self.SetClippingRegion(x1, y1, x2, y2) 
		
		self.DrawSetPen(c4d.Vector(0.3,0.3,0.3)) 
		self.DrawRectangle(x1, y1, x2, y2)

		self.DrawSetPen(c4d.Vector(0.231, 0.231, 0.239)) 
		self.DrawRectangle(x1, 0, x2, 25)

		self.DrawSetPen(c4d.Vector(0.4, 0.631, 0.686)) 
		self.DrawRectangle(x1, 0, 5, 25)
		
		self.DrawSetFont(c4d.FONT_DEFAULT)
		self.DrawSetTextCol(c4d.Vector(0.909, 0.945, 0.972), c4d.Vector(0.231, 0.231, 0.239)) 
		self.DrawText(self.RV, 45, 6)

		if self.fixe == True:
			self.DrawSetFont(c4d.FONT_BOLD)
			self.DrawSetTextCol(c4d.Vector(0.909, 0.945, 0.972), c4d.Vector(0.007, 0.650, 0.462)) 
			self.DrawText("  OK  ", self.w - 45, 5)
		else:
			self.DrawSetFont(c4d.FONT_BOLD)
			self.DrawSetTextCol(c4d.Vector(0.909, 0.945, 0.972), c4d.Vector(0.007, 0.650, 0.462)) 
			self.DrawText("  Fixe  ", self.w - 45, 5)

		self.DrawSetPen(c4d.Vector(0.231, 0.231, 0.239)) 
		path, file = os.path.split(__file__)
		bc = c4d.BaseContainer()
		bmp = bitmaps.BaseBitmap()
		w, h = 10, 10

		bmp.InitWith(os.path.join(path, "res", "icon/" + self.cicon + ".png"))
  		bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True)  

		self.DrawBitmap(bmp, 15, 2, 20, 20, 0, 0, 25, 25, c4d.BMP_ALLOWALPHA)

		self.DrawSetPen(c4d.Vector(0.231, 0.231, 0.239)) 
		self.DrawRectangle(10, 650, x2, 750)
		#self.ScrollArea(500, 0, 0, 0, 0, 0)
	
	def InputEvent(self, msg):
		action = c4d.BaseContainer(c4d.BFM_ACTION)  
		action.SetLong(c4d.BFM_ACTION_ID, self.GetId())

		if isinstance(msg, c4d.BaseContainer):
			if msg.GetLong(c4d.BFM_INPUT_DEVICE) == c4d.BFM_INPUT_MOUSE:
				self.SendParentMessage(action)

				#base = self.Local2Global()
				#print base
				#if base:
					#x = msg.GetLong(c4d.BFM_INPUT_X) - base['x']
					#print x
					#y = msg.GetLong(c4d.BFM_INPUT_Y) - base['y']
					#print y
					#pid = self.GetID(x, y)
					#print pid
					#if pid <= self.Host.PatternSize:
						#self.Host.Pattern[pid] = not self.Host.Pattern[pid]
						#self.Redraw()

		return True

		

##################################################################################################

class RanchChecker(gui.GeDialog):

	def CreateLayout(self):

		self.SetTitle("Ranch Checker")

		self.GroupBeginInMenuLine()
		self.GroupBorderSpace(0, 0, 10, 0)
		self.MenuSubBegin("Settings")
		self.MenuAddString(434343, "Register")
		self.MenuSubEnd()

		self.MenuSubBegin("Help")
		self.MenuAddString(534343, "help")
		self.MenuSubEnd()
		
		path, file = os.path.split(__file__)
		bc = c4d.BaseContainer()
		bmp = bitmaps.BaseBitmap()
		w, h = 10, 10
		bmp.InitWith(os.path.join(path, "res", "icon/ranch.png"))
  		bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True)  
  		bitmap_Button = self.AddCustomGui(IDS_BTN_RANCH, c4d.CUSTOMGUI_BITMAPBUTTON, "", c4d.BFV_CENTER, w, h, bc)
  		bitmap_Button.SetImage(bmp, True)

		bmp.InitWith(os.path.join(path, "res", "icon/login.png"))
  		bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True)  
  		bitmap_Button = self.AddCustomGui(IDS_BTN_LOGIN, c4d.CUSTOMGUI_BITMAPBUTTON, "", c4d.BFV_CENTER, w, h, bc)
  		bitmap_Button.SetImage(bmp, True)

		self.GroupEnd()


		self.GroupBegin(GRP_SUB,c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, 1, 3, "",c4d.BFV_GRIDGROUP_ALLOW_WEIGHTS)#GRP_SUB

		self.GroupBegin(GRP_LOGO, c4d.BFH_CENTER|c4d.BFV_CENTER|c4d.BFH_SCALEFIT, 1,1, "")#GRP_LOGO

		bmp.InitWith(os.path.join(path, "res", "header.png"))
  		bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True)  
  		bitmap_Button = self.AddCustomGui(11111, c4d.CUSTOMGUI_BITMAPBUTTON, "", c4d.BFH_SCALEFIT, w, h, bc)
  		bitmap_Button.SetImage(bmp, True)
		self.GroupEnd()#GRP_LOGO

		#self.GroupBegin(GRP_DYNAMIC_LOGIN,c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, 1, 2,"",c4d.BFV_GRIDGROUP_ALLOW_WEIGHTS)#. GRP_DYNAMIC_LOGIN. ###

		self.GroupBegin(GRP_LOGIN, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT , 2, 1,"",c4d.BFV_GRIDGROUP_ALLOW_WEIGHTS, 700)# GRP_LOGIN ######
		

		self.GroupEnd()# GRP_LOGIN#####

		self.GroupBegin(GRP_SUB2, c4d.BFV_BOTTOM|c4d.BFH_RIGHT, 2,0,"")#GRP_SUB2###
		self.GroupBorderSpace(10, 5, 10, 10)
		self.AddButton(GET_RENDER_ENGINE, c4d.BFH_RIGHT , 120, 14, "Check Project")
		self.AddButton(IDS_ARCHIVE, c4d.BFH_RIGHT , 120, 14, "Archive")
		self.GroupEnd()#GRP_SUB2###
		
		#self.GroupEnd()#. GRP_DYNAMIC_LOGIN. ###
		self.GroupEnd()#GRP_SUB

		return True

	def InitValues(self):
		self.RanchGroup()
		self.SettingProjectGroup()

		return True

	def SettingProjectGroup(self):

		self.LayoutFlushGroup(GRP_DYNAMIC)

		self.GroupBegin(90, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, 1,2, "")###
		self.GroupBorderSpace(10, 10, 10, 10)
		#self.GroupBorderNoTitle(c4d.BORDER_THIN_IN)
		#self.ScrollGroupBegin(50,  c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_VERT, 5, 200)

		self.GroupBegin(100, c4d.BFH_SCALEFIT,2,2 , "Assets" )###
		self.GroupBorderSpace(5, 5, 5, 5)
		self.GroupBorder(c4d.BORDER_ROUND)
		self.AddCheckbox(101, c4d.BFV_TOP|c4d.BFH_LEFT, 0,0, "Separate assets from archive")
		self.AddStaticText(107, c4d.BFV_TOP|c4d.BFH_LEFT, 280,0, "")
		self.AddStaticText(108, c4d.BFV_TOP|c4d.BFH_LEFT, 0,0, "Folder name")
		self.AddEditText(111, c4d.BFH_SCALEFIT, 0, 0, 1)
		self.GroupEnd()

		self.GroupBegin(102, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT,3,1 , "" )#archive distination##
		self.GroupBorderSpace(0, 5, 0, 0)
		self.AddCheckbox(104, c4d.BFV_TOP|c4d.BFH_LEFT, 0,0, "Archive destination")
		self.AddEditText(211, c4d.BFH_SCALEFIT, 0, 0, 1)
		self.AddButton(30, c4d.BFV_TOP|c4d.BFH_LEFT  , 18, 12, "...")
		
		self.GroupEnd()

		self.GroupEnd()#

		self.LayoutChanged(GRP_DYNAMIC)


	def RanchGroup(self):
		path, file = os.path.split(__file__)
		bc = c4d.BaseContainer()
		bmp = bitmaps.BaseBitmap()
		w, h = 10, 10

		self.LayoutFlushGroup(GRP_LOGIN)
		

		self.GroupBorderSpace(10, 10, 10, 10)
		self.GroupBegin(30, c4d.BFV_TOP|c4d.BFH_LEFT, 1,0,"", 50 )###
		self.GroupBorderSpace(0, 0, 5, 0)
		bmp.InitWith(os.path.join(path, "res", "settings.png"))
  		bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True) 
  		bc.SetString(c4d.BITMAPBUTTON_TOOLTIP, "Setting") 

  		Settings_Button = self.AddCustomGui(IDS_SETTINS, c4d.CUSTOMGUI_BITMAPBUTTON, "Setting", c4d.BFH_SCALEFIT, w, h, bc)
  		Settings_Button.SetImage(bmp, True)

		bmp.InitWith(os.path.join(path, "res", "render.png"))
  		bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True)  
  		bc.SetString(c4d.BITMAPBUTTON_TOOLTIP, "Our render support in the current cinema 4d") 
  		Render_Button = self.AddCustomGui(IDS_RENDERSUPPORT, c4d.CUSTOMGUI_BITMAPBUTTON, "Render support", c4d.BFH_SCALEFIT, w, h, bc)
  		Render_Button.SetImage(bmp, True)

		bmp.InitWith(os.path.join(path, "res", "plugins.png"))
  		bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True) 
  		bc.SetString(c4d.BITMAPBUTTON_TOOLTIP, "Our plugins support in the current cinema 4d")  
  		Plugins_Button = self.AddCustomGui(IDS_PLUGINSUPPORT, c4d.CUSTOMGUI_BITMAPBUTTON, "Plugins support", c4d.BFH_SCALEFIT, w, h, bc)
  		Plugins_Button.SetImage(bmp, True)

		bmp.InitWith(os.path.join(path, "res", "console.png"))
  		bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True) 
  		bc.SetString(c4d.BITMAPBUTTON_TOOLTIP, "Your settings in the console")  
  		console_Button = self.AddCustomGui(IDS_CONSOLE, c4d.CUSTOMGUI_BITMAPBUTTON, "Console", c4d.BFH_SCALEFIT, w, h, bc)
  		console_Button.SetImage(bmp, True)

		self.GroupEnd()###
		
		self.GroupBegin(40, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT ,4,1,"")###
		#self.GroupBorderNoTitle(c4d.BORDER_THIN_IN)

		self.GroupBegin(GRP_DYNAMIC, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT , 5,1,"")#dynamic group##
		self.GroupBorderNoTitle(c4d.BORDER_THIN_IN)
		self.GroupEnd()#dynamic group##

		self.GroupEnd()###

		self.GroupEnd()##
		
		#######
  		
		self.LayoutChanged(GRP_LOGIN)
		

	def LogIn_Group(self):
		
		self.LayoutFlushGroup(GRP_LOGIN)
		self.GroupBegin(LOGIN_USER_PASSWORD, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT , 1,1,"" )
		self.GroupBorderNoTitle(c4d.BORDER_THIN_IN)
		self.GroupBorderSpace(20, 20, 20, 20)

		self.GroupBegin(10020, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT , 2,3, "" )
		self.AddStaticText(188, c4d.BFV_CENTER|c4d.BFH_CENTER, 0,0, "Username : ")
		self.AddEditText(1009, c4d.BFV_CENTER|c4d.BFH_CENTER, 220, 0,  0)
		self.AddStaticText(1010, c4d.BFV_CENTER|c4d.BFH_CENTER, 0,0, "Password : ")
		self.AddEditText(1011, c4d.BFV_CENTER|c4d.BFH_CENTER, 220, 0, 1)
		self.AddButton(IDS_SUBMIT_LOGIN, c4d.BFH_RIGHT , 120, 14, "Submit")
		self.GroupEnd()

		self.GroupEnd()
		self.LayoutChanged(GRP_LOGIN)
	
	def ListPluginSupport(self):

		c4dVersion = c4d.GetC4DVersion()
		Plugins_Support = []
		Plugins_SV = []
		Render_Engine_Version = json.loads(urllib2.urlopen('http://mohbakh.pythonanywhere.com/pluginversion/').read())

		for i in Render_Engine_Version:
			splitRenderVersion = i["plugin_version_name"].split("/")

			if splitRenderVersion[0] == "C4D":
				if splitRenderVersion[1][1:] == str(c4dVersion)[:-3]:
					Plugins_Support.append(splitRenderVersion[2])
					Plugins_SV.append(splitRenderVersion[3])

		self.LayoutFlushGroup(GRP_DYNAMIC)
		self.GroupBegin(10022, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, 1,2,"" )

		self.GroupBegin(10033, c4d.BFH_SCALEFIT, 0,0,"" )
		self.AddStaticText(300, c4d.BFH_SCALEFIT, 0,20, "  Our Plugins supported in the current cinema 4d", c4d.BORDER_WITH_TITLE_BOLD|c4d.BORDER_THIN_OUT)
		self.GroupEnd()
		self.ScrollGroupBegin(12321323, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT,  c4d.SCROLLGROUP_AUTOVERT | c4d.SCROLLGROUP_VERT, 100, 10)

		self.GroupBegin(10044, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, 5,0,"" )
		self.GroupBorderSpace(10, 10, 10, 10)

		for i in range(len(Plugins_Support)):
			self.GroupBegin(100+i, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, 0,2,"" )
			
			bc = c4d.BaseContainer()
			bmp = bitmaps.BaseBitmap()
			w, h = 10, 10
			bmp.InitWith(os.path.join(path, "res", "icon/plugins/" + str(Plugins_Support[i]) + ".png"))
			bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True)  
			Arnold1_Button = self.AddCustomGui(200+i, c4d.CUSTOMGUI_BITMAPBUTTON, "", c4d.BFH_FIT, w, h, bc)
			Arnold1_Button.SetImage(bmp, True)
			self.AddStaticText(300+i, c4d.BFV_TOP|c4d.BFH_LEFT, 0,0, str(Plugins_Support[i]) + " " + str(Plugins_SV[i]))
			self.GroupEnd()
		self.GroupEnd()
		self.GroupEnd()
		self.LayoutChanged(GRP_DYNAMIC)
		

	def CheckCinemaVersion(self):
		CinemaVersion = ""
		Software_v = json.loads(urllib2.urlopen('http://mohbakh.pythonanywhere.com/softwareVersion/').read())

		versionCurrent = c4d.GetC4DVersion()

		softwareList = []

		for i in range(len(Software_v)):
			softwareList.append(Software_v[i]["software_version"])
		for i in softwareList:
			Version = i.split("/")
			if Version[1] == str(versionCurrent):
				CinemaVersion = "Cinema 4d version : R " + str(versionCurrent) + " Supported"
			else:
				CinemaVersion = "Cinema 4d version : R "+ str(versionCurrent) +  " not Supported"

		return CinemaVersion

	def ListRenderSuppurte(self):
		#path, file = os.path.split(__file__)
		#RenderSupport_path = os.path.join(path, "res", "icon")
		#ListIcon_InFolder = os.listdir(RenderSupport_path)

		c4dVersion = c4d.GetC4DVersion()
		Render_Support = []
		Render_SV = []
		Render_Engine_Version = json.loads(urllib2.urlopen('http://mohbakh.pythonanywhere.com/renderengienv/').read())

		for i in Render_Engine_Version:
			splitRenderVersion = i["renEngVer_name"].split("/")

			if splitRenderVersion[0] == "C4D":
				if splitRenderVersion[1][1:] == str(c4dVersion)[:-3]:
					Render_Support.append(splitRenderVersion[2])
					Render_SV.append(splitRenderVersion[3])

		self.LayoutFlushGroup(GRP_DYNAMIC)
		self.GroupBegin(10022, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, 1,2,"" )

		self.GroupBegin(10033, c4d.BFH_SCALEFIT, 0,0,"" )
		self.AddStaticText(300, c4d.BFH_SCALEFIT, 0,20, "  Our render supported in the current cinema 4d", c4d.BORDER_WITH_TITLE_BOLD|c4d.BORDER_THIN_OUT)
		self.GroupEnd()
		self.ScrollGroupBegin(12321323, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_VERT | c4d.SCROLLGROUP_AUTOVERT, 100, 10)
		self.GroupBegin(10044, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, 4,0,"" )

		self.GroupBorderSpace(10, 10, 10, 10)

		for i in range(len(Render_Support)):
			self.GroupBegin(100+i, c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT, 0,2,"" )
			
			bc = c4d.BaseContainer()
			bmp = bitmaps.BaseBitmap()
			w, h = 10, 10
			bmp.InitWith(os.path.join(path, "res", "icon/render/" + str(Render_Support[i]) + ".png"))
			bc.SetBool(c4d.BITMAPBUTTON_BUTTON, True)  
			Arnold1_Button = self.AddCustomGui(200+i, c4d.CUSTOMGUI_BITMAPBUTTON, "", c4d.BFH_FIT, w, h, bc)
			Arnold1_Button.SetImage(bmp, True)
			self.AddStaticText(300+i, c4d.BFV_TOP|c4d.BFH_LEFT, 0,0, str(Render_Support[i]) + " " + str(Render_SV[i]))
			self.GroupEnd()

		self.GroupEnd()
		self.GroupEnd()
		self.LayoutChanged(GRP_DYNAMIC)
		
		#return  Render_V_Support

	def ConsoleResult(self):
		self.LayoutFlushGroup(GRP_DYNAMIC)

		self.Console_Group = Console_Group()

		area = self.AddUserArea(123123, c4d.BFH_SCALEFIT |c4d.BFV_SCALEFIT)    
		self.AttachUserArea(self.Console_Group, area)
		self.LayoutChanged(GRP_DYNAMIC)

	def CheckResult(self):
		self.check = self.CheckeRenderVersion()
		self.LayoutFlushGroup(GRP_DYNAMIC)

		self.GroupBegin(100999, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT , 1,2,"")

		cicon = ""
		fixe = True
		if self.check == " render engine is not supported":
			cicon = "error"
			fixe = False
		else:
			cicon = "ok"
			fixe = True

		self.Check_Group = Check_Group(self.check, cicon, fixe)
		#self.Check_Group2 = Check_Group(self.check, cicon, fixe)

		self.ScrollGroupBegin(12321323, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_VERT | c4d.SCROLLGROUP_AUTOVERT, 100, 10) 
		
		self.AddUserArea(143123, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT )    
		self.AttachUserArea(self.Check_Group, 143123)

		#self.AddUserArea(15, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT )    
		#self.AttachUserArea(self.Check_Group2, 15)

		self.GroupEnd()
		self.LayoutChanged(GRP_DYNAMIC)
		 

	def CheckeRenderVersion(self):
		V_render = ""

		renderengine_v = json.loads(urllib2.urlopen('http://mohbakh.pythonanywhere.com/renderengienv/').read())

		d = c4d.documents.GetActiveDocument()
		rd = d.GetActiveRenderData()
		render_engine = rd[c4d.RDATA_RENDERENGINE]

		render_idList = []
		render_NameList = []

		for i in range(len(renderengine_v)):
			render_idList.append(renderengine_v[i]["renEngVer_id"])
			render_NameList.append(renderengine_v[i]["renEngVer_name"])

		fk = 0

		for i in render_idList:
			if int(i) == render_engine:
				r = render_NameList[fk].split("/")
				rf = r[2]

				V_render =   str(rf) + " supported"
				break
			else:
				V_render = " render engine is not supported" 
				
			fk = fk+1

		return V_render

	def FixRenderGroup(self):
		self.LayoutFlushGroup(GRP_DYNAMIC)
		self.GroupBegin(100989, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT , 1,2,"")
 
		self.GroupBegin(100979, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1,1,"")
		self.GroupSpace(20, 20)
		self.AddStaticText(300, c4d.BFH_SCALEFIT, 0,20, "  Fixe render to support : ", c4d.BORDER_WITH_TITLE_BOLD|c4d.BORDER_THIN_OUT)
		self.GroupEnd()

		self.GroupBegin(100969, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT , 1,1,"")
		self.AddStaticText(300, c4d.BFH_SCALEFIT, 0,20, "  Fixe render : ")
		self.GroupEnd()


		self.GroupEnd()
		self.LayoutChanged(GRP_DYNAMIC)


	def Command(self, id, msg):

		if id == 143123:
			self.FixRenderGroup()

		if id == GET_RENDER_ENGINE:
			self.CheckResult()
			self.check = self.CheckeRenderVersion()
			self.soft = self.CheckCinemaVersion()

			print self.soft
			print self.check

		if id == IDS_SETTINS:
			self.SettingProjectGroup()

		if id == IDS_RENDERSUPPORT:
			self.ListRenderSuppurte()

		if id == IDS_PLUGINSUPPORT:
			self.ListPluginSupport()

		if id == IDS_CONSOLE:
			self.ConsoleResult()

		if id == IDS_BTN_LOGIN:
			self.LogIn_Group()

		if id == IDS_BTN_RANCH:
			self.RanchGroup()
			self.SettingProjectGroup()

		return True


class RanchCommand(c4d.plugins.CommandData):

	dialog = None

	def Execute(self, doc):
		if self.dialog == None:
			self.dialog = RanchChecker()
		return self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=PLUGIN_ID, defaulth=700, defaultw=400)

	def RestoreLayout(self, secref):

		return self.dialog.Restore(PLUGIN_ID, secref)

if __name__ == "__main__":

	path, file = os.path.split(__file__)
	resource = c4d.plugins.GeResource()
	bmp = bitmaps.BaseBitmap()
	bmp.InitWith(os.path.join(path, "res", "RanchChecker.tiff"))
	plugins.RegisterCommandPlugin(PLUGIN_ID, "RanchChecker", 0,  bmp, "RanchChecker", RanchCommand())




