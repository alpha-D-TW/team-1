import json
import random
import os


dist = 'dist/funds-chunks'
if os.path.exists(dist):
    for filename in os.listdir(dist):
        filepath = os.path.join(dist, filename)
        os.remove(filepath)
else:
    os.makedirs(dist)


with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


risk_ranges = {
    'R1': (0.1, 2),
    'R2': (2, 5),
    'R3': (-5, 10),
    'R4': (-10, 20),
    'R5': (-20, 66)
}


data.sort(key=lambda x: x['risk'])

exported_counts = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0}
file_counts = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0}

n_limit=50 # 每个类型的总数限制
n_chunk=30 # 文件切片条数

for fund in data:
    risk = fund['risk']
    if exported_counts[risk] < n_limit:  
        if exported_counts[risk] % n_chunk == 0:  
            file_counts[risk] += 1
            txt_file = f'{dist}/{risk}.{file_counts[risk]:02d}.txt'
            file = open(txt_file, 'w', encoding='utf-8')
        
        annual_return_rate = round(random.uniform(*risk_ranges[risk]), 4)
        
        file.write(f"name: {fund['name']}\\n")
        file.write(f"shortName: {fund['shortName']}\\n")
        file.write(f"code: {fund['code']}\\n")
        file.write(f"risk: {fund['risk']}\\n")
        file.write(f"annualReturnRate: {annual_return_rate}\\n\n")
        exported_counts[risk] += 1  
        if exported_counts[risk] % n_chunk == 0:  
            file.close()

print("Generated txt files.")
