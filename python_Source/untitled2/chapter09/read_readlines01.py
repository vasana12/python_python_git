if __name__=='__main__':
    fp = open("text.txt", "rt", encoding="utf-8")
    lines=fp.readlines() #개행문자를 기준으로 리스트 형식으로 반환

    for line in lines:
        print(line, end="")

        fp.close()
