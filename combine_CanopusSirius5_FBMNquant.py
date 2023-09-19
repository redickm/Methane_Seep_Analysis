#!/usr/bin/python3

#identify files from command line
import re, sys
args = sys.argv
input_FBMN_quant = args[1]
input_Canopus = args[2]
output_combined = args[3]
FeaturelistID = args[4]
output_canopusIDs = f'{FeaturelistID}_IdsExtracted.txt'

#open files
dF_handle_quant = open(input_FBMN_quant, "r")
dF_handle_canopus = open(input_Canopus, "r")
dF_handle_canopusIDs = open(output_canopusIDs, "w")


#extract row IDs from canopus summary and create output
pattern = r"_([0-9]*)$"
rawHeaderLine = dF_handle_canopus.readline()
headerLine = rawHeaderLine.rstrip()
dF_handle_canopusIDs.write(f"FeatureID\t{headerLine}")
for rawLine in dF_handle_canopus:
    line = rawLine.rstrip()
    lineparts = line.split("\t")
    SiriusID = lineparts[0]
    match_object = re.search(pattern, SiriusID)
    if (match_object):
        first_occ = match_object.group()
        #print(f"{first_occ}")
        FeatureID = match_object.group(1)
        #print(f"{SiriusID} corresponds to {FeatureID}")
        dF_handle_canopusIDs.write(f"\n{FeatureID}\t{line}")
dF_handle_canopusIDs.close()

#create combined headerline
dF_handle_canopusIDs = open(output_canopusIDs, "r")
dF_handle_out = open(output_combined, "w")
rawHeaderLine_canopus = dF_handle_canopusIDs.readline()
headerLine_canopus = rawHeaderLine_canopus.rstrip()
rawHeaderLine_quant = dF_handle_quant.readline()
headerLine_quant = rawHeaderLine_quant.rstrip()
dF_handle_out.write(f"{headerLine_canopus}\t{headerLine_quant}")
dF_handle_canopusIDs.close()

#combine files
for rawLine in dF_handle_quant:
    line_quant = rawLine.rstrip()
    lineparts_quant = line_quant.split("\t")
    RowID = float(lineparts_quant[0])
    row_has_match = "No"
    dF_handle_canopusIDs = open(output_canopusIDs, "r")
    rawHeaderLine_canopus = dF_handle_canopusIDs.readline()
    headerLine_canopus = rawHeaderLine_canopus.rstrip()
    for canopusrawLine in dF_handle_canopusIDs:
        line_canopus = canopusrawLine.rstrip()
        lineparts_canopus = line_canopus.split("\t")
        FeatureID = float(lineparts_canopus[0])
        if RowID == FeatureID:
            row_has_match = "Yes"
            dF_handle_out.write(f"\n{line_canopus}\t{line_quant}")
    dF_handle_canopusIDs.close()
    if row_has_match == "No":
        dF_handle_out.write(f'\n{RowID}\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\t{line_quant}')
dF_handle_out.close()
dF_handle_quant.close()

        
