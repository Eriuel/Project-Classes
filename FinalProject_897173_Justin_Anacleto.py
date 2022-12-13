
import re
class Doctor():
    def formatDrInfo(propertiesValuesList):
        spaces = [5, 23, 16, 16, 16, 12]
        formattedText = ""
        for item in propertiesValuesList:
            formattedText += item + (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText

    def enterDrInfo(self):
        self.docID = input("Enter the Doctor's ID: \n")
        self.name = input("Enter the Doctor's name: \n")
        self.spec = input("Enter the Doctor's specialty: \n")
        self.workingTime = input("Enter the Doctor's timing (e.g., 7am-10pm): \n")
        self.qualif = input("Enter the Doctor's qualification: \n")
        self.roomNum = input("Enter the Doctor's room number: \n")
        self.addDrToFile(self)

    def readDoctorsFile(self):
        path = "D:\pythonData\doctors.txt"
        doctorsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    doctor = Doctor()
                    doctorsObjectList.append(doctor)
            file.close()
        except IOError:
            file = open(path, 'a+')
            print("doctors.txt file created")
        return doctorsObjectList

    def searchDoctorById(self, idSearch):
        doctorsObjectList = Doctor.readDoctorsFile()
        id = False
        for doctor in doctorsObjectList:
            if docID == idSearch:
                doctor.displayDoctorInfo()
                id = True
                return doctorsObjectList.index(doctor)
        if id == False:
            print("Doctor with given ID couldn't be found. \n")
            return -1

    def searchDoctorByName(self, nameSearch):
        doctorsObjectList = Doctor.readDoctorsFile()
        name = False

        for doctor in doctorsObjectList:
            if doctor.name == nameSearch:
                doctor.displayDoctorInfo()
                nameExist = True
        if name == False:
            print("Doctor with given name couldn't be found. \n")
            return -1

    def displayDoctorInfo(self):
        headerList = ["ID", "Name", "Specialty", "Timing", "Qualification", "Room Number"]
        print(Doctor.formatDrInfo(headerList) + "\n")
        valuesList = [self.docID, self.name, self.spec, self.workingTime, self.qualif,
                      self.roomNum]
        print(Doctor.formatDrInfo(valuesList))

    def editDoctorInfo(self):
        dr_Id = input("Please enter the id of the doctor that you want to edit their information:\n")
        dr_index = Doctor.searchDoctorById(dr_Id)
        if dr_index != -1:
            drObjList = Doctor.readDoctorsFile()
            drObjList[dr_index].name = input("Enter new Name: \n")
            drObjList[dr_index].spec = input("Enter new Specialist in: \n")
            drObjList[dr_index].workingTime = input("Enter new Timing: \n")
            drObjList[dr_index].qualif = input("Enter new Qualification: \n")
            drObjList[dr_index].roomNum = input("Enter new Room Number: \n")
            Doctor.writeListOfDoctorsToFile(drObjList)
        else:
            return -1

    def displayDoctorsList(self):
        path = "D:/pythonData/doctors.txt"
        headerList = ["ID", "Name", "Specialty", "Timing", "Qualification", "Room Number"]
        headerSpaces = [5, 23, 16, 16, 16, 12]
        for item in headerList:
            print(item + (" " * (headerSpaces[headerList.index(item)] - len(item))), end="")
        print("\n")
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()

    def writeListOfDoctorsToFile(self, doctorsObjectList):
        path = "D:/pythonData/doctors.txt"
        file = open(path, "r+")
        textOutput = ""
        for dr in doctorsObjectList:
            drProperties = [dr.id, dr.name, dr.specialization, dr.workingTime, dr.qualification, dr.roomNumber]
            ft = Doctor.formatDrInfo(drProperties)
            textOutput += ft + "\n\n"
        file.truncate(0)
        file.write(textOutput)
        file.close()

    def addDrToFile(self, drObject):
        path = "D:/pythonData/doctors.txt"
        textOutput = ""

        file = open(path, "a")
        dr = drObject
        drProperties = [dr.id, dr.name, dr.specialization, dr.workingTime, dr.qualification, dr.roomNumber]

        addText = Doctor.formatDrInfo(drProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()
class Facility():
    def addFacility(self):
        fname = input("Enter Facility name: \n")
        self.name = fname
        path = "D:/pythonData/facilities.txt"
        with open(path, "a") as file:
            file.write(self.name + "\n\n")

    def displayFacilities(self):
        print("The Hospital  Facilities are: \n\n")
        path = "D:/pythonData/facilities.txt"
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    def writeListOfFacilitiesToFile(self, facilityList):
        path = "D:/pythonData/facilities.txt"
        with open(path, "r+") as file:
            for facility in facilityList:
                file.write(facility + "\n\n")
class Laboratory():
    def addLabToFile(self, labObject):
        path = "D:/pythonData/laboratories.txt"
        textOutput = ""
        file = open(path, "a")
        labPropertiesList = [labObject.name, labObject.cost]
        addText = Laboratory.formatLabInfo(labPropertiesList, propertiesValuesList)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()

    def writeListOfLabsToFile(self, labObjectsList):
        path = "D:/pythonData/laboratories.txt"
        file = open(path, "r+")
        textOutput = ""
        for lab in labObjectsList:
            labPropertiesList = [lab.name, lab.cost]
            ft = Laboratory.formatLabInfo(labPropertiesList)
            textOutput += ft + "\n\n"
        file.truncate(0)
        file.write(textOutput)
        file.close()

    def displayLabList(self):
        path = "D:/pythonData/laboratories.txt"
        headerList = ["Lab", "Cost"]
        print(Laboratory.formatLabInfo(headerList))
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()

    def formatLabInfo(self, propertiesValuesList):
        spaces = [16, 16]
        formattedText = ""
        for item in propertiesValuesList:
            formattedText += item + (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText

    def enterLaboratoryInfo(self):
        self.name = input("Enter Laboratory facility: \n")
        self.cost = input("Enter Laboratory cost: \n")
        Laboratory.addLabToFile(self)

    def readLaboratoriesFile(self):
        path = "D:/pythonData/laboratories.txt"
        labsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    lab = Laboratory(line[0], line[1])
                    labsObjectList.append(lab)
            file.close()
        except IOError:
            file = open(path, 'a+')
            print("laboratories.txt file created")
        return labsObjectList
class Patient():
    def formatPatientInfo(self, propertiesValuesList):
        spaces = [5, 23, 16, 16, 16]
        formattedText = ""
        for item in propertiesValuesList:
            formattedText += item + (" " * (spaces[propertiesValuesList.index(item)] - len(item)))
        return formattedText

    def enterPatientInfo(self):
        self.docID = input("Enter the Patient's ID: \n")
        self.name = input("Enter the Patient's name: \n")
        self.disease = input("Enter the Patient's disease: \n")
        self.gender = input("Enter the Patient's gender: \n")
        self.age = input("Enter the Patient's agae: \n")
        Patient.addPatientToFile(self)

    def readPatientsFile(self):
        path = "D:/pythonData/patients.txt"
        patientsObjectList = []
        try:
            file = open(path, 'r')
            lines = file.readlines()
            for line in lines:
                if line.replace(" ", "") != "\n":
                    line = line.replace('\n', '')
                    line = re.split(r'\s{2,}', line)
                    patient = Patient(line[0], line[1], line[2], line[3], line[4])
                    patientsObjectList.append(patient)
            file.close()
        except IOError:
            file = open(path, 'a+')
            print("patients.txt file created")
        return patientsObjectList

    def searchPatientById(self, idSearch):
        patientsObjectList = Patient.readPatientsFile()
        id = False
        for patient in patientsObjectList:
            if patient.id == idSearch:
                patient.displayPatientInfo()
                id = True
                return patientsObjectList.index(patient)
        if id == False:
            print("Can't find the patient with the same ID on the system \n")
            return -1

    def displayPatientInfo(self):
        headerList = ["ID", "Name", "Disease", "Gender", "Age"]
        print(Patient.formatPatientInfo(headerList) + "\n")
        valuesList = [self.id, self.name, self.disease, self.gender, self.age]
        print(Patient.formatPatientInfo(valuesList))

    def editPatientInfo(self):
        patientID = input("Please enter the id of the Patient that you want to edit their information:\n")
        patientIndex = Patient.searchPatientById(patientID)
        if patientIndex != -1:
            patientObjList = Patient.readPatientsFile()
            patientObjList[patientIndex].name = input("Enter new Name: \n")
            patientObjList[patientIndex].disease = input("Enter new Disease: \n")
            patientObjList[patientIndex].gender = input("Enter new Gender: \n")
            patientObjList[patientIndex].age = input("Enter new Age: \n")
            Patient.writeListOfPatientsToFile(patientObjList)
        else:
            return -1

    def displayPatientsList(self):
        path = "D:/pythonData/patients.txt"
        headerList = ["ID", "Name", "Disease", "Gender", "Age"]
        print(Patient.formatPatientInfo(headerList))
        print("\n\n")
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
        file.close()

    def writeListOfPatientsToFile(self, patientsObjList):
        path = "D:/pythonData/patients.txt"
        file = open(path, "r+")
        textOutput = ""
        for patient in patientsObjList:
            patientProperties = [patient.id, patient.name, patient.disease, patient.gender, patient.age]
            ft = Patient.formatPatientInfo(patientProperties)
            textOutput += ft + "\n\n"

        file.truncate(0)
        file.write(textOutput)
        file.close()

    def addPatientToFile(self, patientObject):
        path = "D:/pythonData/patients.txt"
        textOutput = ""

        file = open(path, "a")
        patient = patientObject
        patientProperties = [patient.id, patient.name, patient.disease, patient.gender, patient.age]
        addText = Patient.formatPatientInfo(patientProperties)
        textOutput += addText + "\n\n"
        file.write(textOutput)
        file.close()

class Management():
    def DisplayMenu(self):
        while True:
            option = input('Select from the following options, or select 0 to stop:'
                           '1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients')
            if option == '1':
                while True:
                    docOption = input('Doctors Menu:\n1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu')
                    if docOption == '1':
                        Doctor.displayDoctorsList(self)
                    if docOption == '2':
                        Doctor.searchDoctorById(self)
                    if docOption == '3':
                        Doctor.readDoctorsFile(self)
                    if docOption == '4':
                        Doctor.addDrToFile(self)
                    if docOption == '5':
                        Doctor.editDoctorInfo(self)
                    if docOption == '6':
                        break
            if option == '2':
                while True:
                    facOption = input('Facilities Menu:\n1 - Display Facilities List\n2 - Add Facility\n3 - Back to the Main Menu')
                    if facOption == '1':
                        Facility.displayFacilities(self)
                    if facOption == '2':
                        Facility.addFacility(self)
                    if facOption == '3':
                        break
            if option == '3':
                while True:
                    labOption = input('Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu')
                    if labOption == '1':
                        Laboratory.displayLabList(self)
                    if labOption == '2':
                        Laboratory.addLabToFile(self)
                    if labOption == '3':
                        break
            if option == '4':
                while True:
                    patientOption = input('Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu')
                    if patientOption == '1':
                        Patient.displayPatientsList(self)
                    if patientOption == '2':
                        Patient.searchPatientById(self)
                    if patientOption == '3':
                        Patient.addPatientToFile(self)
                    if patientOption == '4':
                        Patient.editPatientInfo(self)
                    if patientOption == '5':
                        break
            if option == '0':
                break

doc = Doctor()
facility = Facility()
lab = Laboratory()
patients = Patient()
manage = Management()
manage.DisplayMenu()


