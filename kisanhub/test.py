file_loc = "./data"
txt_file = file_loc + '/Tmax_UK.txt'
csv_file = file_loc + '/Tmax_UK.csv'

input_file = open(txt_file, 'r')
output_file = open(csv_file, 'w')
# input_file.readline() # skip first line 
for line in input_file:
    output_file.write(','.join(line.strip().split('  ')) + '\n')
input_file.close()
output_file.close()

