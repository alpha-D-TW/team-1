import json
import random
import os

# 删除目标目录并重新创建
dist = 'dist/funds-chunks'
if os.path.exists(dist):
    for filename in os.listdir(dist):
        filepath = os.path.join(dist, filename)
        os.remove(filepath)
else:
    os.makedirs(dist)

# 读取原始 JSON 文件并筛选字段
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 风险等级对应的年度回报率范围
risk_ranges = {
    'R1': (0.1, 2),
    'R2': (2, 5),
    'R3': (-5, 10),
    'R4': (-10, 20),
    'R5': (-20, 66)
}

# 对基金数据按照 risk 排序
data.sort(key=lambda x: x['risk'])

# 存储每种 risk 类型已导出的基金数量
exported_counts = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0}

# 存储每种 risk 类型已导出的文件数量
file_counts = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0}

# 遍历基金数据，按照要求选择导出的数据，并写入对应的 txt 文件
for fund in data:
    risk = fund['risk']
    if exported_counts[risk] < 50:  # 检查该风险等级已导出的基金数量是否已经达到了 50 条
        if exported_counts[risk] % 5 == 0:  # 每5条数据创建一个新文件
            file_counts[risk] += 1
            txt_file = f'{dist}/{risk}.{file_counts[risk]:02d}.txt'
            file = open(txt_file, 'w', encoding='utf-8')
        # 生成随机的 annualReturnRate 值
        annual_return_rate = round(random.uniform(*risk_ranges[risk]), 4)
        # 将基金信息按指定格式写入文件
        file.write(f"name: {fund['name']}\\n")
        file.write(f"shortName: {fund['shortName']}\\n")
        file.write(f"code: {fund['code']}\\n")
        file.write(f"risk: {fund['risk']}\\n")
        file.write(f"ForhbinfoUrl: {fund['ForhbinfoUrl']}\\n")
        file.write(f"annualReturnRate: {annual_return_rate}\\n\n")
        exported_counts[risk] += 1  # 更新已导出的基金数量
        if exported_counts[risk] % 5 == 0:  # 关闭文件，达到每 5 条数据一个文件的要求
            file.close()

print("Generated txt files.")
