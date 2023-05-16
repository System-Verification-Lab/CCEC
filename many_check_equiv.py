#Modify the variables of the "for" loop and the variables k,l to the appropriate values
import stim
import time
import math

k = 250
l = 150
check_0 = 0
check_plus = 0




for i in range(50, k+1, 200): 
    
      
        for j in range(10, l+1, 10):
            U_filename = f"UST_{i}_{j}.stim"
            V_filename = f"VST_{i}_{j}.stim"
            Plus_U_filename = f"Plus_UST_{i}_{j}.stim"
            Plus_V_filename = f"Plus_VST_{i}_{j}.stim"
    
            with open(U_filename, "r") as f:
                circuit_str = f.read()
            circuit1 = stim.Circuit.from_file(U_filename)
            U = stim.TableauSimulator()
    
            with open(V_filename, "r") as f:
                circuit_str = f.read()
            circuit2 = stim.Circuit.from_file(V_filename)
            V = stim.TableauSimulator()
    
            with open(Plus_U_filename, "r") as f:
                circuit_str = f.read()
            circuit3 = stim.Circuit.from_file(Plus_U_filename)
            Plus_U = stim.TableauSimulator()
    
            with open(Plus_V_filename, "r") as f:
                circuit_str = f.read()
            circuit4 = stim.Circuit.from_file(Plus_V_filename)
            Plus_V = stim.TableauSimulator()
             
            # Start measuring elapsed time
            start_time = time.monotonic()
            
            # we create the tableaus from circuits:
            U.do(circuit1)
            U.canonical_stabilizers()
    
            V.do(circuit2)
            V.canonical_stabilizers()
    
            Plus_U.do(circuit3)
            Plus_U.canonical_stabilizers()
    
            Plus_V.do(circuit4)
            Plus_V.canonical_stabilizers()
    
            # defining
            stabilizers1 = U.canonical_stabilizers()
            stabilizers2 = V.canonical_stabilizers()
    
            # defining
            stabilizers_plus_1 = Plus_U.canonical_stabilizers()
            stabilizers_plus_2 = Plus_V.canonical_stabilizers()
    
            # testing if U and V are equal on |0>^n
            if stabilizers1 == stabilizers2:
                print(f"The stabilizers are the same on {U_filename} and {V_filename} for |0>^n")
                #check_0 += 1
            else:
                print(f"The stabilizers are different on {U_filename} and {V_filename} for |0>^n")
    
            # testing if U and V are equal on |+>^n
            if stabilizers_plus_1 == stabilizers_plus_2:
                print(f"The stabilizers are the same on {Plus_U_filename} and {Plus_V_filename} for |+>^n")
                #check_plus += 1
            else:
                print(f"The stabilizers are different on {Plus_U_filename} and {Plus_V_filename} for |+>^n")
                # End measuring elapsed time
            end_time = time.monotonic()   
                 # Print elapsed time
                
            elapsed_time = math.floor(1000*(end_time - start_time))
            print(f"Elapsed time: {elapsed_time} seconds")
            
            with open(f"stim_times_{i}.txt", "a") as output_file:
                output_file.write(f"{elapsed_time}\n")
            
            
            
            
            