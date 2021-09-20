from Bio import Entrez

Entrez.email = "A.N.Other@example.com"
Entrez.tool = "MyLocalScript"

def get_retMax(DataBase, TermQuery):
    handle = Entrez.esearch(db=DataBase, term=TermQuery)
    record = Entrez.read(handle)
    handle.close()

    return record["Count"]

def get_All_PMIDs(DataBase, TermQuery, retMaxNo):
    handle = Entrez.esearch(db=DataBase, term=TermQuery, retMax=retMaxNo)
    record = Entrez.read(handle)
    handle.close()
    print("-------------> ", record)
    return record["IdList"]



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

db = "pubmed"
term = "mir145"
retMax = get_retMax(db, term)
print("retMax   ::  ", retMax)
pubmed_id_list = get_All_PMIDs(db, term, int(retMax))
print("Number of PubMed database titles = ", get_retMax(db, term))

if(int(retMax) != 0):
    print("PubMed Database = ", pubmed_id_list)
else:
    print("No documents match your search terms.")
