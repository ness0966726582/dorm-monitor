import Main as um


#讀取文字檔路徑
_sheet_Key_="./參數調整/creds.json"#金鑰路徑
txtPath=["./參數調整/1_URL.txt","./參數調整/2_ID.txt","./參數調整/3_PAGE.txt","./參數調整/4_CELL.txt","./參數調整/5_Path.txt"]

sh="" #金鑰打包API
URL_Info =[] #網址
ID_Info = [] #GoogleID
Page_Info = []  #分頁
Cell_Info=[] #更新的位置
Path_Info=[] #更新的路徑


#讀取文字當內容
def BTN__Read_All_txt_Info__():
    global URL_Info,ID_Info,Page_Info,Cell_Info,Path_Info
    
    filename = open(txtPath[0],'r',encoding='utf-8')        
    URL_Info = str(filename.read())  
    filename = open(txtPath[1],'r',encoding='utf-8')        
    ID_Info = str(filename.read())    
    filename = open(txtPath[2],'r',encoding='utf-8')        
    Page_Info = str(filename.read())    
    filename = open(txtPath[3],'r',encoding='utf-8')        
    Cell_Info = str(filename.read())
    filename = open(txtPath[4],'r',encoding='utf-8')        
    Path_Info = str(filename.read())
    
#自訂開啟瀏覽器
def BTN__Open_URL__():
    import webbrowser
    webbrowser.open(URL_Info)
    
#上傳授權與金鑰需上Google cloud platfrom啟用API與服務
def __GoogleService_Key__():
    global sh
    import gspread
    from gspread.models import Cell
    from oauth2client.service_account import ServiceAccountCredentials 
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(_sheet_Key_, scope) #權限金鑰
    client = gspread.authorize(creds)           #使用金鑰
    sh = client.open_by_key(ID_Info).worksheet(Page_Info) #指定頁面 ID + Page_Info   
    

#發送GOOGLE 指定Cell 更新
def Update():
    
    myList = um.Get_Data()
    #sh.clear()
    sh.update(Cell_Info, myList)
    print(myList)


##########################
#執行準備
##########################
BTN__Read_All_txt_Info__()
#BTN__Open_URL__()
__GoogleService_Key__()


##########################
#發送
##########################
Update()
