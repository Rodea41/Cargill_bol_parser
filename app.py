from math import pi
import re

import PyPDF2 as pdf2

with open ("bol.pdf", "rb") as f:
   pdf = pdf2.PdfFileReader(f)
   page = pdf.numPages
   first_pg = pdf.getPage(0)
   first_text = first_pg.extract_text()

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


   #print(prodmatch)
   for items in net_weight:
      print(items)
      print("-------------------")



   #print(type(matches))
   #for items in has_CTN:
     #print(items)



useRegex(first_text)