# # INSTALLATION INSTRUCTIONS
 
# create a python virtual environment
mkdir env
python3 -m venv env
source env/bin/activate
 
 
########
# Stim #
########
 
 
# download Stim and checkout the version of the code that was used
 
git submodule add https://github.com/quantumlib/Stim
 
 
cd Stim
git checkout 80f1b30abcce41c82629beb6f93c837fec40a3e6
cd ..
 

# apply changes:

In the Stim directory replace the original file "tableau_simulator.cc" by the one provide here.
The original file lies in "Stim/src/stim/simulators/tableau_simulator.cc"

 
 
# install Stim

# Follow instructions in https://github.com/quantumlib/Stim/blob/main/README.md to install Stim
 

#########
# QuSat #
#########
 
 
 
# download QuSat and checkout the version of the code that was used
 
git submodule add git@github.com:cda-tum/qusat.git
 
 
cd qusat
git checkout 974354c2ff96e19d733ada25d46c202acde4afd6
git submodule update --init --recursive
cd ..
 
# apply changes
 
1)In the QuSAT directory replace the original file "test_satencoder.cpp" by the one provided here.
The original file lies in "qusat/test/test_satencoder.cpp"

2)In the QuSAT directory replace the original file "RandomCliffordCircuit.cpp" by the one provided here.
The original file lies in "qusat/extern/qfr/src/algorithms/RandomCliffordCircuit.cpp"


 
# install QuSat
# Follow instructions in https://github.com/cda-tum/qusat/blob/main/README.md to install QuSat
# The provided example will generate the plots for fixed number of qubits for the values 50 and 250 and varying depth up to 150.
# For experiments different than the provided example, make sure to modify the variables of the "for" loops and the variables "i" and "j" according to the desired experiment.
 
#######################
# Running numerics    #
#######################
 

 
#the "run_all.py" will run all four python script that are necessary for producing and plotting the data. 

python3 run_all.py 


#The provided example will generate the plots for fixed number of qubits for the values 50 and 250 and varying depth up to 150. For different experiments make sure to modify the variables accordingly.

#For experiments different than the provided example, make sure to modify the variables of the "for" loop and also the variables "i" and "k" depending on the desired experiment. (They must be consistent across all three .py scripts)

############################################################################################
############################################################################################
############################################################################################






