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
def get_label_from_id(One_ID):
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if One_ID == row[0]:
                a_parents_label = row[1]
                print(a_parents_label)
    return a_parents_label

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
#print("The direct-parents IDs are: ", split_parents)
parents_labels = []
for i in range(len(split_parents)):
    label = get_label_from_id(split_parents[i])
    parents_labels.append(str(label))
    parents_labels[i] = Node(parents_labels[i], parent=Adam)

print("The parents labelings are", parents_labels)
print("----------------")
print(Adam)
print(RenderTree(Adam))





