import csv



my_dict = {}

with open("words.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        my_dict[row[0]] = row [1]

    my_dict = {row[0]:row[1] for row in reader}
def rus_to_eng(word):
    for key, value in my_dict.items():
        if value == word:
            return key
    return