from backend import SmartPlug,SmartAirFryer,SmartHome
import  tkinter as  tk
import subprocess

#instant of the tkinter 
mianWin=tk.Tk()
 #creating an instance of the smart home as global variable 
instance = SmartHome()
    
def setupHome():
    """creates and adds five devices to the SmartHome object and display their properties"""
    counter=0 # local variable for storing total ON buttons   
    
    #Student Number Ends on the 9 SO
    # THe items order is SP, C, SP, SP, C
    
    #creating the items
    plug1=SmartPlug()
    custom1=SmartAirFryer()
    plug2=SmartPlug()
    plug3=SmartPlug()
    custom2=SmartAirFryer()
    
    #adding devices to the smart home object
    instance.addDevice(plug1)
    instance.addDevice(custom1)
    instance.addDevice(plug2)
    instance.addDevice(plug3)
    instance.addDevice(custom2)

    #title for the window
    mianWin.title("Home System")
    #default size for the window when opened
    mianWin.geometry("610x450")
    
    #creating the main frame
    wf=tk.Frame(mianWin,bd=2,border=5,relief="groove",bg="gray")
    wf.pack(side="top",fill="both") #,expand=True)
    
    #heading frame
    head_frame=tk.Frame(wf,bd=2,relief="groove")
    head_frame.grid(row=0,column=0,padx=200,pady=5,sticky="ew") 
    #head_frame.pack(side="top",padx=0,pady=0)
    
    #smart home label 
    label=tk.Label(head_frame,text="Smart Home",font=("Arial",18))
    label.grid(row=0,column=0,padx=0,pady=5)
    
    #turn On button Frame
    button_frame=tk.Frame(wf,bd=2,relief="groove",bg="grey") 
    button_frame.grid(row=1,column=0,padx=4,pady=0,sticky="ew") #ew
     
    #turn On Butoon 
    turn_on=tk.Button(button_frame,text="  Turn all off  ",bd=3,relief="solid") #as the button is pressed, turn on fucntion will be called
    turn_on.grid(row=1,column=0,padx=0,pady=5) #(fill="x",padx=0,pady=0)
    
    #turn Off Button 
    offbutton_frame=tk.Frame(wf,bd=2,relief="groove",bg="grey") 
    offbutton_frame.grid(row=2,column=0,padx=4,pady=0,sticky="ew") 
    
    turn_off=tk.Button(offbutton_frame,text="  Turn all on  ",bd=3,relief="solid")
    turn_off.grid(row=2,column=0,padx=0,pady=5) #pack(side="left",fill="x",padx=0,pady=0) 
    
#creating a new frame for the object1
    obj1=tk.Frame(wf,bd=4,relief="groove",bg="grey")
    obj1.grid(row=3,column=0,columnspan=1,padx=4,pady=0,sticky="ew")
    
    #first device i added is Custom 
    label=tk.Label(obj1,text="Fryer State :{} ,  {}  Cooking Mode ".format(custom1.get_switch(),custom1.get_cooking_mode()))
    label.grid(row=3,column=0,padx=0,pady=5)
    
    #frame for the object1 toggle function 
    toggle1=tk.Frame(obj1,relief="solid")
    toggle1.grid(row=3,column=1,padx=100,pady=3)
    #doing toggling in the parameters                                  #lambda means when the button is pressed,then the run command
    butt1=tk.Button(toggle1,relief="solid",text="Toggle this",command=lambda:label.config(text="Fryer State :{1} ,  {2}  Cooking Mode ".format(custom1.toggleSwitch() , custom1.get_switch(),custom1.get_cooking_mode())))
    butt1.grid(row=3,column=1,padx=0,pady=3)
    
