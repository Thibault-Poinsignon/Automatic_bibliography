
from Bio import Entrez
Entrez.email = "thibault.poinsignon@protonmail.com"

#organism = "Cerevisiae"
organism = "Albicans"


###List of the techniques, grouped as in http://enseqlopedia.com/enseqlopedia/

Low_RNA_detection = ["CEL-Seq","CirSeq","CLaP","CytoSeq","Digital RNA Sequencing","DP-Seq","Drop-Seq","Hi-SCL","InDrop","MARS-Seq","Nuc-Seq","PAIR","Quartz-Seq","scM&T-Seq","SCRB-Seq","scRNA-Seq","scTrio-seq","Smart-Seq","Smart-Seq2","snRNA-Seq","STRT-Seq","SUPeR-Seq","TCR-LA-MC PCR","TIVA","UMI","5C","Div-Seq","FRISCR","TCR Chain Pairing","AbPair"]

RNA_modifications = ["ICE","MeRIP-Seq","miCLIP-m6A","Pseudo-Seq","PSI-Seq"]

RNA_structure = ["CAP-seq","Cap-Seq","CIP-TAP","PARS-Seq","SPARE","Structure-Seq/DMS-Seq","CIRS-Seq","icSHAPE","SHAPE-MaP","SHAPE-Seq"]

RNA_transcription = ["2P-Seq","3’NT Method","3P-Seq","3Seq","3′-Seq","5′-GRO-Seq","BruChase-Seq","BruDRB-Seq","Bru-Seq","CAGE","CHART","ChIRP","ClickSeq","GRO-seq","NET-Seq","PAL-Seq","PARE-Seq","PEAT","PRO-Cap","PRO-Seq","RAP","RARseq","RASL-Seq","RNA-Seq","SMORE-Seq","TAIL-Seq","TATL-Seq","TIF-Seq","TL-Seq","4sUDRB-Seq","CaptureSeq","cP-RNA-Seq","FRT-Seq","GMUCT","mNET-Seq"]

RNA_Protein_interactions = ["AGO-CLIP","CLASH","CLIP-Seq or HITS-CLIP","DLAF","eCLIP","hiCLIP","iCLIP","miR-CLIP","miTRAP","PAR-CLIP","PIP-Seq","Pol II CLIP","RBNS","Ribo-Seq or ARTSeq","RIP-Seq","TRAP-Seq","TRIBE","BrdU-CLIP","HiTS-RAP","irCLIP"]

Protein_Protein_Interaction = ["PD-Seq","ProP-PD/PDZ-Seq"]

Sequence_rearrangements = ["2b-RAD","CPT-seq","ddRADseq","Digenome-seq","EC-seq","hyRAD","RAD-Seq","Rapture","RC-Seq","Repli-Seq","SLAF-seq","TC-Seq","Tn-Seq/INSeq","Bubble-Seq","NSCR","NS-Seq","Rep-Seq/Ig-Seq/MAF"]

DNA_break_mapping = ["BLESS","DSB-Seq","GUIDE-seq","HTGTS","LAM-HTGTS","Break-seq","SSB-Seq"]

DNA_Protein_interactions = ["DNase-Seq","Pu-seq","3-C","Hi-C","4C-seq","5C","ATAC-Seq","Fast-ATAC","CATCH_IT","Chem-seq","ChIA-PET","ChIPmentation","ChIP-Seq","DamID","DNase I SIM","FAIRE-seq","Sono-Seq","FiT-Seq","HiTS-FLIP","MINCE-seq","MNase-Seq","MPE-seq","NG Capture-C","NOMe-Seq","ORGANIC","PAT-ChIP","PB_seq","SELEX-seq","THS-seq","UMI-4C","X-ChIP-seq"]

