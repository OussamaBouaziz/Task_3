import csv
from treelib import Node, Tree

#Label has to be written
entity = input("Please enter the entity label you want to investigate:\n")

#function that gets the LABEL from the ID



def get_label_from_ID(one_ID):

    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        table_parents = []
        for row in reader:
            if one_ID == row[0]:
                table_parents.append(row[1])
        print(table_parents)
    return table_parents

parents = [] #Where the parents IDs are to be stored

with open("onto_x.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if entity == row[1]:
            arbre = Tree()
            arbre.create_node(entity) #first node

            #extracting parent
            parents.append(row[2])





    #extracting direct parents and seperate their class ID

    print("The whole C3 is: ",parents)
    split_parents = parents[0].split("|")
    print("The direct-parents IDs are: ",split_parents)
    for i in range(len(split_parents)):
        weldih = get_label_from_ID(split_parents[i])









