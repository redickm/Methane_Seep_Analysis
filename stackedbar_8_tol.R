#adapted from https://userweb.eng.gla.ac.uk/umer.ijaz/bioinformatics/ecological.html
library(ggplot2)
library(tidyverse)
abund_table<-read.csv("NPCpathway_peakarea.csv",  header = TRUE, row.names = 1)

#Get grouping information
grouping_info<-data.frame(row.names=rownames(abund_table),t(as.data.frame(strsplit(rownames(abund_table),"-"))))
 head(grouping_info)
# X1 X2 X3
# T_2_1   T  2  1
# T_2_10  T  2 10
# T_2_12  T  2 12
# T_2_2   T  2  2
# T_2_3   T  2  3
# T_2_6   T  2  6

#Apply proportion normalisation
x<-abund_table/rowSums(abund_table)
Pathway_list<-colnames(x)[1:N+1]
#x<-x[,order(colSums(x),decreasing=TRUE)]

#Extract list of top N Taxa (this is set to 8 because there are 7 pathways + the unassigned features so this is not actually removing any pathways here) 
N<-8
taxa_list<-colnames(x)[1:N]
#remove "__Unknown__" and add it to others
N<-length(taxa_list)

#Generate a new table with everything added to Others
new_x<-data.frame(x[,colnames(x) %in% taxa_list])
head(new_x)

#You can change the Type=grouping_info[,1] should you desire any other grouping of panels
df<-NULL
for (i in 1:dim(new_x)[2]){
  tmp<-data.frame(row.names=NULL,Depth=grouping_info[,2],Pathway=rep(colnames(new_x)[i],dim(new_x)[1]),Value=new_x[,i],Type=grouping_info[,1])
  if(i==1){df<-tmp} else {df<-rbind(df,tmp)}
}
colours <- c( "#999933", "#882255","#CC6677","#332288","#88CCEE","#44AA99","#117733","#DDDDDD");

legend_title<-"NPClassifier Pathway"


p<-ggplot(df,aes(Depth,Value,fill=fct_inorder(Pathway)))+geom_bar(stat="identity")+facet_grid(. ~ Type, drop=TRUE,scale="free",space="free_x")
p<-p+scale_fill_manual(legend_title,values=colours[1:(N+1)])
p<-p+theme_bw()+ylab("Proportions")
p<-p+ scale_y_continuous(expand = c(0,0))+theme(strip.background = element_rect(fill="gray85"))+theme(panel.margin = unit(0.3, "lines"))
p<-p+theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5))
pdf("NPCPathways_stacked.pdf",height=6,width=21)
print(p)
dev.off()
p
