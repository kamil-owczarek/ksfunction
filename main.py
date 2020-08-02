usb_size = 1
memes = [
    ('rollsafe.jpg', 205, 6),
    ('sad_pepe_compilation.gif', 410, 10),
    ('yodeling_kid.avi', 605, 12)
]

def main():
    print(calculate(usb_size, memes))

def calculate(size_of_usb, list_of_memes):
    """
    The function returns a tuple with value of all list_of_memes on the USB stick and set of list_of_memes names.
    Takes two arguments:
    size_of_usb - a number describing the capacity of the USB stick in GiB
    list_of_memes - list of three element tuples, each contain the name, size in MiB and price in caps.
    """
    # size of USB in MiB
    size_of_usb *= 1024
    n = len(list_of_memes)
    # set for names of list_of_memes in solution
    names = set()
    # creating a table using list comprehensions
    values = [[0 for x in range(size_of_usb + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(size_of_usb + 1):
            if i == 0 or j == 0:
                values[i][j] = 0
            elif list_of_memes[i - 1][1] <= j:
                values[i][j] = max(list_of_memes[i - 1][2] + values[i - 1][j - list_of_memes[i - 1][1]], values[i - 1][j])
            else:
                values[i][j] = values[i - 1][j]
    # it's a max value of list_of_memes which contain USB stick
    caps = values[n][size_of_usb]
    # decrease for loop
    for i in range(n, 0, -1):
        if values[i][size_of_usb] != values[i - 1][size_of_usb]:
            # add name of the meme to set names
            names.add(list_of_memes[i - 1][0])
            # decrease max size of USB stick by size of meme
            size_of_usb -= list_of_memes[i - 1][1]
    # return a tuple of solution and set of list_of_memes
    return caps, names

if __name__ == '__main__':
    main()