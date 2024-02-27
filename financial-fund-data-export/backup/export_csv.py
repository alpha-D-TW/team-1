import json
import random
import csv

# 读取原始 JSON 文件并筛选字段
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 对基金数据按照 risk 排序
data.sort(key=lambda x: x['risk'])

# 存储已导出的基金数量，按照 risk 类型记录
exported_counts = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0}

# 存储导出的基金信息
exported_funds = []

# 遍历基金数据，按照要求选择导出的数据
for fund in data:
    risk = fund['risk']
    if exported_counts[risk] < 50:  # 检查该风险等级已导出的基金数量是否已经达到了 5 条
        annual_return_rate = round(random.uniform(0, 100), 4)  # 生成随机年度回报率
        fund_data = {
            'name': fund['name'],
            'shortName': fund['shortName'],
            'code': fund['code'],
            'risk': risk,
            'ForhbinfoUrl': fund['ForhbinfoUrl'],
            'annualReturnRate': round(annual_return_rate / 100, 2)
        }
        exported_funds.append(fund_data)
        exported_counts[risk] += 1  # 更新已导出的基金数量

# 将导出的基金信息导出到 CSV 文件中
csv_columns = ['name', 'shortName', 'code', 'risk', 'ForhbinfoUrl', 'annualReturnRate']
csv_file = 'dist/funds.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()
    for fund in exported_funds:
        writer.writerow(fund)

print("Generated CSV file:", csv_file)
