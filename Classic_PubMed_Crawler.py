import requests
from bs4 import BeautifulSoup

def pubmed_spider(max_pages):
    page = 1
    while(page <= max_pages):
        base_url = 'https://www.ncbi.nlm.nih.gov/m/pubmed/'
        url = 'https://www.ncbi.nlm.nih.gov/m/pubmed/?term=mir145&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # li = soup.select(".r li > a")
        # print("page ==> ", page)
        #
        # for link in li:
        #     print(link.get('href'))
        print("page ==> ", page)
        for ul in soup.find_all('ul', class_='r'):
            for li in ul.find_all('li'):
                a = li.find('a')
                href = base_url + a['href']
                title = a.get_text()
                pmid = get_pmid(href)

                print("LINK : ", href)
                print("TITLE : ", title)
                print("PMID : [", pmid, "]")
                # print(href, title, '[', pmid, ']')
                # print("-"*60)

        page +=1

def get_pmid(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for div in soup.find_all('div', class_='pmids'):
        pmid = div.find('span')
        pmidStr = pmid.string
        pmidStr = pmidStr.replace(' [PubMed - indexed for MEDLINE]', '')
        pmidStr = pmidStr.replace(' [PubMed - as supplied by publisher]', '')
        pmidStr = pmidStr.replace(' [PubMed - in process]', '')
        return pmidStr

pubmed_spider(2)