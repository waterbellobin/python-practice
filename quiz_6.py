# for i in range(1, 51):
#     file_name = str(i)+"week.txt"
#     file = open(file_name, "w", encoding="utf8")
#     file.write(str(i) + " week\n")
#     file.write("name: Sujong")
#     file.close()

for i in range(1, 51):
    with open(str(i) + "week.txt", "w", encoding="utf8") as file:
        file.write("{0} Week".format(i))