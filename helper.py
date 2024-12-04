def read_file(file_name):
    t = file_name.split('\\')[-1].strip(".py")
    path = f"./input/{t}.txt"
    f = open(path, "r", encoding="utf-8")
    t = f.read().strip()
    f.close()
    return t
