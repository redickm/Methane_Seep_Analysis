#!/usr/bin/python3

#identify files from command line
import re, sys
args = sys.argv
input_original = args[1]
output_results = args[2]
specificid = args[3]

#open files
dF_handle_in = open(input_original, "r")
oF_handle_out = open(output_results, "w")

#filtering
rawHeaderLine = dF_handle_in.readline()
headerLine = rawHeaderLine.rstrip()
oF_handle_out.write(f"{headerLine}")
for rawLine in dF_handle_in:
    passed_filter = "No"
    line = rawLine.rstrip()
    lineparts = line.split("\t")
    for part in lineparts:
        if specificid.casefold() in part.casefold():
            #Passes filter
            passed_filter = "Yes"
            #print(f'{part}')
    if passed_filter == "Yes":
        oF_handle_out.write(f'\n{line}')
oF_handle_out.close()
dF_handle_in.close()
print("i'm done")