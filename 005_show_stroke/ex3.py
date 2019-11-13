coding = 'utf-8'

import xlrd
import json

skrokes = []
result = {}
workbook = xlrd.open_workbook("汉字笔画数.xls")

names = workbook.sheet_names()
print(names)
worksheet=workbook.sheet_by_name("汉字笔划")
print(worksheet.name)
nrows=worksheet.nrows  #获取该表总行数
print(nrows)
ncols=worksheet.ncols  #获取该表总列数
print(ncols)

#遍历第二列　找到所有笔画的数字
for i in range(1,nrows):
    skroke = int(worksheet.row_values(i)[1])
    print(skroke)
    if skroke not in skrokes:
        skrokes.append(skroke)
print(skrokes)

#创建字典的形状
for sk in skrokes:
    result[str(sk)] = ""
print(result)

#遍历表　进行统计
for i in range(1,nrows): #循环打印每一行
    # print(worksheet.row_values(i)) #以列表形式读出，列表中的每一项是str类型
    word,sk = worksheet.row_values(i)[0] ,int(worksheet.row_values(i)[1])
    result[str(sk)] += word

print(result)

#转为json,保存
json = json.dumps(result,ensure_ascii=False,indent=4)
with open("resule.json",'w') as f:
    f.write(json)






#col_data=worksheet.col_values(0)  #获取第一列的内容
#print(col_data)

