import argparse
def main(start, max, path, filename):
    filepath = path + '/' +  filename
    with open(filepath, 'a') as f:
        for i in range(start, max+1):
            if i == max:
                f.write(str(i))
            else:
                f.write(str(i) + '\n')

# python .\intWordlist.py -m 999 -s 0 -p ./wordlists -f number.txt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a incremental integer wordlist.")
    parser.add_argument("-m", "--max", type=int, help="Specify a max number that you want to create 1-max incremental integer wordlist.", required=True)
    parser.add_argument("-s", "--start", type=int,help="Specify a number of wordlist startwith. (default=1).", default=1, required=False)
    parser.add_argument('-p', "--path", type=str, help="Specify a path to save the wordlist. (default=./)", default="./", required=False)
    parser.add_argument('-f', "--filename", type=str, help="Specify a filename to save the wordlist. (default=int.txt)", default="int.txt", required=False)
    start = parser.parse_args().start
    max = parser.parse_args().max
    path = parser.parse_args().path
    filename = parser.parse_args().filename
    main(start, max, path, filename)