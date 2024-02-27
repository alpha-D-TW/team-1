import json
import random

# 读取原始JSON文件
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

# 为每个基金生成年度回报率并分类
funds_by_risk = {risk: [] for risk in risk_ranges}

for fund in data:
    risk = fund['risk']
    annual_return_rate = round(random.uniform(*risk_ranges[risk]), 4)  # 生成随机年度回报率
    fund['annualReturnRate'] = round(annual_return_rate / 100, 2)  # 添加到基金信息中
    fund['orgName'] = '广发基金管理有限公司'
    funds_by_risk[risk].append(fund)

# 将分类后的基金信息导出到不同的JSON文件
for risk, funds in funds_by_risk.items():
    with open(f'json/{risk}.jsonl', 'w', encoding='utf-8') as file:
        for entry in funds:
            json.dump(entry, file, ensure_ascii=False)
            file.write('\n')

print("Generated.")
