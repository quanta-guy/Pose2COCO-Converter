import os
import glob

filelist=os.listdir('I:/Work/Pragatheesh/rework disable/ref')
print(filelist)
for i in filelist:
    png_del= glob.glob('I:/Work/Pragatheesh/rework disable/root/'+i)
   
    if(len(png_del)):
        os.remove(png_del[0])
    i=i[:-4]
    json_del= glob.glob('I:/Work/Pragatheesh/rework disable/json/'+i+'??????????.json')
    json_del[0].replace("\\", "/")
    if(len(json_del)):    
        os.remove(json_del[0])
#source = 'I:/Work/Pragadeesh/Dummy 2/nfd 2set-9.json'
  
# Destination path 
#destination = 'I:/Work/Pragadeesh/Dummy 1/'

#shutil.move(source,destination)



""" def remap(input_list):
    grouped_list = [input_list[i:i + 3] for i in range(0, len(input_list), 3)]
    remapped_indices = {
        1: 1,
        2: 2,
        3: 3,
        5: 4,
        7: 5,
        4: 6,
        6: 7,
        8: 8,
        9: 9,
        10: 10,
        12: 11,
        14: 12,
        11: 13,
        13: 14,
        15: 15
    }

    new_list = [grouped_list[remapped_indices[i] - 1] for i in range(1, len(remapped_indices) + 1)]

    output_list = [elem for sublist in new_list for elem in sublist]

    return output_list

j = 0
path_to_json_files = 'I:/Work/Pragadeesh/53 json from openpose/'
json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

with open('C:/Users/vkant/OneDrive/Desktop/nfd 2set-9.json') as f:
    out_data = json.load(f)

x = out_data['annotations']

for i in range(1, len(x), 2):
    temp = x[i]
    keypoints_data = temp['keypoints']
    with open(path_to_json_files + json_file_names[j]) as f:
        data = json.load(f)
    raw_data = data['people']
    j += 1

    for k in range(len(raw_data)):
        remap_data = raw_data[k]
        remapped = remap(remap_data['pose_keypoints_2d'])
        keypoints_data = remapped  


with open('C:/Users/vkant/OneDrive/Desktop/nfd 2set-9.json', 'w') as f:
    json.dump(out_data, f) """