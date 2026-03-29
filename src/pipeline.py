import numpy as np 

#Quality control 
def quality_control(seq_data)
	print('The quality control begins')
# A simple simultion
	with open(file_path, 'r') as file: 
	for line in file:
	    if len(line) > 10:
		print(f"this is a low quality read:", line)
	  print(f"QC completed")
file = ['ATC', 'TTAC', 'TAGC']
quality_contol(file)
