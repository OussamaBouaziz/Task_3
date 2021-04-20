import csv



print("what label are you looking for ?")
label_input = input()

def get_label_from_id(one_id):
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if one_id == row[0]:
                a_parents_label = row[1]
                print(a_parents_label)


def get_line(string):   #to be applied for extreme cases null, www .. ,
    father = ""

    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        i=1

        for row in reader:
            if string != row[0]:
                i += 1

            else: break

    ancestor = father.join(row[2])

    print("the whole row is", row)
    print("The label is in the ", i, "th line", ancestor)

    return (ancestor.split("|"), i)


def extreme_or_not(string):
    print("extreme cases now")
    for i in range(len(get_line(label_input)[0])):
        if (get_line(label_input)[0])[i] in "http://www.w3.org/2002/07/owl#Thing" or (get_line(label_input)[0]) in (None,""):
            print("the label is you should use is ", get_line(string)[0])
        else : print(("the parents are ", get_line(string)[0]))

def get_parents(table_child):
    parents = []
    generation = 0
    all_of_them = []
    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(len(table_child)):
                if table_child[i] == row[0]:
                    # generation = generation + 1
                    print(table_child, "if is visited for the ", i, "time")
                    parents.append(row[2])  # Construire le tableau des parents [de la case i du table_child[i] ]
                    split_parents = parents[0].split("|")
                    print("split parents of ", get_label_from_id(table_child[i]), "are >>>>", split_parents,
                          "this is the ", generation, "generation")
                    # generation = generation + 1
                    for j in range(len(split_parents)):
                        generation = generation + 1
                        # print("We are now in the for LOOOOOOP<<<<<<<<", j)
                        # generation = generation + 1
                        print(get_label_from_id(split_parents[j]), "This is one parent from the > ", generation,
                              " < genration")
                        get_parents(split_parents)

    return (generation)

get_line(label_input)
get_parents(get_line(label_input)[0])
extreme_or_not(label_input)