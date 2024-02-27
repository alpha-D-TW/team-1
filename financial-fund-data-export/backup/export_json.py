import json
import random

# 读取原始 JSON 文件并筛选字段
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

LIMIT=20

# 初始化风险等级对应的年度回报率范围
risk_ranges = {
    'R1': (0.1, 2),
    'R2': (2, 5),
    'R3': (-5, 10),
    'R4': (-10, 20),
    'R5': (-20, 66)
}

# 存储所有基金信息的字典，按照风险等级分组
funds_by_risk = {risk: [] for risk in risk_ranges}

# 为每个基金生成年度回报率并添加到相应的风险等级组中
for fund in data:
    risk = fund['risk']
    if len(funds_by_risk[risk]) < LIMIT:  # 检查该风险等级下的基金数量是否已经达到了 ? 条
        annual_return_rate = round(random.uniform(*risk_ranges[risk]), 4)  # 生成随机年度回报率
        fund_data = {
            'name': fund['name'],
            'name': fund['shortName'],
            'code': fund['code'],
            'risk': fund['risk'],
            'ForhbinfoUrl': fund['ForhbinfoUrl'],
            'annualReturnRate': round(annual_return_rate / 100, 2)
        }
        funds_by_risk[risk].append(fund_data)

# 将分类后的基金信息导出到同一个 JSONL 文件中
with open('dist/funds-limit-by-risk.jsonl.txt', 'w', encoding='utf-8') as file:
    for funds in funds_by_risk.values():
        for entry in funds:
            json.dump(entry, file, ensure_ascii=False, separators=(',', ':'))
            file.write('\n')

print("Generated.")
