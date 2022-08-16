

poketypes= { "fire": {"strong": ["grass", "bug"],
                      "weak": ["water", "ground"]},
             "water": {"strong": ["fire"],
                      "weak": ["grass"]},
             "grass": {"strong": ["water"],
                      "weak": ["fire"]},
           }


x= input("Pick a type: ")

y= input("strong or weak?")

print(poketypes[x][y])
