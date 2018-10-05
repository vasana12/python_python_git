if __name__ =='__main__':
    fp = open("text.txt", "rt", encoding="utf-8")

    while True:
        line = fp.readline()
        if line == '':
            break
        print(line.strip()) #또는 print(line, end='')
    fp.close()
