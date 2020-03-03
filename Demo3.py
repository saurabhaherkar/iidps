import os 
import random 
import shutil

# def random_file(file):
#     lines = open(file).read().splitlines()
#     return random.choice(lines)

out = []
O = list(out)
files = os.listdir('C:\\Users\\Saurabh Ahekar\\PycharmProjects\\IIDPS\\dataset\\malicious\\')
# for file in files:
#     content = open('C:\\Users\\Saurabh Ahekar\\PycharmProjects\\IIDPS\\dataset\\malicious\\'+file, 'r')
#     # print(content.readline())
#     with open(content) as f:
#         with open('output.trace', 'w') as fp:
#             fp.writelines(content)
# print(len(res))
# print(res)
# for file in files:
#     with open(file) as f:
#         with open('output.trace', 'w') as fp:
#             for lines in f:
#                 for lines1 in f:
#                     if lines[0:] == lines1[0:]:
#                         fp.writelines(lines[0:])
li = []
for file in files:
    content = open('C:\\Users\\Saurabh Ahekar\\PycharmProjects\\IIDPS\\dataset\\malicious\\'+file, 'r')
    for lines in content:
        with open('dup_df.trace', 'w') as fp:
            fp.write(lines[0:])
            for i in content:
                fp.write(i)
            break
            
