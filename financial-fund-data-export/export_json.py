import json
import random

# 读取原始 JSON 文件并筛选字段
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 初始化风险等级对应的年度回报率范围
risk_ranges = {
    'R1': (0.1, 2),
    'R2': (2, 5),
    'R3': (-5, 10),
    'R4': (-10, 20),
    'R5': (-20, 66)
}

# 存储所有基金信息的列表
funds = []

# 为每个基金生成年度回报率并添加到列表中
for fund in data:
    risk = fund['risk']
    annual_return_rate = round(random.uniform(*risk_ranges[risk]), 4)  # 生成随机年度回报率
    fund_data = {
        'name': fund['name'],
        'orgName': '广发基金管理有限公司',
        'risk': fund['risk'],
        'ForhbinfoUrl': fund['ForhbinfoUrl'],
        'code': fund['code'],
        'typeCode': fund['typeCode'],
        'subType': fund['subType'],
        'orgCode': fund['orgCode'],
        'buyRate': fund['buyRate'],
        'redeemRate': fund['redeemRate'],
        'manageRate': fund['manageRate'],
        'subscribeRate': fund['subscribeRate'],
        'annualReturnRate': round(annual_return_rate / 100, 2)
    }
    funds.append(fund_data)

# 将所有基金信息导出到同一个 JSONL 文件中
with open('json/funds.jsonl.txt', 'w', encoding='utf-8') as file:
    for entry in funds:
        json.dump(entry, file, ensure_ascii=False)
        file.write('\n')

print("Generated.")
