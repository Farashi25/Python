from datetime import datetime
class Patient(object):
    def __init__ (self,name, allergies, bedNumber):        
        self.id = id(self)
        self.name = name
        self.allergies = allergies
        self.bedNumber = bedNumber
        self. time = datetime.now()

    def display(self):
        print "Patient#:{}: Patient's Name: {} Known Allergies: ({}) Bed Assignment'{}'".format(self.id,self.name, self.allergies, self.bedNumber)
        return self

patient1 =Patient('Farashi','No Known Allergies','10162002')
patient1.display()


class Hospital(object):
    def __init__(self,hospitalName):
        self.patients =[]
        self.hospitalName = hospitalName
        self. hospital_capacity = 3
        self.hospital_num_patient = 0  
    def admit(self,name, allergies,bedNumber):
        self.patients.append(Patient(name,allergies,bedNumber))
        self.hospital_num_patient +=1
        if self.hospital_num_patient >= self.hospital_capacity:
          print ('patient can NOT be admitted, the hospital is full')
        else:
          print ('Admission is Complete: CONFIRMED')
        return self
    def discharge(self, name):
        for patient in self.patients:
            if patient.name == name:
                self.patients.remove(patient)
                self.hospital_num_patient -=1
                print name,'is confirmed for discharge'
        return self

Case1=Hospital('North Memorial')
Case1.admit('Farashi','No Known Allergies','10162002').admit('John', 'Sinus', '70192011').admit('Peter', 'Sinus', '7192011').admit('Tom', 'Sinus', '72192011').admit('james', 'Sinus', '71192011').discharge('Farashi')
# Case1.discharge('701-3444').info()