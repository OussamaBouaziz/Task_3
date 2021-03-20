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
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(len(table_child)):
                if table_child[i] == row[0]:
                    parents.append(row[2])  # Construire le tableau des parents [de la case i du table_child[i] ]
                    split_parents = parents[0].split("|")
            # print({row[Preferred Label]}, "this is a label")
            print(split_parents, "those are the split parents")

    return split_parents


def extremes(table): # input is split_parents
    parents_id = []
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(len(table)):
                if table[i] == ("http://www.w3.org/2002/07/owl#Thing" or "null"):
                    parents_id.append(row[1])

                else: parents_id.append(get_label_from_id(table[i]))

    print(parents_id, "and this ")

    return parents_id

get_parents(first_one)
# extremes(get_parents(first_one))

