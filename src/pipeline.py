import numpy as np

# Quality control
def quality_control(file_path):
    print("The quality control begins")

    # A simple simulations
    with open(file_path, 'r') as file:
        for line in file:
            if len(line.strip()) > 10:
                print("This is a low quality read:", line.strip())

    print("QC completed")


# Example usage (test data)
file = ['ATC', 'TTAC', 'TAGC']
