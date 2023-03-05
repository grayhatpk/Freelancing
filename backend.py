class SmartPlug: # smartplug class
    
    """This class represents a smart plug object with the properties and behaviour"""
    
    def __init__(self): 
        """Default Constructor"""
        self.switched_on=False
        self.consumption_rate=0
    
    def toggleSwitch(self):
        """Changing the switched_on vaiable value between True and False""" 
        if(self.switched_on==False):
            self.switched_on=True
        else:
            self.switched_on=False
    def set_switchedOn(self,switch):
        """Setter for the switched_on attribute"""
        self.switched_on=switch
    def get_switch(self):
        """Getter of the switched on attribute"""
        return self.switched_on
    def set_rate(self,rate):
        """Setter for the consumption rate"""
        self.consumption_rate=rate
    def get_rate(self):
        """Getter for the consumption rate"""
        return self.consumption_rate
    def __str__(self): #convert an object to its string representation.
        return f"My Class Instance: Switch State={self.switched_on} , ConsumptionRate={self.consumption_rate} "
    
#last digit 9 therefore Smart Air Fryer Device
# Smart Air Fryer class  is inherited from SmartPlug
    
class SmartAirFryer(SmartPlug):
    """Custom Device based on the Student Number"""         
    def __init__(self):
        """Default Constructor """
        super().__init__()                     # calling out parent class constructor to initialize values 
        self.Cooking_mode="Healthy"
        
    def set_cooking_mode(self,cook_mode):
        """Setter for the cooking_mode attribute"""
        self.Cooking_mode=cook_mode
    
    def get_cooking_mode(self):
        """Getter for the Cooking_mode attribute"""
        return self.Cooking_mode
    
    def __str__(self):
        return f"Smart Air Fryer Class Instance: Switech State{self.switched_on}, Cooking_mode = {self.Cooking_mode} "

class SmartHome():
    """Smart Home Class""" 
    def __init__(self): 
        """Default Constructor initializing the device list """
        self.devices=[]
        
    def getDevices(self):
        """Getter for the devices list"""
        return self.devices
    
    def getDeviceAt(self,index):
        """Getter for getting device at specific index"""
        return self.devices[index]
    
    def addDevice(self,object):
        """Adding new device to Devices List"""
        self.devices.append(object)
    
    def toggleSwitch(self,index):
        """Accessing the Device in the list and chaning it's switch state """
        device=self.devices[index]
        
        if  isinstance(device, SmartPlug):
                device.toggleSwitch()
        elif isinstance(device, SmartAirFryer):
                device.toggleSwitch()    
        
    
    def turnOnAll(self):
        """Switiching all the devices's state to True"""
        for device in self.devices:
            if isinstance(device, SmartPlug):
                device.switched_on=True
            elif isinstance(device, SmartAirFryer):
                device.switchedOn=True
                         
    
    def turnOffAll(self):
        """Turn OFF all the devices in the deice attribute list"""
        for device in self.devices:
            if isinstance(device, SmartPlug):
                    device.switched_on=False
            elif isinstance(device, SmartAirFryer):
                    device.switchedOn=False
                        
    def __str__(self):
        device_list = ""
        for device in self.devices:
            device_list += f"{device.__class__.__name__} - "
            if isinstance(device, SmartPlug):
                    device_list += f"Switch State: {device.get_switch()}, Consumption Rate: {device.get_rate()}\n"
            elif isinstance(device, SmartAirFryer):
                device_list += f"Switched State: {device.get_switchedOn()}, IS in mode : {device.get_cooking_mode()}\n"
            
        return device_list    
                  
def testSmartHome():
    """Function is used for testing the samrt home class by accessing it's method through object"""
    print('-'*100)
    print(' '*30+" THE Test Smart Home Function ")
    print('-'*100)
    #instant of smart home class
    smarthome=SmartHome()
    
    #create two instance of smart plug class
    plug1=SmartPlug()
    plug2=SmartPlug()
    
    #create an instance of the custom smart device
    custom=SmartAirFryer()
    
    plug2.toggleSwitch()
    
    plug2.set_rate(45)
    
    custom.set_cooking_mode("Crispy")
    
    smarthome.addDevice(plug1)
    smarthome.addDevice(plug2)
    smarthome.addDevice(custom)
    
    #print the smarthome object
    print(smarthome)
    
    smarthome.turnOnAll()
    
    print(smarthome)
    
    
def testsmartplug():
    """Testing the Smart plug class by accessing it's methods through class object"""
    print('-'*100)
    print(' '*30+"THE Test Smart Plug Function")
    print('-'*100)
    #creating an instance for the smartplug class
    instance=SmartPlug()
    
    # toggle the plug switch
    instance.toggleSwitch()
    
    #printing the value of the switched on by accessing the accessor
    print (" Switch Value at the moment is {}".format(instance.get_switch()))
    print('  ')
    
    print(" Consumption Rate Right Now:{}".format(instance.get_rate()))
    instance.set_rate(50) #setting consmption rate of our choice btw 0 and 150
    print(" Consumption Rate Right Now:{}".format(instance.get_rate())) #printing again the consumption rate
    print(" ")
    
    print(instance)
    print('-' * 80) # printing the fucntion ending lines
    

def testDevice():
    """Testing the custom smart air fryer class """
    print('-'*100)
    print(' '*30+"THE Smart Device Function")
    print('-'*100)
    
    instance=SmartAirFryer()
    #togling the device 
    instance.toggleSwitch()
    
    print("THe Switch at the moment-> {}".format(instance.get_switch()))
    print('  ')
    print("THe Cooking Mode at the moment-> {}".format(instance.get_cooking_mode()))
    print('  ')
    instance.set_cooking_mode("Defrost")
    #("Healthy", "Defrost" or "Crispy

    print("The Cooking Mode of the Air Fryer after change -> {}".format(instance.get_cooking_mode()))
    print('  ')
    
    print(instance)
        
#calling the mian funtion       

def main():
    testsmartplug()
    testDevice()
    testSmartHome()

main()    