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

callers = set()
telemarketers = set()
for call in calls:
    callers.add(call[0])

for caller in callers:
    exist_flag = False
    # check in texts
    for text in texts:
        if caller == text[0] or caller == text[1]:
            exist_flag = True

    # check in calls
    for call in calls:
        if caller == call[1]:
            exist_flag = True

    if exist_flag == False:
        telemarketers.add(caller)

result = sorted(telemarketers)

print("These numbers could be telemarketers: ")

for telemarketer in result:
    print(telemarketer)

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

