from evotree.ploter import Tracer


Tracer_oj = Tracer(data="Posterior_Samples.tsv",usedata=["Polypodiales_sigma2","Cyatheales_sigma2"],n_row=1,n_col=2,n_chains=2,fs=(14,6))
Tracer_oj.basic_draw()
Tracer_oj.saveplot(output="Trace_Posterior_Samples.svg")


