import json

# 读取JSON文件
with open('preview.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 按照risk的值分类数据，并将数据写入txt文件
for item in data:
    page_content = item.get('page_content', '')
    risk_start_index = page_content.find('risk:')
    if risk_start_index != -1:
        risk_end_index = page_content.find('\n', risk_start_index)
        if risk_end_index != -1:
            risk = page_content[risk_start_index + len('risk:'):risk_end_index].strip()
            txt_filename = f"dist/{risk}.txt"
            with open(txt_filename, 'a', encoding='utf-8') as txt_file:
                txt_file.write('"' + page_content.replace('\n', '\\n') + '"' + '\n')
