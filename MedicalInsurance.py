import csv 

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst

load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex' )
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')

class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    # Method that calculates the average ages of the patients in insurance.csv
    def analyze_ages(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        return ("Average Patient Age: " + str(round(total_age/len(self.patients_ages), 2)) + " years")
    
    # Method that calculates the average bmi of the patients in insurance.csv
    def average_bmi(self):
        total_bmi = 0
        for bmi in self.patients_bmis:
            total_bmi += float(bmi)
        return ("Average Patient BMI: " + str(round(total_bmi/len(self.patients_bmis), 2)) + ".")

    # Method that calculates the number of males and females in insurance.csv
    def analyze_sexes(self):
        females = 0
        males = 0
        for sex in self.patients_sexes:
            if sex == 'female':
                females += 1
            elif sex == 'male':
                males += 1
        print("Count for female: ", females)
        print("Count for males: ", males)

    # method to find each unique region patients are from
    def unique_regions(self):
        unique_regions = []
        for region in self.patients_regions:
            if region not in unique_regions:
                unique_regions.append(region)
        return unique_regions
    


    # method to find average yearly medical charges for patients in insurance.csv
    def average_charges(self):
        total_charges = 0
        for charge in self.patients_charges:
            total_charges += float(charge)
        return("Average Yearly Medical Insurance Charges: " + str(round(total_charges/len(self.patients_charges), 2)) + " dollars.")
    

    # method to create dictionary with all patients information
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary

patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

# analyzed_ages = patient_info.analyze_ages() 
# print(analyzed_ages)

# analyzed_sexes = patient_info.analyze_sexes()
# print(analyzed_sexes)

# unique_regions = patient_info.unique_regions()
# print(unique_regions)

# average_charges = patient_info.average_charges()
# print(average_charges)


#patient_dict = patient_info.create_dictionary()
#print(patient_dict)

# averaged_bmis = patient_info.average_bmi()
# print(averaged_bmis)