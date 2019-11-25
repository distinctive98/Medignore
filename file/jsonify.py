
# input_file_name = "durItem.txt"
# output_file_name = "dur.txt"
# with open(input_file_name, "r", encoding="utf-8", newline="") as input_file, \
#         open(output_file_name, "w", encoding="utf-8", newline="") as output_file:

#     line = input_file.readline
#     print(line)
#     # for line in lines :
#     #     print(line)
#     #     # newline = line
#     #     # newline += ','
#     #     #print(line, file=output_file)


input_file_name = "durProhibit3.txt"
output_file_name = "durP3.txt"

input_file = open(input_file_name, 'r', encoding="utf-8")
output_file = open(output_file_name, 'w', encoding="utf-8")

while True:
    line = input_file.readline()
    if not line: 
        break
    else :
        line = line.strip('\n')
        line = line.replace('﻿', '')
        line += ','
        print(line, file=output_file)

input_file.close()
output_file.close()