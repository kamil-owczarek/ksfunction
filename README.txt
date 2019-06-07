The task is similary to Knapsack problem.

The function takes two arguments: 
	usb_size - a number describing the capacity of the USB stick in GiB,
	memes - list of three element tuples, each contain the name, size in MiB and price in caps.

At the beginning of function I use operator *= with "usb_size" to change size into MiB from GiB beacuse memes size is MiBs.

An empty matrix "caps" is in dimension (usb_size)x(number of memes).

In for loop I fill first element of each row with 0 and then if the size from previous row is equal or smaller than current column number, cell fills up with Max function.

Else otherwise cell of "caps" fills up with value from previous row.

"caps" is the last element of "caps" and it's solution.

Then I also retrun which values create the result and add this memes to as set "names".

The result of the function is a tuple with value of all memes on the USB stick and set of memes names.

Python version: 3.7

