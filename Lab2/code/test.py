def parse_element(element):
    """简单解析元素，假设格式为 'A(x)' """
    func, vars = element.split('(')
    vars = vars.rstrip(')')
    return func, vars.split(',')

def can_unify(element1, element2):
    """检查是否可以合一化，并返回合一化方案，如果不可以则返回None"""
    func1, vars1 = parse_element(element1)
    func2, vars2 = parse_element(element2)
    if func1 != func2 or len(vars1) != len(vars2):
        return None
    substitution = {}
    for var1, var2 in zip(vars1, vars2):
        if var1.islower():  # 假设变量是小写的
            substitution[var1] = var2
        elif var1 != var2:
            return None
    return substitution

# 假设集合
clauses = {
    ('A(mike)',),
    ('A(tony)',),
}

# 遍历集合中的每个元组
for clause1 in clauses:
    for element1 in clause1:
        for clause2 in clauses:
            if clause1 != clause2:
                for element2 in clause2:
                    # 尝试合一化
                    substitution = can_unify(element1, element2)
                    if substitution:
                        print(f"可以合一化: {element1} 和 {element2} 使用 {substitution}")
