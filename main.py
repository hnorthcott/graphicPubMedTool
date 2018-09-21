from Bio import Entrez

Entrez.email = 'awmoulaison@wpi.edu'
Entrez.api_key = 'f513b4e2e1a0b578c9d3dd731e36f19f7f08'


def __init__(self, email):
    """Entrez requires and email address."""
    Entrez.email = 'awmoulaison@wpi.edu'
    Entrez.api_key = 'f513b4e2e1a0b578c9d3dd731e36f19f7f08'


def search(query):
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='50',
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results


def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'awmoulaison@wpi.edu'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results


def summary_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'awmoulaison@wpi.edu'
    handle = Entrez.esummary(db = 'pubmed',
                             retmode = 'xml',
                             id= ids)
    records = Entrez.parse(handle)

    for record in records:
        print(record['AuthorList'])
        print(record['LastAuthor'])




if __name__ == '__main__':
    results = search('cancer')
    id_list = results['IdList']
    summary_details(id_list)
    papers = fetch_details(id_list)
    for i, paper in enumerate(papers['PubmedArticle']):
        print("%d) %s" % (i + 1, paper['MedlineCitation']['Article']['ArticleTitle']))






