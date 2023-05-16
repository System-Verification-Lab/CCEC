#include "CircuitOptimizer.hpp"
#include "SatEncoder.hpp"
#include "algorithms/RandomCliffordCircuit.hpp"
#include <fstream>

#include <chrono>
#include <fstream>
#include <sys/resource.h>


#include <ctime>
#ifdef _MSC_VER
#define localtime_r(a, b) (localtime_s(b, a) == 0 ? b : NULL)
#endif

#include <filesystem>
#include <gtest/gtest.h>
#include <locale>


class SatEncoderTest : public testing::TestWithParam<std::string> {};
 

TEST_F(SatEncoderTest, CheckEqualWhenEqualRandomCircuits) {
  std::random_device        rd;
  std::mt19937              gen(rd());
  qc::RandomCliffordCircuit circOne(100, 1, gen());
  qc::CircuitOptimizer::flattenOperations(circOne);
  

    std::size_t step1 = 1;
    std::size_t j = 1;

  

  std::size_t iList[] = {250, 50};
    

    for (std::size_t k = 0; k < 10; ++k) {
    std::size_t i = iList[k];
     std::size_t j = 1;
     for (; j <= 151; j += step1) {

      circOne = qc::RandomCliffordCircuit(i, j, gen());
      qc::CircuitOptimizer::flattenOperations(circOne);
     
      
      auto start = std::chrono::high_resolution_clock::now(); // start timer 
       
    
      auto circTwo = circOne.clone();

      SatEncoder satEncoder; 
      bool result = satEncoder.testEqual(circOne, circTwo);
      EXPECT_EQ(result, true);



      auto end = std::chrono::high_resolution_clock::now(); // end timer
      auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count(); // duration in milliseconds
      
      std::ofstream myfile;
      myfile.open("dokimiprint1.txt", std::ios::app);
      myfile << duration << "ms\n";
      myfile.close();

      // renaming the original file
      std::ostringstream newFileName;
      newFileName << "qusat_output_" << i << "_" << j << ".txt";
      std::rename("dokimiprint1.txt", newFileName.str().c_str());
      }



   


  }
}


