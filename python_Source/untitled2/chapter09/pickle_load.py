import pickle,os

if __name__=="__main__":
    # fp = open('binary.dat', "rb")
    # data=pickle.load(fp)
    # print(data)
    # data=pickle.load(fp)
    # print(data)
    # data=pickle.load(fp)
    # print(data)
    # data=pickle.load(fp)
    # print(data)
    # data=pickle.load(fp)
    # print(data)
    # data=pickle.load(fp)
    # print(data)
    # data=pickle.load(fp)
    # print(data)
    # fp.close()

    fp = open('binary.ddat', "rb")
    while True:

        if (fp.tell()==os.fstat(fp.fileno()).st_size):
            break
        data = pickle.load(fp)
        print(data)
    fp.close()