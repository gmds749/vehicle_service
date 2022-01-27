class Vehicle:
    def __init__(self,id,veh_no,vt,vm_no,von,ph,dos):
        self.id=id
        self.veh_no=veh_no
        self.vt=vt
        self.vm_no=vm_no
        self.von=von
        self.ph=ph
        self.dos=dos
    def services(self):
        self.amount=input("Enter the amount:")
    def track(self):
        self.new_id=input("Enter the new id:")
        if(self.id==self.new_id):
            print("5% Discount Available:")
        else:
            print("5% Discount not available:")
    def display(self):
        print("VEHICLE_ID  VEHICLE_NUMBER   VEHICLE_TYPE  VEHICLE_MODEL   VEHICLE_OWNERNAME   PHONE_NUMBER   DATE_OF_SERVICE  AMOUNT   NEW_ID")
        print("______________________________________________________________________________________________________________________________")
        print(self.id,'\t',self.veh_no,'\t',self.vt,'\t',self.vm_no,'\t',self.von,'\t',self.ph,'\t',self.dos,'\t',self.amount,'\t',self.new_id)
        print("______________________________________________________________________________________________________________________________")
v=[]
n=int(input("Enter the no of customers:"))
for i in range(n):
    id=int(input("Enter the Id:"))
    veh_no=input("Enter the vehicle number:")
    vt=input("Enter the Vehicle Type:")
    vm_no=input("Enter the Vehicle Model:")
    von=input("Enter the Vehicle Owner name:")
    ph=int(input("Enter the Phone Number:"))
    dos=input("Enter the Date of Service:")
    v.append(Vehicle(id,veh_no,vt,vm_no,von,ph,dos))

for obj in v:
    obj.services()
    obj.track()
    obj.display() 
