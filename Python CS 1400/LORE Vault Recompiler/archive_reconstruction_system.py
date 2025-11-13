import sys


#opens the text file, then sorts and exports every line as a tuple with the number first
def text_parser(Bookcode):
    with open(sys.argv[1], 'r') as file:
        lines_sortable =[]

        #splits the lines by the | then adds it to the list as a tuple
        for line in file:
            line_contents = line.split("|")
            lines_sortable.append((line_contents[1], line_contents[0]))

        #sorts the tuples
        sorted_lines = sorted(lines_sortable)

        #creates a second list of only the text files in order to check for length
        lines_second = [text[1] for text in sorted_lines]

        longest_line = max(lines_second, key=len)
        longest_line_index = lines_second.index(longest_line)
        print(f"Longest line ({longest_line_index + 1}): {longest_line}")

        average_line = (sum(len(text) for text in lines_second)/len(lines_second))
        print(f"Average length: {average_line:.3f}")

        external_file(Bookcode, longest_line_index, longest_line, average_line, lines_second)






def external_file(Bookcode, longest_line_index, longest_line, average_line, lines_second):
    #checks that a file exicts. creates it if it doesn't and writes to it if it does
    try:
        with open(f"{Bookcode}_book.txt", "x") as file:
            print("File not found, creating new file")
            file.write(f"""{Bookcode}\n
            Longest line ({longest_line_index}): {longest_line}\n
            {average_line}\n""")
            for line in lines_second:
                file.write(f"{line}\n")

    except FileExistsError:
        print("File Found!")
        with open(f"{Bookcode}_book.txt", "w") as file:
            file.write(f"""{Bookcode}\n
Longest line ({longest_line_index}): {longest_line}\n
Average length: {average_line}\n""")
            for line in lines_second:
                file.write(f"{line}\n")



#Displays Bookcode, then calls the text parser function
def main():
    Bookcode = (f"{sys.argv[1][0]}{sys.argv[1][1]}{sys.argv[1][2]}")
    print(Bookcode)

    text_parser(Bookcode)


#Initializese program
if __name__ == '__main__':
    main()