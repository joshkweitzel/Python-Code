#Calculator - to demonstrate Batch UI
#   Limited error handling implementation. Focus is on interaction.

from calculator import *

filename = "calculator_batch.txt"

batch_file = open(filename)

for line in batch_file:
    items = line.split(" ")
    command = (items[0], int(items[1]), int(items[2]))
    
    result = execute_command(command)
    print(command, " = ", result)

batch_file.close()

