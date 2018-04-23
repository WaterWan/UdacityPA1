"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
market_nums = set()
not_market_nums = set()
for call in calls:
    incoming_num = call[0]
    if not incoming_num.startswith('140'):
        continue
    market_nums.add(incoming_num)

for call in calls:
    answering_num = call[1]
    if not answering_num.startswith('140'):
        continue
    not_market_nums.add(answering_num)

for text in texts:
    incoming_number = text[0]
    if incoming_number.startswith('140'):
        not_market_nums.add(incoming_number)
    answering_number = text[1]
    if answering_number.startswith('140'):
        not_market_nums.add(answering_number)

market_nums -= not_market_nums
sorted_marketer_num = sorted(market_nums)
print("These numbers could be telemarketers: ")
for num in sorted_marketer_num:
    print(num)