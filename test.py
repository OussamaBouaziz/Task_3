import csv



print("what label are you looking for ?")
label_input = input()


def get_line(string):   #to be applied for extreme cases null, www .. ,
    father = ""

    with open("onto_x.csv") as csvfile:
        reader = csv.reader(csvfile)
        i=1

        for row in reader:
            if string != row[0]:
                i += 1

            else: break

    ancestor = father.join(row[1])
    print("The ancestor <<<<<<<<<<<<<<<<<<<<<", ancestor)
    print("the whole row is", row)
    print("The label is in the ", i, "th line", ancestor)

    return (ancestor, i, row[2])

# get_line(label_input)
# print("The result is ", get_line(label_input)[2])

def extreme_or_not(string):

     if get_line(label_input)[2] == "http://www.w3.org/2002/07/owl#Thing" or get_line(label_input)[2] in (None,""):
            print("the label is you should use is ", get_line(string)[0])
     else : print(("the parents are ", get_line(string)[2]))





extreme_or_not(label_input)












