import sys


#opens the text file, then sorts and exports every line as a tuple with the number first
def text_parser(Bookcode):

    with open(sys.argv[1], "r") as file:
        lines_sortable =[]
        longest_line = "starter"
        longest_line_index = 0

        #splits the lines by the | then adds it to the list as a tuple
        for line in file:
            line_contents = line.split("|")
            lines_sortable.append((int(line_contents[1]), line_contents[0]))


            #sets the variable to the longest line in the file by len it also chooses the highest line number
            #by nature of going though the iterations of the loop.
            if len(line_contents[0]) > len(longest_line):
                longest_line = line_contents[0]
                longest_line_index = line_contents[1]

        #sorts the tuples
        sorted_lines = sorted(lines_sortable)

        #creates a second list of only the text files in order to check for length
        lines_second = [text[1] for text in sorted_lines]

        average_line = (sum(len(text) for text in lines_second)/len(lines_second))

        external_file(Bookcode, longest_line, longest_line_index, average_line, lines_second)





## Both my round and my :.f are rounding, but it seems the rubric is truncating...

def external_file(Bookcode, longest_line, longest_line_index, average_line, lines_second):
    #checks that a file exicts. creates it if it doesn't and writes to it if it does
    try:
        with open(f"{Bookcode}_book.txt", "x") as file:
            print("File not found, creating new file")
            file.write(f"""{Bookcode}\n
Longest line ({longest_line_index}): {longest_line}\n
Average length: {round(average_line)}\n
""")
            for line in lines_second:
                file.write(f"{line}\n")

    except FileExistsError:
        print("File Found!")
        with open(f"{Bookcode}_book.txt", "w") as file:
            file.write(f"""{Bookcode}\n
Longest line ({longest_line_index}): {longest_line} \n
Average length: {average_line:.0f}\n
""")
            for line in lines_second:
                file.write(f"{line}\n")



#Displays Bookcode, then calls the text parser function
def main():
    Bookcode = (f"{sys.argv[1][0]}{sys.argv[1][1]}{sys.argv[1][2]}")

    text_parser(Bookcode)


#Initializese program
if __name__ == '__main__':
    main()
