<<<<<<< HEAD
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
=======
import numpy as np

#Quality control
def quality_control(seq_data)
        print(f"this is a low quality read:", line)
# A simple simultion
        with open(file_path, 'r') as file:
        for line in file:
            if len(line) > 10:
                print(f"this is a low quality read:", line)
          print(f"QC completed")
>>>>>>> variant-module
file = ['ATC', 'TTAC', 'TAGC']
quality_contol(file)
