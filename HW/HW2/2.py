#과제_2

from re import search

def handle_uniprot_header (header):
    result = {'id' : '', 'Entry' : '', 'Protein' : '',
              'OS' : '', 'GN' : '', 'PE' : '', 'SV' : '' }
    res = search("\|[A-Z][0-9]+\|", header)
    result['id'] = res.group()[1:-1]
    
    res = search("[A-Z]+_[A-Z]+", header)
    result['Entry'] = res.group()
    
    res = search("[A-Z][a-z]+[a-z\s]+[^\sOS=]", header)
    result['Protein'] = res.group()
    
    res = search("OS=[A-Z][a-z]+[a-zA-z\s(/)0-9]+[^\sGN=][^\sOX=]", header)
    result['OS'] = res.group()[3:]

    res = search("GN=[A-Za-z]+[^\sPE=]", header)
    result['GN'] = res.group()[3:]

    res = search("PE=[0-9]+", header)
    result['PE'] = res.group()[3:]

    res = search("SV=[0-9]+", header)
    result['SV'] = res.group()[3:]
    
    return result

# main
print(handle_uniprot_header(">sp|P01942|HBA_MOUSE Hemoglobin subunit alpha OS=Mus musculus OX=10090 GN=Hba PE=1 SV=2"))



