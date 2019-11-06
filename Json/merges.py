import os,json
prefix=(input("Enter the Prefix data:").strip()).encode(encoding='utf-8').decode('ascii')
output=input("Enter the output file name:").strip()
dirname="E:\Freshworks\Json"
output_filename = output.encode(encoding='utf-8').decode('ascii')+".json"
# s.encode(encoding='utf-8').decode('ascii')
merge_dict={}
for filename in os.listdir(dirname):
    root, ext = os.path.splitext(filename)
    if root.startswith(prefix) and ext == '.json':
        with open(filename, 'r') as f:
            temp_dict = json.load(f)
            for x in temp_dict.items():
                if x[0] not in merge_dict:
                    merge_dict[x[0]]=[]
                    for temp in x[1]:
                        merge_dict[x[0]].append(temp)
                else:
                     for temp in x[1]:
                        merge_dict[x[0]].append(temp)   
with open(output_filename, 'w') as fp:
    json.dump(merge_dict, fp)                           
               
    

    
