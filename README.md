# Methane_Seep_Analysis
# Integration of Untargeted Metabolomics and Microbial Community Analyses to Characterize Distinct Deep-Sea Methane Seeps.
Margaret A. Redick1, Milo E. Cummings2, George F. Neuhaus1, Lila M. Ardor Bellucci3, Andrew R. Thurber2,3*, Kerry L. McPhail1*
1Department of Pharmaceutical Sciences, College of Pharmacy, 2Department of Microbiology, College of Science, 3College of Earth, Ocean, and Atmospheric Sciences, Oregon State University, Corvallis, Oregon, USA

**This repository contains computer code used for data analysis in the above titled manuscript. The workflow is as follows**:

1. MZmine3 was used to pre-process raw mass spectrometry (MS) data files, containing MS1 and MS2 data, in .mzML format. The resulting MS feature list was exported as an .mgf file, with an accompanying quantification (peak area) table as a .tsv file.
2. SIRIUS 5 CANOPUS analysis was performed using the .mgf file to obtain predicted molecular formulas and structure class for all MS features in the feature list as a .tsv file.
3. Python script combine_CanopusSirius5_FBMNquant was used to combine the MZmine-generated quantification table and CANOPUS compound summary tsv files.

**For pie charts and sunburst plots**:

4. Plotly was used to generate pie charts (Figure 2) and sunburst plots of canopus data by core using Create_Sunburst_Plots.ipynb. This input file used is the combined CANOPUS and quant table with the addition of columns containing summed peak areas by feature for each core and the NPClassifier pathways “Fatty Acids” and “Terpenoids” were renamed as “Lipids and Lipid-like” (canopus_peakarea_combined_sumbycore_combinelipidnpcpath.txt). “maxdepth” is set to 1, so the resulting .pdf outputs appear as pie charts. The sunburst plots can be produced if maxdepth is set higher and can also be exported as interactive .html files.
   
**For stacked bar chart**:

5. R script stackedbar_8_tol.R was used to generate stacked bar plots of NPClassifier pathway proportions by core/depth (Figure 3).  Input file: The combined CANOPUS and quantification file (from step 3) was used to create NPCpathway_peakarea.csv which contains peak areas summed by NPClassifier pathway for each sample in Excel with samples in rows and NPClassifier pathways in columns. 

**For correlation analysis and generation of Figures 7 and S1**:

6. Filter_specificid was used to filter the combined CANOPUS and quantification table (from step 3) for a CANOPUS classification of interest (peptide), selecting all features annotated as potentially peptidic at any level in either the ClassyFire or NPClassifier ontologies.
7. The Jupyter notebook correlations_between_two_datasets.ipynb provided by Allegra Aron: (https://github.com/allegra-aron/Stromatolite_analysis/blob/main/correlations_between_two_feature_tables.ipynb) was updated and used to perform a Spearman’s rank correlation analysis between microbial families and the MS features annotated as potentially peptidic. This outputs the heatmap in Figure S1.
8. The table of significant correlations output from the correlation analysis (corr_coef_sig_peptidemz_family_BH.csv) was then used to create a list of MS features with significant correlations (p-values < 0.05). In Excel, the quantification table of potentially peptidic features was filtered using the list of MS features with significant correlations. This filtered peptidic feature quantification table was log10(x+1) transformed and used as the input table for heatmaps.ipynb to generate the heatmap in Figure 7.
