def is_var(x):
    if (x == 'x' or x == 'y' or x == 'z'):
        return True
    elif (x == 'u' or x == 'v' or x == 'w'):
        return True
    else:
        return False

def unify_atoms(L1, L2):
    # 若L1或L2为一原子
    if isinstance(L1, tuple) and isinstance(L2, tuple) and len(L1) == 1 and len(L2) == 1:
        atom1, atom2 = L1[0], L2[0]
        
        # 若L1和L2恒等
        if atom1 == atom2:
            return "NIL"
        
        # 检查是否为变量形式，假设变量形式为'A(x)'等
        if "(" in atom1 and ")" in atom1:
            var1 = atom1[atom1.find("(")+1:atom1.find(")")]
        else:
            var1 = None
            
        if "(" in atom2 and ")" in atom2:
            var2 = atom2[atom2.find("(")+1:atom2.find(")")]
        else:
            var2 = None
        
        # 若L1为一变量
        if var1 and is_var(var1):
            # 若L1出现在L2中
            if var1 in atom2:
                return "F"
            else:
                return (atom1.replace(var1, var2), var1, var2)
        
        # 若L2为一变量
        if var2 and is_var(var2):
            # 若L2出现在L1中
            if var2 in atom1:
                return "F"
            else:
                return (atom2.replace(var2, var1), var2, var1)
        
    # 否则返回F
    return "F"

# 示例测试
print(unify_atoms(('A(x)',), ('L(tony)',)))
