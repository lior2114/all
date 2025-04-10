def some_matriz(mat):
    if len(mat) == 0:
        raise ValueError ("empty matriz! (in function)")
    lis = []
    for i in mat:
        for j in i:
            j_new = str(j)
            if not j_new.isdigit():
                raise ValueError ("enter only numbers! (function j)")
            lis.append(j)
    return lis