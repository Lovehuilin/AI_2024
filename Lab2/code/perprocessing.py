"""
Project: ResolutionFOL.
Author : Jason Rao
Time   : 24-03-23
"""

"""
    存储公式的python数据结构：
    用字符串存储
    符号¬用‘~’代替
    谓词的首字母大写, 例如用A, B, C, P1, P2, Student等表示; 
    谓词的每个参数之间用逗号“,”间隔且不加空格
    常量用小写单词或a, b, c等小写字母表示;
    本次作业的公式中不含∃,∀量词符号
    例子: ¬child存储为 “~child” boy存储为“boy”
    几个公式: “R(a)”, “~P(a,zz)”, “Student(tony)”. 这里应该将a,tony
    看做常量,将zz看做变量
"""

"""
    :param clause_num: int 输入的子句集总数
    :param clause_set: set{tuple} 所有输入的子句集以元组存储在集合中
    :param clause: tuple 输入的子句集元组，元素为每个子句
    :param clause_str: 输入的子句集的字符串形式
"""
# 合一化判断及处理
"""
def is_unifiable(element1, element2):
    predicate1, t1 = element1.split('(')
    predicate2, t2 = element2.split('(')
    t1.replace(')', '')
    t2.replace(')', '')
    if (predicate2 - predicate1 == '~' or predicate1 - predicate2 == '~'):
        
    else:
        return False
"""


# 处理输入字符串为子句集集合
import re
class text:
    def preprocessing():
        clause_num = int(input()) # clause_num: number of clauses
        clause_set = set() # clause_set: set of clauses
        for cnt in range(clause_num):
            clause = () # clause: every single clause
            clause_str = input().replace(' ', '')
            if clause_str[0] == '(' and clause_str[-1] == ')':
                clause_str = clause_str[1:-1].replace('¬', '~').strip()
            clause_set.add(tuple(re.split(r'(?<=\)),', clause_str)))
        return clause_set
