import csv
from anytree import Node, RenderTree, AsciiStyle, PreOrderIter

with open("onto_x.csv") as csvfile:
    reader = csv.reader(csvfile)


# start building tree before function.
def get_parents_and_draw_nodes(table_child, node_child): # table child is the input for the first time, the first generation in the second ...

    parents =[]

    for row in reader:
        for i in range(len(table_child)):

            if table_child[i] == row[0]:        #   Cherche le ID
                node_parent = Node(str(get_label_from_id(table_child[i]))) # construire le point
                parents.append(row[2])          # Construire le tableau des parents [de la case i du table_child[i] ]
                split_parents = parents.split("|")      # separer les parents
                new_node = Node(str(split_parents[j]), parent=node_child)

                print(RenderTree(Adam, style=AsciiStyle()).by_attr())

def get_parents(table_child):
    parents = []
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(len(table_child)):
                if table_child[i] == row[0]:
                    parents.append(row[2])  # Construire le tableau des parents [de la case i du table_child[i] ]
                    split_parents = parents.split("|")
        print(split_parents, "those are the split parents"")

    return split_parents


def draw_next_generation(table_child, Tree):
    for i in range(len(table_child)):



