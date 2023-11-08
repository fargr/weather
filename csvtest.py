import csv
def load_data_from_csv(csv_file):
    not_empties = []
    with open(csv_file, "r", encoding="utf-8") as file:
        data = csv.reader(file)
        for line in data: 
            not_empties.append(line)
            # if line != []:
            #     not_empties.append(line) 
    print(not_empties)
    
load_data_from_csv("\data\example_two.csv")