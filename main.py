#1 generate quote list
import csv
quote_list=[]
with open("/Users/ritu/Downloads/quote.csv",mode ='r') as file:
	csv_file=csv.reader(file)
	for row in csv_file:
		quote=row[0].replace("-"," ")
		quote_list.append(quote)




#2 call script
from script import convert
import uuid
for quote in quote_list:
	img=convert(quote=quote,author=None,fg="white",image="asset/background.png",border_color="black",font_size=42,font_file="asset/times.ttf",width=1080,height=1080)
	image_name=str(uuid.uuid4())+".png"
	image_path="/Users/ritu/Downloads/quote/"
	img.save(image_path+image_name)
			
	
		
		






   
  
	
			
	

        