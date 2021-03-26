import csv
from anytree import Node, RenderTree, AsciiStyle, PreOrderIter
import pprint



entity = input("Please enter the entity label you want to investigate:\n")  # Label has to be written
first_one =[]
first_one.append(entity)
#print(first_one)
# function that gets the LABEL from the ID
def get_label_from_id(one_id):
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if one_id == row[0]:
                a_parents_label = row[1]
                print(a_parents_label)
    return a_parents_label


def get_parents(table_child):
    parents = []
    all_of_them = []
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(len(table_child)):
                if table_child[i] == row[0]:
                    parents.append(row[2])  # Construire le tableau des parents [de la case i du table_child[i] ]
                    split_parents = parents[0].split("|")
                    for j in range(len(split_parents)):
                        print(split_parents, "Those are split parents")
                    get_parents(split_parents)



get_parents(first_one)
# extremes(get_parents(first_one))

