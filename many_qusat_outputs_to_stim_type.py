
#Modify the variables of the "for" loop and the variables k,l to the appropriate values

k = 250
l = 150

#the 3rd parameter is the step-jump
for i in range(50, k+1,200):
    for j in range(10,l+1,10):

        # translate qusat_output_i_j.txt to appropriate stim code for U on |0>^n
        with open(f"qusat_output_{i}_{j}.txt", "r") as input_file, open(f"UST_{i}_{j}.stim", "w") as output_file:

            for line in input_file:
                line = line.strip()
                if line.startswith("h"):
                    n = line.split()[1]
                    output_file.write(f"H {n}\n")
                elif line.startswith("both(hs)"):
                    n = line.split()[1]
                    output_file.write(f"H {n}\n")
                    output_file.write(f"S {n}\n")
                elif line.startswith("sdagh"):
                    n = line.split()[1]
                    output_file.write(f"S_DAG {n}\n")
                    output_file.write(f"H {n}\n")
                elif line.startswith("z"):
                    n = line.split()[1]
                    output_file.write(f"Z {n}\n")
                elif line.startswith("x"):
                    n = line.split()[1]
                    output_file.write(f"X {n}\n")
                elif line.startswith("y"):
                    n = line.split()[1]
                    output_file.write(f"Y {n}\n")
                elif line.startswith("cnot"):
                    n, k = line.split()[1:]
                    output_file.write(f"CNOT {n} {k}\n")
                    
                    
                    
        # translate qusat_output_i_j.txt to appropriate stim code for V on |0>^n
        with open(f"qusat_output_{i}_{j}.txt", "r") as input_file, open(f"VST_{i}_{j}.stim", "w") as output_file:

            for line in input_file:
                line = line.strip()
                if line.startswith("h"):
                    n = line.split()[1]
                    output_file.write(f"H {n}\n")
                elif line.startswith("both(hs)"):
                    n = line.split()[1]
                    output_file.write(f"H {n}\n")
                    output_file.write(f"S {n}\n")
                elif line.startswith("sdagh"):
                    n = line.split()[1]
                    output_file.write(f"S_DAG {n}\n")
                    output_file.write(f"H {n}\n")
                elif line.startswith("z"):
                    n = line.split()[1]
                    output_file.write(f"Z {n}\n")
                elif line.startswith("x"):
                    n = line.split()[1]
                    output_file.write(f"X {n}\n")
                elif line.startswith("y"):
                    n = line.split()[1]
                    output_file.write(f"Y {n}\n")
                elif line.startswith("cnot"):
                    n, k = line.split()[1:]
                    output_file.write(f"CNOT {n} {k}\n")
                    
                    
                    
        # translate qusat_output_i_j.txt to appropriate stim code for U on |+>^n
        with open(f"qusat_output_{i}_{j}.txt", "r") as input_file, open(f"Plus_UST_{i}_{j}.stim", "w") as output_file:
            #hadamards
            for o in range(0, i):
                output_file.write(f"H {i}\n")            

            for line in input_file:
                line = line.strip()
                if line.startswith("h"):
                    n = line.split()[1]
                    output_file.write(f"H {n}\n")
                elif line.startswith("both(hs)"):
                    n = line.split()[1]
                    output_file.write(f"H {n}\n")
                    output_file.write(f"S {n}\n")
                elif line.startswith("sdagh"):
                    n = line.split()[1]
                    output_file.write(f"S_DAG {n}\n")
                    output_file.write(f"H {n}\n")
                elif line.startswith("z"):
                    n = line.split()[1]
                    output_file.write(f"Z {n}\n")
                elif line.startswith("x"):
                    n = line.split()[1]
                    output_file.write(f"X {n}\n")
                elif line.startswith("y"):
                    n = line.split()[1]
                    output_file.write(f"Y {n}\n")
                elif line.startswith("cnot"):
                    n, k = line.split()[1:]
                    output_file.write(f"CNOT {n} {k}\n")
                    
                    
                    
        # translate qusat_output_i_j.txt to appropriate stim code for U on |+>^n
        with open(f"qusat_output_{i}_{j}.txt", "r") as input_file, open(f"Plus_VST_{i}_{j}.stim", "w") as output_file:
            #hadamards
            for o in range(0, j):
                output_file.write(f"H {i}\n")            

            for line in input_file:
                line = line.strip()
                if line.startswith("h"):
                    n = line.split()[1]
                    output_file.write(f"H {n}\n")
                elif line.startswith("both(hs)"):
                    n = line.split()[1]
                    output_file.write(f"H {n}\n")
                    output_file.write(f"S {n}\n")
                elif line.startswith("sdagh"):
                    n = line.split()[1]
                    output_file.write(f"S_DAG {n}\n")
                    output_file.write(f"H {n}\n")
                elif line.startswith("z"):
                    n = line.split()[1]
                    output_file.write(f"Z {n}\n")
                elif line.startswith("x"):
                    n = line.split()[1]
                    output_file.write(f"X {n}\n")
                elif line.startswith("y"):
                    n = line.split()[1]
                    output_file.write(f"Y {n}\n")
                elif line.startswith("cnot"):
                    n, k = line.split()[1:]
                    output_file.write(f"CNOT {n} {k}\n")
                    
                    
                    
                    