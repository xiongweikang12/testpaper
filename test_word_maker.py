# TODO  type content answer analysis
import pandas as pd
import re
import tkinter as tk

#读取txt文本
with open('test_word.txt', 'r',encoding='utf-8') as test_string:
    test_string_l = test_string.readlines()
    print(test_string_l)

#获取答案，获取题目的索引list_kon，stl替换答案为空的string（题目）列表
def get_answer(string):
    stl=string
    list_kon=[]
    answer=[]
    for i in range(len(string)):
        if (bool(re.match(r'\d.+?',string[i]))):
            # print(string[i])
            if (bool(re.search('([ABCD])',string[i]))):
                # theme.append(re.sub('([ABCD])','',string[i]))
                answer.append((re.findall('([ABCD])',string[i]))[0])
                list_kon.append(i)
                stl[i] = (re.sub('([ABCD])', '', string[i]))


    print(stl)
    print(list_kon)

    return stl ,list_kon,answer

#通过list_on,string通过索引得到，两个题目之间的内容（选项）
def get_content(string, list_k):
    content = []
    for k in range(len(list_k)):
        try:
            (string[list_k[k]:list_k[k + 1]])
        except IndexError:
            content.append(string[list_k[-1]:])
        else:
            content.append(string[list_k[k]:list_k[k + 1]])

    print(content)
    return content

    # return answer,theme,list_kon

                # if (''in list(re.findall(r'[(](.*?)[)]',string[i][0]))):
                #     answer.append(re.findall(r'[(](.*?)[)]')),string[i][0].replace(" ","")

# answer,theme=get_answer(test_string_l)
#通过遍历答案，得到新的type列表
def get_type(answer_list):
    list_type_answer=[]
    for answer_1 in answer_list:
        if len(answer_1)==1:
            list_type_answer.append("单选题")
        if len(answer_1)>1:
            list_type_answer.append("多选题")
    return list_type_answer



def get_all_content():
    string_k,list_k,answer_k=get_answer(test_string_l)
    content_k=get_content(test_string_l,list_k)
    type_k=get_type(answer_k)
    content_all=[]

    for p in content_k:
        content_part=''
        for p_into in p:
            content_part+=p_into
        content_all.append(content_part)
    print(content_all)

    #TODO 将其创建dataframe,导出excel表格

    sheet_work=pd.DataFrame(columns=['type','content','answer','analysis'])
    sheet_work['type']=type_k
    sheet_work['content']=content_all
    sheet_work['answer']=answer_k
    sheet_work['analysis']=0



    return sheet_work
def to_excel():
    global sheet_name
    global file_name
    one_sheet=get_all_content()
    # sheet_name=input('请输入表名:')
    # file_name=input('请输入文件名:')
    file_name=file_name+'.xls'

    one_sheet.to_excel(file_name,sheet_name=sheet_name)

# homework_sheet.to_excel('speed_px.xls', sheet_name='速度_密度 线性回归')

# if __name__=="__main__":
#     to_excel()
root=tk.Tk()
root.title('对分易试卷转换')
root.geometry('250x150')
l1=tk.Label(root,text='sheet name')
l1.grid(row=0,column=0)
l2=tk.Label(root,text='file name')
l2.grid(row=1,column=0)
entry_sheet=tk.Entry(root,show=None)
entry_sheet.grid(row=0,column=1)
entry_file=tk.Entry(root,show=None)
entry_file.grid(row=1,column=1)
def set_name():
    global sheet_name
    global file_name
    sheet_name=entry_sheet.get()
    file_name=entry_file.get()
    if sheet_name and file_name:
        to_excel()

start_1=tk.Button(root,text='开始转换',width=10,height=1,bg='red',command=set_name)
start_1.grid(row=2,column=1)
quit_=tk.Button(root,text='退出',width=10,height=1,command=quit)
quit_.grid(row=3,column=1)
root.mainloop()

































