# http://people.duke.edu/~ccc14/pcfb/biopython/BiopythonEntrez.html

from Bio import Entrez

Entrez.email = "A.N.Other@example.com"
Entrez.tool = "MyLocalScript"

# ==============================================================================================================
# What databases do I have access to?

handle = Entrez.einfo()
record = Entrez.read(handle)
print(record["DbList"])
# ['pubmed', 'protein', 'nuccore', 'nucleotide', 'nucgss', 'nucest', 'structure', 'genome',
# 'genomeprj', 'bioproject', 'biosample', 'biosystems', 'blastdbinfo', 'books', 'cdd', 'clone',
# 'gap', 'gapplus', 'dbvar', 'epigenomics', 'gene', 'gds', 'geo', 'geoprofiles', 'homologene',
# 'journals', 'mesh', 'ncbisearch', 'nlmcatalog', 'omia', 'omim', 'pmc', 'popset', 'probe',
# 'proteinclusters', 'pcassay', 'pccompound', 'pcsubstance', 'pubmedhealth', 'seqannot', 'snp',
# 'sra', 'taxonomy', 'toolkit', 'toolkitall', 'unigene', 'unists', 'gencoll', 'gcassembly',
# 'assembly']

# ==============================================================================================================
# What if I want info about a database?

handle = Entrez.einfo(db="pubmed")
record = Entrez.read(handle)
print(record["DbInfo"]["Description"])  # PubMed bibliographic record
print(record["DbInfo"]["Count"])    # 27179031

# ==============================================================================================================
# How do I search a db for a given term?

handle = Entrez.esearch(db="pubmed", term="mir145", retmax=100)
record = Entrez.read(handle)
print(record["IdList"])
print(record["Count"])
print(record)
print(len(record["IdList"]))