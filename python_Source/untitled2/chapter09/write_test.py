if __name__=='__main__':
    fp= open("text.txt", "wt", encoding="utf-8")
    fp.write("%d\n" %1)
    fp.write("%.2f\n" %3.14)
    fp.write("Hello World\n")
    fp.write("안녕 파이썬")
    fp.close()
