# Created by Noman Masood Khan
# Orgranization: Grayhat.pk
# Contact: nomsnkhan07@gmail.com 
# program for perfroming the automated tasks 

import pyautogui
import webbrowser
import time
import pandas as pd
import pyperclip


tidel_url=r"https://listen.tidal.com/"

default_page=r"https://search.brave.com/"

vpn_url=r"https://chrome.google.com/webstore/detail/free-vpn-zenmate-best-vpn/fdcgdnkidjaadafnichfpabhfomcebme"

barve_path=r"C:\Users\HP\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Brave.lnk" 

iproyal='https://chrome.google.com/webstore/detail/iproyal-proxy-manager/gjakohbhfclfjmhhlenfdkldieofkpjl/related'

usernumber=10
        

def create_premium_account():
         
    global usernumber
    
    time.sleep(23)
    
    pyautogui.press("tab")
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    
    file=pd.read_excel("TEST.xlsx")
    
    email=str(file.at[usernumber,"Usuarios (Correos)"])
    
    #if(str(email)=='nan'):
    #   usernumber+=1 
    #   email=file.at[usernumber,"Usuarios (Correos)"] 

    time.sleep(10) 
    
    pyautogui.typewrite(email)
    pyautogui.press('enter')
    time.sleep(2)    
    
    password=file.at[usernumber,'Password']
    
    for w in range(2):
        pyautogui.typewrite(password)
        time.sleep(1)
        pyautogui.press('tab')    
    
    time.sleep(1)
    
    name=file.at[usernumber,'Name']
    
    pyautogui.typewrite(name)
    pyautogui.press('tab')
    
    file['Birthday']=pd.to_datetime(file['Birthday'])
    
    
    birthday=file.at[usernumber,"Birthday"]
    
    #birth_data = re.split(r'[/]',birthday)
    pyautogui.press('enter')
    
    
    day=birthday.day
    month=birthday.month
    year=birthday.year
    
    for w in range(day):
       pyautogui.press('down')
    pyautogui.press('enter')
    
    pyautogui.press("tab")
    pyautogui.press('enter')
    
    pyautogui.sleep(0.5)
    
    for z in range(month):
        pyautogui.press('down')
    pyautogui.press('enter')
    
    year=(2023-year) + 1
    
    pyautogui.press("tab")
    pyautogui.press('enter')
    
    for l in range(year):
        pyautogui.press('down')
    pyautogui.press('enter')
    
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('space')
    
    for m in range(3):
        pyautogui.press('tab')
    pyautogui.press('enter') # Pressed In Sign In button 
        
    time.sleep(8) 
    
    for q in range(4):       # Moving to the HiFi Plus
        pyautogui.press('tab')
    pyautogui.press('enter')
          
    for p in range(2):        # Moving to the Individual Plan
        pyautogui.press('tab')
    
    pyautogui.hotkey('tab','enter') # Opening the individual Plan
    time.sleep(1)
    for o in range(2):          # Selecting the Continue Option 
        pyautogui.press('tab')
    pyautogui.press('enter')
    
    time.sleep(7)
    
    for y in range(2):
        pyautogui.press('tab')    #selecting the name feild 
        
    pyautogui.typewrite(name)  # typing the name feild
    
    credit_card=str(file.at[usernumber,'Credit Card'])
         
    pyautogui.press('tab')
    pyautogui.typewrite(credit_card)
    pyautogui.press('tab')
    
    
    month=str(file.at[usernumber,'Month'])  # Writing the Month and year
    year=str(file.at[usernumber,'Year'])
    
    pyautogui.typewrite(month)
    pyautogui.typewrite('/')
    pyautogui.typewrite(year)
    pyautogui.press('tab')
    
    #cvv=file.at[usernumber,'CVV']

    #pyautogui.press('tab')
    #pyautogui.press('enter')
    
    #usernumber+=1
    
    time.sleep(10)
    
def open_tidal():    
    
    time.sleep(4)
    
    pyautogui.hotkey("ctrl","e")
    pyautogui.press('backspace')
    pyautogui.typewrite(tidel_url)
    pyautogui.press("enter")
    
    time.sleep(4)    

    #create_premium_account()   
 
