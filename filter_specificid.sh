#Shell script for "filter_specificid.py" filtering of a combined CANOPUS output and quantification (peak area) table for a specific chemical class as annotated by CANOPUS in either ontology at any level or confidence.
#Argument 1 is the python script being called.
#Argument 2 is the path for a tab delimited input file with CANOPUS output and peak areas of MS features.
#Argument 3 is the file name for the output file.
#Argument 4 is the search term that will be used for filtering.
./filter_specificid.py canopus_peakarea_combined.txt canopus_peakarea_peptide_filter.txt peptid