#creating a frame for the object 2
    obj2=tk.Frame(wf,bd=4,relief="groove",bg="grey")
    obj2.grid(row=4,column=0,columnspan=1,padx=4,pady=0,sticky="ew")
    
  #Second Device is the Smart Plug
    label2=tk.Label(obj2,text="Plug :{} ,  {} consumption ".format(plug1.get_switch(),plug1.get_rate()))
    label2.grid(row=4,column=0,padx=0,pady=5)
         
    toggle2=tk.Frame(obj2,relief="solid")
    toggle2.grid(row=4,column=1,padx=175,pady=3) 
    #doing toggling in the parameters
    butt2=tk.Button(toggle2,relief="solid",text="Toggle this",command=lambda:label2.config(text="Plug :{1} ,  {2} consumption  ".format(plug1.toggleSwitch() , plug1.get_switch(),plug1.get_rate())))
    butt2.grid(row=4,column=1,padx=0,pady=3)
    
#creating a frame for the object 3
    obj3=tk.Frame(wf,bd=4,relief="groove",bg="grey")
    obj3.grid(row=5,column=0,columnspan=1,padx=4,pady=0,sticky="ew")
    
  #Third device agian Custom Device 
    label3=tk.Label(obj3,text="Fryer State :{} ,  {}  Cooking Mode ".format(custom2.get_switch(),custom2.get_cooking_mode()))
    label3.grid(row=5,column=0,padx=0,pady=5)
    
  #frame for the object3 toggle function 
    toggle3=tk.Frame(obj3,relief="solid")
    toggle3.grid(row=5,column=1,padx=100,pady=3)
    
   #doing toggling in the parameters
    butt3=tk.Button(toggle3,relief="solid",text="Toggle this",command=lambda:label3.config(text="Fryer State :{1} ,  {2}  Cooking Mode ".format(custom2.toggleSwitch() , custom2.get_switch(),custom2.get_cooking_mode())))
    butt3.grid(row=5,column=1,padx=0,pady=3)
    
#creating frame for the object 4
    obj4=tk.Frame(wf,bd=4,relief="groove",bg="grey")
    obj4.grid(row=6,column=0,columnspan=1,padx=4,pady=0,sticky="ew")
    
 #Fourth Device is the Smart Plug
    label4=tk.Label(obj4,text="Plug :{} ,  {} consumption ".format(plug2.get_switch(),plug2.get_rate()))
    label4.grid(row=6,column=0,padx=0,pady=5)
    
  #frame for the object4 toggle function 
    toggle4=tk.Frame(obj4,relief="solid")
    toggle4.grid(row=6,column=1,padx=175,pady=3) 
    
   #doing toggling when the toggled button is presssed
    butt4=tk.Button(toggle4,relief="solid",text="Toggle this",command=lambda:label4.config(text="Plug :{1} ,  {2} consumption  ".format(plug2.toggleSwitch() , plug2.get_switch(),plug2.get_rate())))
    butt4.grid(row=6,column=1,padx=0,pady=3)
           
        
#Frame for the Object NO.5
    obj5=tk.Frame(wf,bd=4,relief="groove",bg="grey")
    obj5.grid(row=7,column=0,columnspan=1,padx=4,pady=0,sticky="ew")
    
 #Fiveth Device is the Smart Plug
    label5=tk.Label(obj5,text="Plug :{} ,  {} consumption ".format(plug3.get_switch(),plug3.get_rate()))
    label5.grid(row=7,column=0,padx=0,pady=5)
    
  #frame for the object4 toggle function 
    toggle5=tk.Frame(obj5,relief="solid")
    toggle5.grid(row=7,column=1,padx=175,pady=3) 
    
   #doing toggling when the toggled button is presssed
    butt5=tk.Button(toggle5,relief="solid",text="Toggle this",command=lambda:label5.config(text="Plug :{1} ,  {2} consumption  ".format(plug3.toggleSwitch() , plug3.get_switch(),plug3.get_rate())))
    butt5.grid(row=7,column=1,padx=0,pady=3)        
    
