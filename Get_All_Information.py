from Bio import Entrez
from pubmed_lookup import Publication
from pubmed_lookup import PubMedLookup


Entrez.email = "A.N.Other@example.com"
Entrez.tool = "MyLocalScript"
email = ''

def get_retMax(DataBase, TermQuery):
    handle = Entrez.esearch(db=DataBase, term=TermQuery)
    record = Entrez.read(handle)
    handle.close()

    return record["Count"]


retMode = "xml"

db = "pubmed"
term = "mir-183 AND breast cancer"

retMaxNo = get_retMax(db, term)
print(retMaxNo)



handle = Entrez.esearch(db="pubmed", term="mir-183 AND breast cancer", retMax=retMaxNo)
result = Entrez.read(handle)
handle.close()
# ids = result['IdList']
ids = ['25277099', '26309161', '23791657', '25394902', '28440475', '20858276', '23333633', '26462034',
        '21953071', '25888956', '28693273', '26400174', '23791885', '26124344', '23497265', '23359482',
        '26712794', '27071841', '21375733', '19665978', '27476679', '27446418', '23372687', '24788655',
        '27155522', '20331864']

print(len(ids))
print(ids)
doi = []
pmids = []
#for each ids go through it and pull the summary
for uid in ids:
     handle2 = Entrez.esummary(db="pubmed", id=uid, rettype="gb", retmode="text")
     result2 = Entrez.read(handle2)
     handle2.close()

     lookup = PubMedLookup("https://www.ncbi.nlm.nih.gov/pubmed/"+ uid, email)
     publication = Publication(lookup)
     # print(result2)
     # print(result2[0]['ArticleIds']['doi'])
     # print(result2[0]['ELocationID'])

     print("[ Title ] : ", result2[0]['Title'])

     if "accepted" in result2[0]['History']:
         print("[ Published Date ] : ", result2[0]['History']['accepted'])
     else:
         print("[ Published Date ] : ", result2[0]['History']['pubmed'])

     if "DOI" in result2[0]:
         print("[ DOI ] : ", result2[0]['ArticleIds']['doi'])
         doi.append(result2[0]['ArticleIds']['doi'])
         pmids.append(result2[0]['ArticleIds']['eid'])
     else:
         print("[ DOI ] : ")

     print("[ PMID ] : ", result2[0]['ArticleIds']['eid'])
     print("[ ABSTRACT ] : ", repr(publication.abstract))
     print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

print(doi)
print(pmids)
print("=============")
print(len(doi))
print(len(pmids))

