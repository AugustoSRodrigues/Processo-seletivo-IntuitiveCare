import requests
import re
import zipfile
from bs4 import BeautifulSoup as bs
from PyPDF2 import PdfMerger



def download_pdf(url):
    response = requests.get(url)
    
    
    m = PdfMerger() 
    

    soup = bs(response.text,'html.parser')
    links = soup.find_all('a',href=re.compile(".pdf"),string=re.compile("Anexo"))
    # z = re.compile("Anexo")
    
    for l in links:
        print((l.get_text()))
    
    with zipfile.ZipFile("anexos.zip","w") as z:
        for link in links:
            with open(link.get_text()+".pdf",'wb') as p:
                pdf = requests.get(link.get('href'))
                p.write(pdf.content)
                z.write(p.name)
            p.close()
    z.close


    # with open("pdf.pdf", 'ab') as p:
    #     for link in links:
         
    #         if 'Anexo' in link.get('href',[]):
    #             response = requests.get(link.get('href'))
    #             cont+=response.content
                
    #     p.write(cont)       
    # p.close()


def main():
    url = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
    download_pdf(url)

main()

