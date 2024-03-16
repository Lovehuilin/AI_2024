import re
def compare_and_map(expr1, expr2):
    """
    比较两个表达式expr1和expr2，考虑函数名可能相差一个'~'，并比较参数列表。
    返回所有可能的变量到常量的映射列表，或特定的消息。
    """
    expr1 = expr1.replace(' ', '')
    expr2 = expr2.replace(' ', '')
    pattern = re.compile(r'([~]?[A-Za-z]+)\(([^)]+)\)')
    match1 = pattern.match(expr1)
    match2 = pattern.match(expr2)

    if not match1 or not match2:
        return "格式不匹配"

    func1, args1 = match1.groups()
    func2, args2 = match2.groups()

    # 检查函数名是否满足条件
    if func1 != func2 and func1.strip('~') != func2.strip('~'):
        return "函数名不匹配"

    args1 = args1.split(',')
    args2 = args2.split(',')

    if len(args1) != len(args2):
        return "参数数量不匹配"

    variables = {'x', 'y', 'z', 'u', 'v', 'w'}
    mappings = []

    for arg1, arg2 in zip(args1, args2):
        arg1, arg2 = arg1.strip(), arg2.strip()
        if arg1 in variables and arg2 not in variables:
            mappings.append(f'{arg1} = {arg2}')
        elif arg2 in variables and arg1 not in variables:
            mappings.append(f'{arg2} = {arg1}')
        elif arg1 in variables and arg2 in variables:
            if arg1 != arg2:
                return False
            continue
        elif arg1 != arg2:
            return False

    if not mappings:
        return None
    return '; '.join(mappings)

# 示例
expr1 = "~F(y)"
expr2 = "F(x)"
print(compare_and_map(expr1, expr2))
