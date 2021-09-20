from Bio import Entrez
Entrez.email = "Your.Name.Here@example.org"
handle = Entrez.efetch("pubmed", id="28440475,27476679", retmode="xml")
# handle = Entrez.efetch("pubmed", id="25277099,26309161,23791657,25394902,28440475,20858276,23333633,26462034,"
#                                     "21953071,25888956,28693273,26400174,23791885,26124344,23497265,23359482,"
#                                     "26712794,27071841,21375733,19665978,27476679,27446418,23372687,24788655,"
#                                     "27155522,20331864", retmode="xml")

records = Entrez.read(handle)
print("1 ---> ", records)
records = records['PubmedArticle']
print("2 ---> ", records)

for record in records:
    print(record['MedlineCitation']['Article']['ArticleTitle'])
    # print(record['MedlineCitation']['Article'])
handle.close()