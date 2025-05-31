from evotree.simulatepbmm import PBMMBuilder,savage_dickey_density_ratio,writebf

PBMM = PBMMBuilder(tree='Fern.newick',trait='Fern_Data.tsv',traitcolname='Average DNA amount per chromosome (Mb)',traitname='Average chromosome size')

PBMM.calculate_ini_parameters()

pairs_to_compare = ["Equisetales_sigma2","Psilotales_sigma2","Ophioglossales_sigma2","Marattiales_sigma2"]

BF_Pair = savage_dickey_density_ratio(PBMM,sample="Posterior_Samples.tsv",compared_parameters=pairs_to_compare,lognormal=True)

writebf(BF_Pair,output="BF.tsv")

