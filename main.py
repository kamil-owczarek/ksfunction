def calculate(usb_size, memes):
    """
    The function returns a tuple with value of all memes on the USB stick and set of memes names.
    Takes two arguments:
    usb_size - a number describing the capacity of the USB stick in GiB
    memes - list of three element tuples, each contain the name, size in MiB and price in caps.
    """
    # size of USB in MiB
    usb_size *= 1024
    n = len(memes)
    # set for names of memes in solution
    names = set()
    # creating a table using list comprehensions
    values = [[0 for x in range(usb_size + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(usb_size + 1):
            if i == 0 or j == 0:
                values[i][j] = 0
            elif memes[i - 1][1] <= j:
                values[i][j] = max(memes[i - 1][2] + values[i - 1][j - memes[i - 1][1]], values[i - 1][j])
            else:
                values[i][j] = values[i - 1][j]
    # it's a max value of memes which contain USB stick
    caps = values[n][usb_size]
    maks = usb_size
    # decrease for loop
    for i in range(n, 0, -1):
        if values[i][usb_size] != values[i - 1][usb_size]:
            # add name of the meme to set names
            names.add(memes[i-1][0])
            # decrease max size of USB stick by size of meme
            usb_size -= memes[i-1][1]
    # return a tuple of solution and set of memes
    return caps, names


usb_size = 1
memes = [
    ('rollsafe.jpg', 205, 6),
    ('sad_pepe_compilation.gif', 410, 10),
    ('yodeling_kid.avi', 605, 12)
]

print(calculate(usb_size, memes))