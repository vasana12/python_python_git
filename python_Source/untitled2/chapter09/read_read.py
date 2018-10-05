if __name__=='__main__':
    fp=open("text.txt", "rt", encoding="utf-8")
    contents = fp.read()
    print(contents)
    fp.close()

    fr=open("text.txt", "rt", encoding="utf-8")
    rr=fr.readlines()
    for lsts in rr:
        print(lsts,end="")
    fr.close()