import os,json

def remap(input_list):
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
path_to_json_files = 'I:/Work/Pragatheesh/1 nfd/'
json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

with open('I:/Work/Pragatheesh/nfd coco/NFD root-15.json') as f:
    out_data = json.load(f)

x = out_data['annotations']

for i in range(1, len(x), 2):
    temp = x[i]
    keypoints_data = temp['keypoints']
    with open(path_to_json_files + json_file_names[j]) as f:
        data = json.load(f)
    raw_data = data['people']
    j += 1

    for k in range(0,len(raw_data)):
        remap_data = raw_data[k]
        remapped = remap(remap_data['pose_keypoints_2d'])
        keypoints_data[:]= remapped  
        print(keypoints_data[i])

with open('I:/Work/Pragatheesh/nfd coco/NFD root-15.json', 'w') as f:
    json.dump(out_data, f) 