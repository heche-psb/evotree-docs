from evotree.simulatepbmm import PBMMBuilder
import pandas as pd

df = pd.read_csv("Fern_Data.tsv",header=0,index_col=0,sep='\t')
all_trait_names = df.columns

for trait_name in all_trait_names:
    PBMM = PBMMBuilder(tree='Fern.newick',trait='Fern_Data.tsv',traitcolname=trait_name,traitname=trait_name)
    PBMM.pagel_lambda()
