import os
import json
file_path="E:/ZewailCity/Grad Proj/Uefa Champions league/2014-2015/2014-11-05 - 22-45 Manchester City 1 - 2 CSKA Moscow/Labels-v2.json"  
new_file="updated_"+file_path.split('.')[0]+".json"   ##new file will be created 
dict={"UrlLocal":'',"UrlYoutube":'',"annotations":[]}
with open(file_path, 'r') as f:
     data= json.load(f)
     annotations=data["annotations"]
dict['UrlLocal']=data['UrlLocal']
dict["UrlYoutube"]=data["UrlYoutube"]
sub_count=0
flag=False
sub=False
temp=0
for i, annotation in enumerate(annotations):
    if annotation["label"] == "Ball out of play" or annotation["label"] == "Foul":
        temp=i
        flag=True
    
    if annotation["label"] == "Substitution" and flag==True:
        sub_count+=1
        sub=True
    
    
    if annotation["label"] == "Penalty" :
        if annotations[i-1]["label"] == "Foul":
            del annotations[i]
            annotations[i-1]["label"] = "Penalty"
        elif sub:
            del annotations[i]
            annotations[temp]["label"] = "Penalty"
        else:
            print("action problem found in: "+file_path+ "game_time_to_search "+annotations[i]["gameTime"])
        flag=False
        sub=False
        sub_count=0
        
    elif annotation["label"] == "Corner":
        
        if annotations[i-1]["label"] == "Ball out of play":
            annotations[i-1]["team"] = annotations[i]["team"]
            del annotations[i]
            annotations[i-1]["label"] = "Corner"
            
        
        elif sub:
            annotations[temp]["team"] = annotations[i]["team"]
            del annotations[i]
            annotations[temp]["label"] = "Corner"
        else:
            print("action problem found in: "+file_path+ "game_time_to_search"+annotations[i]["gameTime"])
        flag=False
        sub=False
        sub_count=0

     
    elif annotation["label"] == "Clearance" :
        if annotations[i-1]["label"] == "Ball out of play":
           annotations[i-1]["label"] = "Goal kick"
           annotations[i-1]["team"] = annotations[i]["team"]
        elif sub:
            annotations[temp]["label"] = "Goal kick"

        flag=False
        sub=False
        sub_count=0

    elif annotation["label"] != "Substitution" and annotation["label"] != "Ball out of play" and annotation["label"] != "Foul":
       
        flag=False
        sub=False
        sub_count=0


with open(new_file, 'w') as f:
    dict["annotations"]=annotations
    json.dump(dict, f,indent=4)