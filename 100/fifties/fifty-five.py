# -*- coding: utf-8 -*-

# functions
def reverse_number(a):
    """
    """
    return int(str(a)[::-1])

def add_reverse(a):
    """
    """
    return reverse_number(a) + a

def is_palendrome(a):
    """
    """
    return str(a) == str(a)[::-1]

def is_lychrel(n, c=0):
    """
    """
    if c > 50:
        return True
    
    else:
        new_n = add_reverse(n)
        #print new_n
        if is_palendrome(new_n):
            return False
        else:
            return is_lychrel(new_n, c+1)

ans = sum([is_lychrel(x) for x in range(0, 10000)])
print ans  # 249
