import os,json,sys
from os import path
prefix=(input("Enter the Prefix data:").strip()).encode(encoding='utf-8').decode('ascii')
output=input("Enter the output file name:").strip()
dirname=input("Enter the path where files are stored:")
file_size=int(input("Enter the size of the file:"))
output_file_counter=1
output_filename = output
output_filename+=str(output_file_counter)
output_filename = output_filename.encode(encoding='utf-8').decode('ascii')+".json"
merge_dict={}
for filename in os.listdir(dirname):
    root, ext = os.path.splitext(filename)
    if root.startswith(prefix) and ext == '.json':
        with open(filename, 'r') as f:
            temp_dict = json.load(f)
            for x in temp_dict.items():
                if int(sys.getsizeof(merge_dict)) > file_size :
                        with open(output_filename, 'w') as fp:
                            json.dump(merge_dict, fp)
                            output_file_counter += 1
                            output_filename = output
                            output_filename+=str(output_file_counter)
                            output_filename = output_filename.encode(encoding='utf-8').decode('ascii')+".json"
                            merge_dict={}
                if x[0] not in merge_dict:
                    merge_dict[x[0]]=[]
                    for temp in x[1]:
                        merge_dict[x[0]].append(temp)
                else:
                     for temp in x[1]:
                        merge_dict[x[0]].append(temp)                                   
with open(output_filename, 'w') as fp:
    json.dump(merge_dict, fp)                           
               
    

    
