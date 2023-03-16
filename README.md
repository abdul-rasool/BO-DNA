# BO-DNA

BO-DNA: Biologically optimized encoding model for a highly-reliable DNA data storage

## What is BO-DNA?

BO-DNA proposes a novel **b**iologically **o**ptimized encoding for **DNA** data storage (**BO-DNA**) to overcome the reliability problem. BO-DNA is developed by a new rule-based mapping method to avoid data drop during the transcoding of binary data to premier nucleotides. A customized optimization algorithm based on a tent chaotic map is applied to maximize the lower bounds that help to minimize the nonspecific hybridization errors. The robustness of BO-DNA is computed by four bio-constraints to confirm the reliability of newly generated DNA sequences.

The improved MFOS algorithm goal is to achieve global optima solutions with robust convergence and balanced searching abilities to enhance the lower bounds and coding rates of DNA codes by overcoming the above problems. The improved heuristic algorithm is practiced to generate the optimized DNA codewords with GC-content, Hamming distance, no-runlength constraints, and it improved 12–28% lower bounds coding sets than the prior algorithms. Consequently, our approach's shorter sequences can help reduce errors during DNA synthesis and sequencing. Thus, storing a larger file in a shorter DNA sequence is feasible due to the improved lower bounds and coding rates of DNA coding sets. 

# Installation 

Step-by-step installation is as follows: 

## Tools and environment 

> Install Anaconda from here https://www.anaconda.com/products/distribution, a leading platform powered by Python 

> VS code https://code.visualstudio.com/download or any alternative Python supported source-code editor 


## Experimental steps 

Update the existing system according to requirements or run

```
pip3 install -r requirements.txt
```
1. Firstly, load the data to convert into binary (1, 0) and convert it into DNA nucleotides (A, C, G, T) by using rule-based mapping. It generates premier nucleotides and suppored by encode and decode the data.
2. train the CMF algorithm (or any other) with premier nucleotides.
(the parameter and operators settings are given in the manuscript (currently under review))
3. CMF is based on 6 benchmark functions. *Algorithms performances* folder contains the *Optimizer.py* file, in which all algorithms configuration is available by selecting the following operations with your requirements:
   - Select optimizer (e.g.)
   ```
    optimizer=["CMF","MFOS"]
   ``` 
   - Select benchmark function (e.g.) 
   ```
    objectivefunc=["F1","F6"] 
   ``` 
   - select other parameters and export results 
   ```
    params = {'PopulationSize' : 50, 'Iterations' : 500}
    export_flags = {'Export_avg':True, 'Export_details':True, 'Export_convergence':True, 'Export_boxplot':True}
   ``` 
4. The output will be received with different numbers of lower bounds which used with the bio-coding constraitns (GC content, Hamming distance, homopolymer, and RC constraints). 
5. After the CMF assessments, train BO-DNA to calculate the GC content, Hamming distance, homopolymer, and RC  DNA coding constraints for C<sup>GC, NL, RC</sup>(*n,W,d*) constraints. The output will provide the statistical results with different information, i.e., total DNA nucleotides, running time, density, sequence lenght, etc.


## Requirements

- NumPy
- SciPy
- sklearn
- pandas
- matplotlib
- fcmaes
- python 3.xx 
- math
- random 

# License

BO-DNA is licensed under the GNU General Public License, for more information read the LICENSE file or refer to:

http://www.gnu.org/licenses/

# Citation

A related paper is under review. 
