import sys



def text_parser():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            lines = line.split('|')

            print(lines)







def main():
    print(sys.argv[1])

    text_parser()





if __name__ == '__main__':
    main()