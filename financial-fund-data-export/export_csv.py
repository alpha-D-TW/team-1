import json
import random
import csv

# 读取原始 JSON 文件并筛选字段
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 随机打乱基金数据
random.shuffle(data)

# 存储所有基金信息的列表
funds = []

for fund in data:
    risk = fund['risk']
    annual_return_rate = round(random.uniform(0, 100), 4)  # 生成随机年度回报率
    fund_data = {
        'name': fund['name'],
        'shortName': fund['shortName'],
        'code': fund['code'],
        'risk': fund['risk'],
        'ForhbinfoUrl': fund['ForhbinfoUrl'],
        'annualReturnRate': round(annual_return_rate / 100, 2)
    }
    funds.append(fund_data)

# 将所有基金信息导出到 CSV 文件中
csv_columns = ['name', 'shortName', 'code', 'risk', 'ForhbinfoUrl', 'annualReturnRate']
csv_file = 'dist/funds.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()
    for fund in funds:
        writer.writerow(fund)

print("Generated CSV file:", csv_file)
