import mysql.connector
import wx  

connection = mysql.connector.connect(host='localhost',
                                         database='mydatabase',
                                         user='root',
                                         password='simon')

class Example(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Example, self).__init__(parent, title = title,size = (500,500)) 
         
      self.InitUI() 
		
   def InitUI(self):  
      
      topPanel = wx.Panel(self)
     
      self.st = wx.StaticText(topPanel, label ="Base de donnees")
      self.user = wx.TextCtrl(topPanel,pos = (50,50))
      self.look = wx.Button(topPanel, -1, label = 'Aller',pos = (50,100)) 
      self.Bind(wx.EVT_BUTTON, self.Search, self.look)
      self.look = wx.Button(topPanel, -1, label = 'Aller2',pos = (150,100)) 
      self.Bind(wx.EVT_BUTTON, self.Symptom, self.look)
      self.look = wx.Button(topPanel, -1, label = 'Aller3',pos = (250,100)) 
      self.Bind(wx.EVT_BUTTON, self.Report, self.look)
      self.result = wx.StaticText(topPanel, label ="", pos = (50,150))

      self.Center() 
      self.Show(True)    

     
   def Search(self, e): 
        welders = ['Pierre Cox', 'Miranda Shaffer', 'Brand Krammer', 'Alice Ramos', 'Erick Diaz']  
        missing=''
        date=self.user.GetValue()
        data=date+'%'
        sql_select_Query = "select name from test where date like %s"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (data,))
    # get all records
        response=[]
        records = cursor.fetchall()
        for row in records:
           response.append(row[0])

        for x in welders:
           if x not in response:
              missing=missing+x+'\n'

        self.result.SetLabel(missing)

   def Symptom(self, e): 
        general=''
        date=self.user.GetValue()
        data=date+'%'
        sql_select_Query = "select name from test where date like %s and general=true"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (data,))
    # get all records
        records = cursor.fetchall()
        for row in records:
           general=general+row[0]+'\n'

        self.result.SetLabel(general)

   def Report(self, e): 
        final=''
        date=self.user.GetValue()
        data=date+'%'
        sql_select_Query = "select * from test where date like %s and general=true"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (data,))
    # get all records
        records = cursor.fetchall()
        for row in records:
           final=final+row[0]+'\n'
           if row[2]==1: 
              final=final+'- Sensation d\'etre fievreux...'+'\n'
           if row[3]==1: 
              final=final+'- Perte sudain de l\'orodat...'+'\n'
           if row[4]==1: 
              final=final+'- Toux recente ou une toux chronique...'+'\n'
           if row[5]==1: 
              final=final+'- Difficulte a respirer ou essoufflement'+'\n'
           if row[6]==1: 
              final=final+'- Mal de gorge'+'\n'
           if row[7]==1: 
              final=final+'- Nez qui coule...'+'\n'
           if row[8]==1: 
              final=final+'- Mal de ventre'+'\n'
           if row[9]==1: 
              final=final+'- Nausees ou vomissements'+'\n'
           if row[10]==1: 
              final=final+'- Diarrhee'+'\n'
           if row[11]==1: 
              final=final+'- Fatigue intense...'+'\n'
           if row[12]==1: 
              final=final+'- Perte d\'appetit importante'+'\n'
           if row[13]==1: 
              final=final+'- Doleurs musculaires...'+'\n'
           if row[7]==1: 
              final=final+'- Mal de tete inhabituel'+'\n'

        f = open("file.txt", "w")
        print(final, file=f)
        f.close()
      
ex = wx.App() 
Example(None,'Atlantis') 
ex.MainLoop()

