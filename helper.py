def read_file(path):
    f = open(path, "r", encoding="utf-8")
    t = f.read()
    f.close()
    return t
