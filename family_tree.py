import csv
from anytree import Node, RenderTree


entity = input("Please enter the entity label you want to investigate:\n")  # Label has to be written

# This is Adam- The tree's root is constructed after this
with open("onto_x.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if entity == row[1]:
            print("The labeling you are looking for exists")


# function that gets the LABEL from the ID
def get_label_from_id(one_id):
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if one_id == row[0]:
                a_parents_label = row[1]
                print(a_parents_label)
    return a_parents_label


def all_grands(table_parents_labels):
    print("AHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    grands = []  # Where the parents IDs are to be stored
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(len(table_parents_labels)):
                if table_parents_labels[i] == row[1]:
                    print("d5alna ", i ,"marrs lil if")
                    # extracting parent
                    grands.append(row[2])
                    split_grands = grands[0].split("|")
                    print("The direct-parents IDs are: ", split_grands)
                    grands_labels = []
                    for j in range(len(split_grands)):
                        label = get_label_from_id(split_grands[i])
                        grands_labels.append(str(label))
                        #grands_labels[i] = Node(grands_labels[i], parent=table_parents_labels[i])
                        print(grands_labels[i],"AYA kifech")



parents = []  # Where the parents IDs are to be stored
with open("onto_x.csv") as csvfile:
    reader = csv.reader(csvfile)
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

    parents_labels.append(str(label))



all_grands(parents_labels)

print("The parents labelings are", parents_labels)
#print("----------------")
#print(RenderTree(Adam))
