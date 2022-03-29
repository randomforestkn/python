import json
from difflib import get_close_matches

print("Λεξιλόγιο Αγγλικών Ορισμών!")


#  load the data to a python dictionary
data = json.load(open("data.json","r"))

# function return data from the dict
def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    # suggesting word with similarity ratio with word in dictionary
    elif len(get_close_matches(w, data.keys())) > 0:
        print(f"Μήπως ψάχνεις την λεξη {get_close_matches(w, data.keys())[0]}; ")
        x = input("... ")
        x = x.lower()
        if x in ["ναι","yes","y","ye","yea"]:
            return data[get_close_matches(w, data.keys())[0]]
        else:
            y = input("Ποια λέξη ψάχνεις ")
            if y in data:
                return data[y]
            else:
                return "Η λέξη αυτή δεν υπάρχει"

    else:
        return "Αυτή η λέξη δεν υπάρχει."

w = input("Δώσε την λέξη: ")
word = dictionary(w)
if isinstance(word,list):
    for _ in word:
        print(_)
else:
    print(word)
