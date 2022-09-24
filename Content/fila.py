def isFull(f):
    return False

def isEmpty(f):
    if len(f) == 0:
        return True
    return False    

def put(f, info):
    f.append(info)

def get(f):
    return f.pop(0)

def peek(f):
    return f[0]    