Epigenetics = ["Aba-seq","BisChIP-Seq/ChIP-BS-Seq/ChIP-BMS","BSAS","BSPP","BS-Seq/Bisulfite-Seq/WGBS","CAB-Seq","EpiRADseq","fCAB-seq","fC-CET","fC-Seal","hMeDIP-seq","JBP1-seq","MAB-seq","MethylCap-Seq","MeDIP-Seq","DIP-seq","MIRA","MRE-Seq","Methyl-Seq","oxBS-Seq","PBAT","redBS-Seq","caMAB-seq","RRBS-Seq","RRMAB-seq","TAB-Seq","TAmC-Seq","T-WGBS"]

Low_level_DNA_detection = ["Safe-SeqS","scAba-seq","scATAC-Seq (Cell index variation)","scATAC-Seq (Microfluidics variation)","scBS-Seq","cM&T-Seq","scRC-Seq","SMDB","smMIP","G&T-Seq","5C","DR-Seq","G&T-Seq","MALBAC","MDA","MIDAS","IMS-MDA","ddMDA","scM&T-Seq","Drop-ChIP","scChIP-seq","Duplex-Seq","MIPSTR","nuc-seq/SNES","OS-Seq"]

techniques = [Low_RNA_detection, RNA_modifications, RNA_structure, RNA_transcription, RNA_Protein_interactions, DNA_break_mapping, Protein_Protein_Interaction, Sequence_rearrangements, DNA_Protein_interactions, Epigenetics, Low_level_DNA_detection]

names_techniques = ["Low_RNA_detection", "RNA_modifications", "RNA_structure", "RNA_transcription", "RNA_Protein_interactions","DNA_break_mapping", "Protein_Protein_Interaction", "Sequence_rearrangements", "DNA_Protein_interactions", "Epigenetics", "Low_level_DNA_detection"]


###Creation of the bibliography

#For each group, a .txt file is created.
#For each technique, the name of the technique is search on PubMed with the name of the organism : "[technique] [organism]"
#The name of the technique and the count of articles found are written in the .txt file.
#For the 20 first articles, their titles, DOI, publication dates and abstracts are written in the .txt file.

for T,name in zip(techniques,names_techniques) :
	fichier = open(name+"_biblio.txt","a")
	for t in T :
	    req = Entrez.esearch(db="pubmed", term=t+" "+organism)
	    res = Entrez.read(req)
	    Id = res["IdList"]
	    Count = res["Count"]
	    fichier.write("\n"+t+"\n"+Count+"\n")
	    if int(Count) > 0 :
	        for i in Id :
	            req_esummary = Entrez.esummary(db="pubmed", id=i)
	            res_esummary = Entrez.read(req_esummary)
	            req_efetch = Entrez.efetch(db="pubmed", id=i, rettype="txt")
	            res_efetch = Entrez.read(req_efetch)
	            if res_esummary != [] :	
	            	if "Title" in res_esummary[0] :
	            		fichier.write("\n\n"+ res_esummary[0]["Title"])
	            	if "DOI" in res_esummary[0] :
	            		fichier.write("\n" + res_esummary[0]["DOI"])
	            	if "PubDate" in res_esummary[0] :
	            		fichier.write("\n" + res_esummary[0]["PubDate"])
	            if res_efetch != [] :
	            	if "Abstract" in res_efetch['PubmedArticle'][0]['MedlineCitation']['Article'] :
	            		fichier.write("\n" + res_efetch['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText'][0] + "\n\n")
	fichier.close()


###Articles inventory

#count the number of articles for each technic.

fichier = open("Articles_inventory_"+organism+".txt","a")
fichier.write("technic type\ttechnic\tnumber of articles\n")

for T,name in zip(techniques,names_techniques) :
	for t in T :
	    req = Entrez.esearch(db="pubmed", term=t+" "+organism)
	    res = Entrez.read(req)
	    Id = res["IdList"]
	    Count = res["Count"]
	    fichier.write(name+"\t"+t+"\t"+Count+"\n")

fichier.close()