def add_proxies():
    
    pyautogui.hotkey("ctrl","e")
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.typewrite(iproyal)
    pyautogui.press("enter")            
    time.sleep(10)
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite("Add to Brave")
    
    for i in range(3):
        pyautogui.press("tab")  # cancelling the search menu
    time.sleep(1)
    pyautogui.press("enter")   
    
    pyautogui.press("enter")  # pressing the Add to Brave option 
    
    time.sleep(2)             # waiting for the add to brave menu 
    pyautogui.press("tab")
    
    pyautogui.press("enter")   

    time.sleep(10)            # waiting for the extesnion to get download
    
    pyautogui.press('tab')   # cancel the download notification 
    pyautogui.press('enter')  
    
    time.sleep(3)
    
    pyautogui.press('alt')
    
    time.sleep(1)
    
    for w in range(5):
        pyautogui.press('left')  
        
    pyautogui.press('enter')
    
    for j in range(5):
        pyautogui.press('tab')  # Moving to the selecting proxy manager
    
    pyautogui.press('enter')    #select the proxy manager   
    time.sleep(1)
    
    for k in range(2):          # select the options 
        pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(1)
    
    for l in range(2):           #selecting the create new proxy option 
        pyautogui.press('tab')
    pyautogui.press('enter')
    
    for m in range(3):           # selecting the single proxy option and clicking next 
        pyautogui.press('tab')
    pyautogui.press('enter')
    
    for n in range(5):          # to reach the proxy name writing box
        pyautogui.press('tab')
    
    file= pd.read_excel('TEST.xlsx')
    
    proxy_name = file.at[usernumber,'Pais']
    Ip = str(file.at[usernumber,'IP'])
    
    pyautogui.typewrite(proxy_name)
    
    pyautogui.press('tab')
    
    pyperclip.copy(Ip)
    
    pyautogui.hotkey('ctrl','v')
    
    for o in range(2):
        pyautogui.press('tab')
        
    pyautogui.hotkey('ctrl','c')
    proxy_username = pyperclip.paste()
    #proxy_username= proxy_username
        
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl','c')
    
    proxy_password = pyperclip.paste()
    #proxy_password = proxy_password.strip()    
    
    for p in range(2):
        pyautogui.press('tab') # reaching the save button  
    
    pyautogui.press('enter')
    
    time.sleep(1) 
    
    pyautogui.press('alt')
    for q in range(5):
        pyautogui.press('left')
    pyautogui.press('enter')
    
    time.sleep(1)
    for r in range(5):
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    for s in range(2):
        pyautogui.press('tab')
    pyautogui.press('enter')
    
    time.sleep(3)
    
    open_tidal()
   
def install_extension():
    
    flag=False
    path_img="identify.jpg"
    
    pyautogui.hotkey('ctrl','e')
    pyautogui.press('backspace')
    
    pyautogui.typewrite(vpn_url)
        
    pyautogui.press("enter")
    
    while flag == False:
        if pyautogui.locateOnScreen(path_img):
            flag=True
                    
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite("Add to Brave")
    
    for i in range(3):
        pyautogui.press("tab")
    
    time.sleep(2)
    pyautogui.press("enter")
    
    pyautogui.press("enter")
    
    time.sleep(5)
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    
    path="icon.jpg"
    flag=False
   
    while flag == False:
        if pyautogui.locateOnScreen(path):
            flag=True
    
    add_proxies()
    
    
def register_brave():
    
    webbrowser.register("brave",None,webbrowser.BackgroundBrowser(barve_path))  
    
    brave=webbrowser.get("brave")
       
def open_brave():
    #showing the default page of the brave browserclear
        
    webbrowser.open(default_page)               
    time.sleep(2)
    
def create_profile(profiles):
    
    profile_number=2
    temp=1   
    
    time.sleep(2)
    # Creating Profile window  
    pyautogui.hotkey('shift', 'P')  
    
    for i in range (profiles):
        
        temp= temp+3
        
        time.sleep(2)
        
        for w in range(temp):
            pyautogui.press("tab")
                    
        pyautogui.press("enter")
        
        time.sleep(2)
        
        pyautogui.typewrite("Profile " + str(profile_number)) 
        profile_number+=1
        time.sleep(2)
        
        pyautogui.press("tab")
        pyautogui.press("tab")
        
        pyautogui.press("enter")
        
        #start from here 
        time.sleep(3)
        install_extension()
            
        if i+1 != profiles:
            
            pyautogui.hotkey('ctrl','t')
            
            time.sleep(2)
            
            for j in range(2):
                pyautogui.press('tab')
            
            pyautogui.press("alt")
            pyautogui.press('enter')
            
            for k in range(14):
                pyautogui.press('down')
                
            pyautogui.press('enter')
            
                
def main():
    
    No_of_profiles=0
    
    pyautogui.FAILSAFE=False
    
    with open('Users.txt','r') as file:
        No_of_profiles=int(file.read())
    
    register_brave()

    open_brave()
    
    create_profile(No_of_profiles)
        
    create_premium_account()
    
main()  
