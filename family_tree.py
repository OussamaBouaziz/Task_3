import csv
from anytree import Node, RenderTree, AsciiStyle
import pprint


entity = input("Please enter the entity label you want to investigate:\n")  # Label has to be written

# function that gets the LABEL from the ID
def get_label_from_id(one_id):
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if one_id == row[0]:
                a_parents_label = row[1]
                print(a_parents_label)
    return a_parents_label


def looking_for_brothers_and_sisters(from_parents_table):
    bro_sis_labels = []
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if from_parents_table[0] == row[2]:
                bro_sis_labels.append(row[1])

    return bro_sis_labels

def all_grands(first_node,table_parents_labels):

    grands = []  # Where the parents IDs are to be stored

    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            for i in range(len(table_parents_labels)):# for el in table_parents_labels:

                if table_parents_labels[i] == row[1]: #if el == row[1]

                    #   print(table_parents_labels[i] )
                    print("if node is visited ", i + 1 ,"Times")
                    print(table_parents_labels, "HOWWWAAA WALLA lAAAA .. 7lili")

                    grands.append(row[2])
                    print(grands , "DOES THIS HAVE ONE ELEMENT ?")
                    grands_labels = []
                    node_parent = Node(str(table_parents_labels[i]), parent=first_node)
                    final_dictionary.update({str(table_parents_labels[i]): node_parent.depth})

                    for k in range(len(grands)):
                        split_grands = grands[k].split("|") # The grands table doesn't have just one element.
                        print("The direct-parents IDs are: ", split_grands)


                    for j in range(len(split_grands)):
                        label = get_label_from_id(split_grands[j])
                        grands_labels.append(str(label))
                        new_node = Node(str(grands_labels[j]), parent=node_parent)

                        print(new_node.depth, "3oooooooooom9")

                        final_dictionary.update({str(grands_labels[j]): new_node.depth})

                        formal_dictionary = pprint.PrettyPrinter(width=10)
                        formal_dictionary.pprint(final_dictionary)

    return formal_dictionary





parents = []  # Where the parents IDs are to be stored
with open("onto_x.csv") as csvfile:
    reader = csv.reader(csvfile) # muss man nicht jedes mal machen
    for row in reader:
        if entity == row[0]:
            # extracting parent
            parents.append(row[2])
            Adam = Node(str(row[1]))

    print(parents,"333333333333333333333333")

    print(looking_for_brothers_and_sisters(parents), "brudiiiiis and schwestiiiiis !!!!")


final_dictionary = {}

# print("The parents are: ", parents)
split_parents = parents[0].split("|")
# print("The direct-parents IDs are: ", split_parents)
parents_labels = []
for i in range(len(split_parents)):
    label = get_label_from_id(split_parents[i])
    parents_labels.append(label)

all_grands(Adam, parents_labels)

print(RenderTree(Adam, style=AsciiStyle()).by_attr())










