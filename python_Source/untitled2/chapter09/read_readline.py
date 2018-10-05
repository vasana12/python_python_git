if __name__=="__main__":
    fp = open("text.txt", "rt", encoding="utf-8")
    line= fp.readline()
    print(line, end="") #print(line.strip()) <- 줄바꿈 문자가 이미 포함되어 있는데 그걸 없애는 것
    line=fp.readline()
    print(line.strip())
    line=fp.readline()
    print(line.strip())
    line=fp.readline()
    print(line.strip())
    fp.close()

