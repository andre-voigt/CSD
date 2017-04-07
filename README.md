CSD - a set of software for generating differential co-expression networks. 

Basic steps for generating a CSD network:

Step 1: Computing Correlation scores for both conditions. 

FindCorrAndVar.cpp (once compiled), computes correlation and variance for all gene pairs IN A SINGLE data set, in the correct format for further processing. Specify file name, number of genes and number of data points in the header, compile, and run the resulting program. For large data sets, a user may need to run the command "ulimit -s unlimited" before running the resulting program, in order to accommodate for the large arrays involved. The output file is named "RhoAndVar.txt". Running the program will overwrite this file if it exists, so either change the file name after computing RhoAndVar.txt for the first data set, or change the name of the output file in the code header.

The input files are expected to be under the following format:
-Header line, containing sample IDs (may be empty, but must exist)
-One line of expression data per gene. The first column contains the gene name, the remaining columns contain individual data points. Columns must be separated by tabs. An example file is provided as ExpData.txt


FindCSD.py assumes that its two inputs (corresponding to RhoAndVar.txt generated under each condition) match gene pairs line-by-line. For this to be the case, it is IMPERATIVE that the two  original expression data sets:
- Contain the same number of genes
- Have said genes sorted in the same order.


Step 2: Computing C/S/D-scores

Specify filenames (RhoAndVar.txt from the two iterations of FindCorrAndVar.cpp") as the variables file1 and file2. Then, simply run the command:

python FindCSD.py


This produces a file "AllValues.txt", containing correlation and variance under both conditions, as well as C, S and D scores for all gene pairs. AllValues.txt may be quite large, on the order of gigabytes for ordinary data sets. It also produces three auxiliary files, Useable*Values.txt, which are used to generate the network in the next step.


Step 3: Network generation

After running the Step 2, simply run:

python CreateNetwork.py

The stringency of the cut-off value for network generation is determined by selSize (default value 10 000) in CreateNetwork.py (higher selSize results in a smaller network).

CreateNetwork.py outputs 4 files (one network of each interaction type, and a combined network), all following the same format. Each line represent an edge in the network, with the two genes specified in the first two columns. The third column specifies edge weight (value of the selected score), and the fourth column specifies edge type. 







