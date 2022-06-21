

import re
from csv import DictWriter
#import PyPDF2 as pdf2
try:
    import PyPDF2 as pdf2
except ImportError as err:
    print("PyPDF2 needs to be installed")


# with open ("bol.pdf", "rb") as f:
#    pdf = pdf2.PdfFileReader(f)
#    page = pdf.numPages
#    first_pg = pdf.getPage(page)
#    first_text = first_pg.extract_text()


def product_info(input):
   #! Gets the Lot # , Order shipped, CTN, Product Code, and Code Date
    pattern = re.compile(r"\d.+") 
    matches = pattern.findall(input)
    has_CTN = [s for s in matches if "CTN" in s]
    

    product_list = []
    for items in has_CTN:
        rm_extra_spaces = " ".join(items.split())
        convert_to_list = rm_extra_spaces.split(" ")
        if len(convert_to_list) < 6:
            pass # Need to create a function that adds in fields, if they are blank
        
        details = {
            "Lot #": convert_to_list[0],
            "Case Orders": convert_to_list[1],
            "Case Picked": convert_to_list[2],
            "Product Code": convert_to_list[4],
            "Code Date": convert_to_list[5]
        }

        product_list.append(details)

    return product_list



def get_pallet_id(input):
    palletID =re.compile(r"\n.+\b.+")
    pIDmatch = palletID.findall(input)
    has_Pid = [s for s in pIDmatch if "Pallet Id" in s]
    
    pallet_list = []
    for items in has_Pid:
        rm_extra_spaces = " ".join(items.split())
        convert_to_list = rm_extra_spaces.split(" ")
    
        pallet_list.append(convert_to_list)
        
    return pallet_list



def get_gross_weight(input):
    gross_weight =re.compile(r"\n.+\b.+")
    gross_match = gross_weight.findall(input)
    g_weights = [s for s in gross_match if "G  " in s]


    gross_list = []
    for items in g_weights:
        rm_extra_spaces = " ".join(items.split())
        convert_to_list = rm_extra_spaces.split(" ")
        

        details = {
            "Gross Unit Weight": convert_to_list[1],
            "Gross Shipping Weight": convert_to_list[2]
        }

        gross_list.append(details)
    
    return gross_list


def get_net_weight(input):
    net_weight = re.compile(r"\n.+\b.+")
    net_match = net_weight.findall(input)

    net_weight = [s for s in net_match if "N " in s]
    #n_weights = net_weight[7:]
    
    #print(net_weight)

    net_list = []

    for items in net_weight:
        rm_extra_spaces = " ".join(items.split())
        convert_to_list = rm_extra_spaces.split(" ")
        if len(convert_to_list) > 4:
            continue
        else:
        
            details = {
                "Net Unit Weight": convert_to_list[1],
                "Net Shipping Weight": convert_to_list[2]
                }
        
            net_list.append(details)

    return net_list
    #print(net_list)


    

def get_page_info(page):

    with open ("bol.pdf", "rb") as f:
        pdf = pdf2.PdfFileReader(f)

        first_pg = pdf.getPage(page)
        text = first_pg.extract_text()
    
    product = product_info(text)
    g_weight = get_gross_weight(text)
    n_weight = get_net_weight(text)
    palletID = get_pallet_id(text)

    #print(product)
    
    for i in range(len(product)):
        product[i].update(g_weight[i])

    for i in range(len(product)):
        product[i].update(n_weight[i])


    with open('spreadsheet.csv','a') as outfile:
        if page == 0:
            writer = DictWriter(outfile, ('Lot #','Case Orders','Case Picked', 'Product Code', 'Code Date', 'Gross Unit Weight', 'Gross Shipping Weight', 'Net Unit Weight', 'Net Shipping Weight'))
            writer.writeheader()
            writer.writerows(product)
        
        else:
            writer = DictWriter(outfile, ('Lot #','Case Orders','Case Picked', 'Product Code', 'Code Date', 'Gross Unit Weight', 'Gross Shipping Weight', 'Net Unit Weight', 'Net Shipping Weight'))
            writer.writerows(product)
    


def main():
    
    with open ("bol.pdf", "rb") as f:
        pdf = pdf2.PdfFileReader(f)
        page_count = pdf.numPages
        #first_pg = pdf.getPage(page)
        #text = first_pg.extract_text()

    for pages in range(page_count):
        get_page_info(pages)
        #get_page_info(pages) 
     


#get_net_weight(first_text)
#get_page_info()
main()
#print(page)

