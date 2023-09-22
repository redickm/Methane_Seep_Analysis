#./combine_CanopusSirius5_FBMNquant.py arg1 arg2 arg3 arg4
#arg1: tab delimited quant file for fbmn
#arg2: tab delimited canopus results summary
#arg3: name for combined output
#arg4: Feature list ID (no spaces, can be a date, file name etc. output will be arg4_IDsExtracted.tsv and will include the canopus summary with an additional column for feature IDs. You can leave it as Canopus and have it get overwritten each time if you want.)
#both input files (args 1 & 2) MUST be generated from same mzmine feature list
./combine_CanopusSirius5_FBMNquant.py 062922_mzmine3_seep_quant.tsv canopus_compound_summary.tsv 20220629_5m_mat_canopus_combined.txt 20220629_canopus
