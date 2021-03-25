import csv



print("what label are you looking for ?")
label_input = input()


def get_line(string):   #to be applied for extreme cases null, www .. ,
    father = ""

    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        i=1

        for row in reader:
            if string != row[1]:
                i += 1
            else: break
        ancestor = father.join(row[1])
        print("The ancestor <<<<<<<<<<<<<<<<<<<<<", ancestor)
        print("the whole row is", row)
        print("The label is in the ", i, "th line", ancestor)

    return (ancestor, i)

get_line(label_input)
# print("The result is ", get_line(label_input)[0])

def extreme_or_not(string):

    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[2] == ("http://www.w3.org/2002/07/owl#Thing" or "null"):
                print("the label is", get_line(string)[1])

#extreme_or_not(label)












