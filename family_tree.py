import csv
from anytree import Node, RenderTree, AsciiStyle, PreOrderIter


entity = input("Please enter the entity label you want to investigate:\n")  # Label has to be written

# This is Adam- The tree's root is constructed after this
with open("onto_x.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if entity == row[1]:# gib 0 an um ID zu finden
            print("The labeling you are looking for exists")
            # a_parents_label = row[1]


# function that gets the LABEL from the ID
def get_label_from_id(one_id):
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if one_id == row[0]:
                a_parents_label = row[1]
                print(a_parents_label)
    return a_parents_label


def all_grands(first_node,table_parents_labels):
    print("AHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    first_node.is_root

    grands = []  # Where the parents IDs are to be stored

    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            for i in range(len(table_parents_labels)):# for el in table_parents_labels:

                if table_parents_labels[i] == row[1]: #if el == row[1]

                    node_parent = Node(str(table_parents_labels[i]), parent= first_node)
                    #   print(table_parents_labels[i] )
                    print("if node is visited ", i + 1 ,"Times")

                    grands.append(row[2])
                    print(grands , "DOES THIS HAVE ONE ELEMENT ?")
                    grands_labels = []

        for k in range(len(grands)):
            split_grands = grands[k].split("|") # The grands table doesn't have just one element.
            print("The direct-parents IDs are: ", split_grands)

            for j in range(len(split_grands)):
                label = get_label_from_id(split_grands[j])
                grands_labels.append(str(label))

                new_node = Node(str(grands_labels[j]), parent=node_parent)

                print(grands_labels,"AYA kifech")




parents = []  # Where the parents IDs are to be stored
with open("onto_x.csv") as csvfile:
    reader = csv.reader(csvfile) # muss man nicht jedes mal machen
    for row in reader:
        if entity == row[1]:
            # extracting parent
            parents.append(row[2])
            Adam = Node(str(row[1]))


# extracting direct parents and seperate their class ID


# print("The parents are: ", parents)
split_parents = parents[0].split("|")
# print("The direct-parents IDs are: ", split_parents)
parents_labels = []
for i in range(len(split_parents)):
    label = get_label_from_id(split_parents[i])
    parents_labels.append(label)

all_grands(Adam, parents_labels)
print(RenderTree(Adam, style=AsciiStyle()).by_attr())


print("The parents labelings are", parents_labels)
#print("----------------")
#print(RenderTree(Adam))
