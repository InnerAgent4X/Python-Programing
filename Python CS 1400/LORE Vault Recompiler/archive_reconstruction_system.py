import sys



def text_parser():
    with open(sys.argv[1], 'r') as file:
        for line in file:
            print("This is working")







def main():
    print(sys.argv[0])
    print(sys.argv[1])

    text_parser()





if __name__ == '__main__':
    main()