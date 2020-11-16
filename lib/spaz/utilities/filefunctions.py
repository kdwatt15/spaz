""" utility functions used to input/output data """
import csv
import json
import os


def read_csv(file_name):
    """ read a csv file into list of lists """
    with open(os.path.join('inputs',file_name), 'r') as f:
        return [row for row in csv.reader(f, delimiter=',')]
    
    
def write_csv(csv_list, file_path='output.csv'):
    """ write a list of lists to a csv file """
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for row in csv_list:
            csvwriter.writerow(row)
            
            
def flatten_dict(nested_dict):
    """ flattens a dictionary with values that are dictionaries. Helpful with JSON """
    for k1, v1 in nested_dict.items():
        output = [[k1, k2, v2] for k2, v2 in v1.items()]
    return output

