
import re
#import PyPDF2 as pdf2
try:
    import PyPDF2 as pdf2
except ImportError as err:
    print("PyPDF2 needs to be installed")


with open ("bol.pdf", "rb") as f:
   pdf = pdf2.PdfFileReader(f)
   page = pdf.numPages
   first_pg = pdf.getPage(0)
   first_text = first_pg.extract_text()

#print(first_pg)
#print(pdf.numPages)
#print(first_text)

def useRegex(input):
   #! Gets the Lot # , Order shipped, CTN, Product Code, and Code Date
    pattern = re.compile(r"\d.+") 
    matches = pattern.findall(input)
    has_CTN = [s for s in matches if "CTN" in s]
    
   #! Gets the pallet ID 
    palletID =re.compile(r"\n.+\b.+")
    pIDmatch = palletID.findall(input)
    
    has_Pid = [s for s in pIDmatch if "Pallet Id" in s]
    gross_weight = [s for s in pIDmatch if "G  " in s]
    net_weight = [s for s in pIDmatch if "N  " in s]
    list_of_net_weights = net_weight[7:]

    filter_list = []
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
        print(details)


   #print(prodmatch)
"""    for items in has_CTN:
      print(items)
      print("-------------------")
"""

useRegex(first_text)
