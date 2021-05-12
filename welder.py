import wx  
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="simon",
  database="mydatabase"
)

mycursor = mydb.cursor() 

class Example(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Example, self).__init__(parent, title = title,size = (1000,500)) 
         
      self.InitUI() 
		
   def InitUI(self):    
      topPanel = wx.Panel(self)
      pn1 = wx.Panel(topPanel, -1, pos=(0,0),size=(500,50))
      pn2 = wx.Panel(topPanel, -1, pos=(0,50),size=(500,50))
      pn3 = wx.Panel(topPanel, -1, pos=(0,100),size=(1000,400))
      pn4 = wx.Panel(topPanel, -1, pos=(0,400),size=(500,100))
      self.st = wx.StaticText(pn1, label ="Allo, Erick. Est-ce que tu as de symptomes")
      self.merci = wx.StaticText(pn4, label ="")

      self.styesA = wx.StaticText(pn3, label ="no", pos = (450,0))
      self.stnoA = wx.StaticText(pn3, label ="oui", pos = (480,0))
      self.stA = wx.StaticText(pn3, label ="Sensation d'etre fievreux, d'avoir de frissons comme lors d'une grippe,", pos = (10,50))
      self.stA2 = wx.StaticText(pn3, label ="ou une fievre mesuree avec une temperature prise par la bouche", pos = (10,65))
      self.stA3 = wx.StaticText(pn3, label ="egale ou superior a 38,1 C (100.6 F)", pos = (10,80))
      self.stB = wx.StaticText(pn3, label ="Perte sudain de l'orodat sans congestion nasale (nez bouche)", pos = (10,110))
      self.stB2 = wx.StaticText(pn3, label ="avec ou sans perte de gout", pos = (10,125))
      self.stC = wx.StaticText(pn3, label ="Toux recente ou une toux chronique agravee depuis peu", pos = (10,155))
      self.stD = wx.StaticText(pn3, label ="Difficulte a respirer ou essoufflement", pos = (10,185))
      self.stE = wx.StaticText(pn3, label ="Mal de gorge", pos = (10,215))
      self.stF = wx.StaticText(pn3, label ="Nez qui coule ou une congestion nasale (nez bouche) de cause inconnue", pos = (10,245))
      self.rb11 = wx.RadioButton(pn3, 11, pos = (450,50), style = wx.RB_GROUP) 
      self.rb12 = wx.RadioButton(pn3, 12, pos = (480,50)) 
      self.rb21 = wx.RadioButton(pn3, 21,pos = (450,110), style =wx.RB_GROUP) 
      self.rb22 = wx.RadioButton(pn3, 22, pos = (480,110)) 
      self.rb31 = wx.RadioButton(pn3, 31,pos = (450,155), style = wx.RB_GROUP) 
      self.rb32 = wx.RadioButton(pn3, 32,pos = (480,155)) 
      self.rb41 = wx.RadioButton(pn3, 41,pos = (450,185), style = wx.RB_GROUP) 
      self.rb42 = wx.RadioButton(pn3, 42,pos = (480,185)) 
      self.rb51 = wx.RadioButton(pn3, 51,pos = (450,215), style = wx.RB_GROUP) 
      self.rb52 = wx.RadioButton(pn3, 52,pos = (480,215)) 
      self.rb61 = wx.RadioButton(pn3, 61,pos = (450,245), style = wx.RB_GROUP) 
      self.rb62 = wx.RadioButton(pn3, 62,pos = (480,245)) 
      self.styesB = wx.StaticText(pn3, label ="no", pos = (900,0))
      self.stnoB = wx.StaticText(pn3, label ="oui", pos = (930,0))
      self.stG = wx.StaticText(pn3, label ="Mal de ventre", pos = (550,50))
      self.stH = wx.StaticText(pn3, label ="Nausees (maux de coeur) ou vomissements", pos = (550,80))
      self.stI = wx.StaticText(pn3, label ="Diarrhee", pos = (550,110))
      self.stJ = wx.StaticText(pn3, label ="Fatigue intense inhabituelle sans raison evidente", pos = (550,140))
      self.stK = wx.StaticText(pn3, label ="Perte d'appetit importante", pos = (550,170))
      self.stL = wx.StaticText(pn3, label ="Doleurs musculaires generalisees ou courbatures", pos = (550,200))
      self.stL2 = wx.StaticText(pn3, label ="inhabituelles (non liees a un effort phyusique)", pos = (550,215))
      self.stM = wx.StaticText(pn3, label ="Mal de tete inhabituel", pos = (550,245))
      self.rb71 = wx.RadioButton(pn3, 71, pos = (900,50), style = wx.RB_GROUP) 
      self.rb72 = wx.RadioButton(pn3, 72, pos = (930,50)) 
      self.rb81 = wx.RadioButton(pn3, 81,pos = (900,110), style =wx.RB_GROUP) 
      self.rb82 = wx.RadioButton(pn3, 82, pos = (930,110)) 
      self.rb91 = wx.RadioButton(pn3, 91,pos = (900,155), style = wx.RB_GROUP) 
      self.rb92 = wx.RadioButton(pn3, 92,pos = (930,155)) 
      self.rb101 = wx.RadioButton(pn3, 101,pos = (900,185), style = wx.RB_GROUP) 
      self.rb102 = wx.RadioButton(pn3, 102,pos = (930,185)) 
      self.rb111 = wx.RadioButton(pn3, 111,pos = (900,215), style = wx.RB_GROUP) 
      self.rb112 = wx.RadioButton(pn3, 112,pos = (930,215)) 
      self.rb121 = wx.RadioButton(pn3, 121,pos = (900,245), style = wx.RB_GROUP) 
      self.rb122 = wx.RadioButton(pn3, 122,pos = (930,245))
      self.rb131 = wx.RadioButton(pn3, 131,pos = (900,245), style = wx.RB_GROUP) 
      self.rb132 = wx.RadioButton(pn3, 132,pos = (930,245))


      self.Center() 
      self.Show(True)    

      self.symp = wx.Button(pn2, -1, label = 'Pas de symptomes',pos = (50,0)) 
      self.cont = wx.Button(pn2, -1, label = 'Quelques symptomes',pos = (200,0)) 
      self.envoyer = wx.Button(pn2, -1, label = 'Envoyer',pos = (370,0)) 
      self.Bind(wx.EVT_BUTTON, self.PasSymptomes, self.symp)
      self.Bind(wx.EVT_BUTTON, self.Quelques, self.cont)
      self.Bind(wx.EVT_BUTTON, self.Sending, self.envoyer)

      self.rb11.Show(False)
      self.rb12.Show(False)
      self.rb21.Show(False)
      self.rb22.Show(False)
      self.rb31.Show(False)
      self.rb32.Show(False)
      self.rb41.Show(False)
      self.rb42.Show(False)
      self.rb51.Show(False)
      self.rb52.Show(False)
      self.rb61.Show(False)
      self.rb62.Show(False)
      self.rb71.Show(False)
      self.rb72.Show(False)
      self.rb81.Show(False)
      self.rb82.Show(False)
      self.rb91.Show(False)
      self.rb92.Show(False)
      self.rb101.Show(False)
      self.rb102.Show(False)
      self.rb111.Show(False)
      self.rb112.Show(False)
      self.rb121.Show(False)
      self.rb122.Show(False)
      self.rb131.Show(False)
      self.rb132.Show(False)
      self.styesA.Show(False)
      self.stnoA.Show(False)
      self.styesB.Show(False)
      self.stnoB.Show(False)
      self.stA.Show(False)
      self.stA2.Show(False)
      self.stA3.Show(False)
      self.stB.Show(False)
      self.stB2.Show(False)
      self.stC.Show(False)
      self.stD.Show(False)
      self.stE.Show(False)
      self.stF.Show(False)
      self.stG.Show(False)
      self.stH.Show(False)
      self.stI.Show(False)
      self.stJ.Show(False)
      self.stK.Show(False)
      self.stL.Show(False)
      self.stL2.Show(False)
      self.stM.Show(False)
      self.envoyer.Disable()

   def PasSymptomes(self, e): 
      mycursor.execute("INSERT INTO test (name, general, sympA, sympB, sympC, sympD, sympE, sympF, sympG, sympH, sympI, sympJ, sympK, sympL, sympM) VALUES ('Erick Diaz', false, false, false, false, false, false, false, false, false, false, false, false, false, false)")
      mydb.commit()
      mydb.close()
      self.merci.SetLabel("Merci")
      self.symp.Disable()
      self.cont.Disable()

   def Quelques(self, e): 
      self.rb11.Show(True)
      self.rb12.Show(True)
      self.rb21.Show(True)
      self.rb22.Show(True)
      self.rb31.Show(True)
      self.rb32.Show(True)
      self.rb41.Show(True)
      self.rb42.Show(True)
      self.rb51.Show(True)
      self.rb52.Show(True)
      self.rb61.Show(True)
      self.rb62.Show(True)
      self.rb71.Show(True)
      self.rb72.Show(True)
      self.rb81.Show(True)
      self.rb82.Show(True)
      self.rb91.Show(True)
      self.rb92.Show(True)
      self.rb101.Show(True)
      self.rb102.Show(True)
      self.rb111.Show(True)
      self.rb112.Show(True)
      self.rb121.Show(True)
      self.rb122.Show(True)
      self.rb131.Show(True)
      self.rb132.Show(True)
      self.styesA.Show(True)
      self.stnoA.Show(True)
      self.styesB.Show(True)
      self.stnoB.Show(True)
      self.stA.Show(True)
      self.stA2.Show(True)
      self.stA3.Show(True)
      self.stB.Show(True)
      self.stB2.Show(True)
      self.stC.Show(True)
      self.stD.Show(True)
      self.stE.Show(True)
      self.stF.Show(True)
      self.stG.Show(True)
      self.stH.Show(True)
      self.stI.Show(True)
      self.stJ.Show(True)
      self.stK.Show(True)
      self.stL.Show(True)
      self.stL2.Show(True)
      self.stM.Show(True)
      self.symp.Disable()
      self.cont.Disable()
      self.envoyer.Enable()
   
   def Sending(self, e): 
      sympA=False
      sympB=False
      sympC=False
      sympD=False
      sympE=False
      sympF=False
      sympG=False
      sympH=False
      sympI=False
      sympJ=False
      sympK=False
      sympL=False
      sympM=False
      if self.rb12.GetValue()==True: sympA=True
      if self.rb22.GetValue()==True: sympB=True
      if self.rb32.GetValue()==True: sympC=True
      if self.rb42.GetValue()==True: sympD=True
      if self.rb52.GetValue()==True: sympE=True
      if self.rb62.GetValue()==True: sympF=True
      if self.rb72.GetValue()==True: sympG=True
      if self.rb82.GetValue()==True: sympH=True
      if self.rb92.GetValue()==True: sympI=True
      if self.rb102.GetValue()==True: sympJ=True
      if self.rb112.GetValue()==True: sympK=True
      if self.rb122.GetValue()==True: sympL=True
      if self.rb132.GetValue()==True: sympM=True
      insert_stmt = ("INSERT INTO test (name, general, sympA, sympB, sympC, sympD, sympE, sympF, sympG, sympH, sympI, sympJ, sympK, sympL, sympM) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
      data = ('Erick Diaz', True, sympA, sympB, sympC, sympD, sympE, sympF, sympG, sympH, sympI, sympJ, sympK, sympL, sympM)
      mycursor.execute(insert_stmt, data)
      mydb.commit()
      self.merci.SetLabel("Merci")
      mydb.close()
      self.symp.Disable()
      self.cont.Disable()
      self.envoyer.Disable()
      
ex = wx.App() 
Example(None,'Atlantis') 
ex.MainLoop()