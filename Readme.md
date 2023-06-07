## INSTALLATION INSTRUCTIONS
 
 Run 
 ```
 git submodule update --init --recursive 
 ```
 This will download the submodules of QuSAT and stim.
 

# apply changes on stim:

In the Stim directory replace the original file "tableau_simulator.cc" by the one provide here.
The original file lies in "Stim/src/stim/simulators/tableau_simulator.cc"

 
# install Stim

Follow instructions in https://github.com/quantumlib/Stim/blob/main/README.md to install Stim
 

# apply changes on QuSAT
 
1)In the QuSAT directory replace the original file "test_satencoder.cpp" by the one provided here.
The original file lies in "qusat/test/test_satencoder.cpp"

2)In the QuSAT directory replace the original file "RandomCliffordCircuit.cpp" by the one provided here.
The original file lies in "qusat/extern/qfr/src/algorithms/RandomCliffordCircuit.cpp"


# install QuSAT
 Follow instructions in https://github.com/cda-tum/qusat/blob/main/README.md to install QuSat

The provided example will generate the plots for fixed number of qubits for the values 50 and 250 and varying depth up to 150.


# Running numerics    #

 
the "run_all.py" will run all four python scripts that are necessary for producing and plotting the data. 

```
python3 run_all.py 

```
The provided example will generate the plots for fixed number of qubits for the values 50 and 250 and varying depth up to 150.

Make sure that you run "run_all.py" in the same directory as the one in which the output files produced by QuSAT are (i.e. the .txt files with names of the form "qusat_output_{}_{}.txt").








