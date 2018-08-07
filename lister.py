import glob, os, sys

directory = sys.argv[1]
os.chdir(directory)

names = set()
for file in glob.glob("./**/*.txt", recursive=True):
    with open(file, "r") as dump_info:
        lines = dump_info.readlines()
        internal_name_line = lines[3]
        internal_name_line
        name = internal_name_line.replace("Internal Name: ", "")
        names.add(name)

names = sorted(names)

with open("games.txt", "w") as games_list:
    count = str(len(names))
    print("Found " + count + " games.")
    games_list.write("Total: " + str(count) +"\n\n")

    for name in names:
        games_list.write(name)