count= 0

with open("dracula.txt","r") as foo:
    with open("vampytimes.txt","w") as bar:
        for line in foo:
            if "vampire" in line.lower():
                count += 1
                print(line, end="", file=bar)

print(count)
