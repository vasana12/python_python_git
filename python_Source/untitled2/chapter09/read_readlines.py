if __name__=='__main__':
    fp =open("text.txt", "rt", encoding="utf-8")
    lines = fp.readlines()
    print(lines)
    fp.close