#frame for the total devices turned  ON
    obj6=tk.Frame(wf,bd=4,relief="groove",bg="grey")
    obj6.grid(row=8,column=0,columnspan=1,padx=4,pady=0,sticky="ew")
  
  #creating label for the TURNED ON devices variables  
    label6=tk.Label(obj6,text="    NO. of Turned ON Devices: {}   ".format(counter))
    label6.grid(row=8,column=0,padx=90,pady=5)  


    def count(event):
      """ Display the number of devices that are turned on in the home and value should update automatically as devices are toggled"""
      nonlocal counter  # using nonlocal keyword tell counter does not belong to this funtion and it's is declared in the outer fucntion 
      if event.widget==butt1:
        if(custom1.get_switch()==False): #acessing the object of the device and checking it's state
              counter+=1
        else:
              counter-=1
      elif event.widget==butt2:
            if(plug1.get_switch()==False):
                  counter+=1
            else:
                  if(counter>0):
                    counter-=1
      elif event.widget==butt3:
            if(custom2.get_switch()==False):
                  counter+=1
            else:
                  if(counter>0):
                    counter-=1
      elif event.widget==butt4:
           if(plug2.get_switch()==False):
                 counter+=1
           else:
                 if(counter>0):
                    counter-=1
      elif event.widget==butt5:
            if(plug3.get_switch()==False):
                  counter+=1
            else:
                  if(counter>0):
                    counter-=1
          
      label6.config(text="    NO. of Turned ON Devices: {}   ".format(counter))



    butt1.bind("<ButtonPress>",count)
    butt2.bind("<ButtonPress>",count)
    butt3.bind("<ButtonPress>",count)
    butt4.bind("<ButtonPress>",count)
    butt5.bind("<ButtonPress>",count)
    
    def turn_ON(event): # event is hodling information about the button press 
      """This Function is controlling process of Turn On All button. when the button is clicked it turns On all the devices"""
      
      label.config(text="Fryer State :{1} ,  {2}  Cooking Mode ".format(custom1.set_switchedOn(True) , custom1.get_switch(),custom1.get_cooking_mode()))
      label2.config(text="Plug :{1} ,  {2} consumption  ".format(plug1.set_switchedOn(True) , plug1.get_switch(),plug1.get_rate()))
      label3.config(text="Fryer State :{1} ,  {2}  Cooking Mode ".format(custom2.set_switchedOn(True) , custom2.get_switch(),custom2.get_cooking_mode()))            
      label4.config(text="Plug :{1} ,  {2} consumption  ".format(plug2.set_switchedOn(True) , plug2.get_switch(),plug2.get_rate()))  
      label5.config(text="Plug :{1} ,  {2} consumption  ".format(plug3.set_switchedOn(True) , plug3.get_switch(),plug3.get_rate()))    
      label6.config(text="    NO. of Turned ON Devices: {}   ".format(5))
    turn_off.bind("<ButtonPress>",turn_ON)
    
    def turn_OFF(event):
      """This function is Controlling process of Turn All OFF butoon. when the button is clicked it turns all the buttons OFF and sets
      the couter variable to 0"""
      nonlocal counter
      label.config(text="Fryer State :{1} ,  {2}  Cooking Mode ".format(custom1.set_switchedOn(False) , custom1.get_switch(),custom1.get_cooking_mode()))
      label2.config(text="Plug :{1} ,  {2} consumption  ".format(plug1.set_switchedOn(False) , plug1.get_switch(),plug1.get_rate()))
      label3.config(text="Fryer State :{1} ,  {2}  Cooking Mode ".format(custom2.set_switchedOn(False) , custom2.get_switch(),custom2.get_cooking_mode()))            
      label4.config(text="Plug :{1} ,  {2} consumption  ".format(plug2.set_switchedOn(False) , plug2.get_switch(),plug2.get_rate()))  
      label5.config(text="Plug :{1} ,  {2} consumption  ".format(plug3.set_switchedOn(False) , plug3.get_switch(),plug3.get_rate()))    
      label6.config(text="    NO. of Turned ON Devices: {}   ".format(0))
      counter=0
    turn_on.bind("<ButtonPress>",turn_OFF)
     
    mianWin.mainloop()
    
def main():
    setupHome()
    
main()
