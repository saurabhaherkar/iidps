import os

from scipy.sparse import lil_matrix
from sklearn.decomposition import TruncatedSVD
import numpy

numpy.set_printoptions(threshold=numpy.inf)

normal_dir = "dataset/normal"
malicious_dir = "dataset/malicious"


def getarray(tlist, MasterIndex):
    n = len(MasterIndex)
    matrix = lil_matrix((n, n))

    previndex = -1
    for i in range(len(tlist)):
        index = MasterIndex.index(tlist[i])
        if previndex == -1:
            previndex = index
            continue
        matrix[previndex, index] += 1
        previndex = index
        # print(previndex,index,matrix[previndex,index])

    # print(matrix.todense())

    svd = TruncatedSVD(n_components=20)
    svd.fit(matrix)
    return svd.singular_values_
    # return svd.transform(matrix)


def parse_file(file):
    sclist = []
    with open(file, "r") as f:
        contents = f.readlines()[1:]
        for line in contents:
            try:
                start = line.index('(')
                sc = line[0: start]
                if ',' in line:
                    index1 = line.index(',')
                    param = line[start + 1: index1]
                else:
                    end = line.index(')')
                    param = line[start + 1: end]
                sclist.append([sc, param])
            except:
                pass
    return sclist


map = {}


def main():
    lst_normal = os.listdir(normal_dir)
    lst_malicious = os.listdir(malicious_dir)

    AllContents = []

    map['normal'] = []
    map['malicious'] = []

    set1 = set()
    for file in lst_normal:
        if file.endswith(".trace"):
            sclist = parse_file(normal_dir + '/' + file)
            tlist = []
            for sc, param in sclist:
                # set1.add(sc)
                AllContents.append(sc)
                tlist.append(sc)
                # AllContents.append(sc + ':' + param)
                # tlist.append(sc + ':' + param)
            map['normal'].append(tlist)

    for file in lst_malicious:
        if file.endswith(".trace"):
            sclist = parse_file(malicious_dir + '/' + file)
            tlist = []
            for sc, param in sclist:
                # set1.add(sc)
                AllContents.append(sc)
                tlist.append(sc)
                # AllContents.append(sc + ':' + param)
                # tlist.append(sc + ':' + param)
            map['malicious'].append(tlist)

    MasterIndex = list(set(AllContents))
    MasterIndex.sort()

    for t in map.keys():
        for tlist in map[t]:
            arr = getarray(tlist, MasterIndex)
            print(t, arr)

    print('Total indices', len(MasterIndex))
    #
    # print(map)
    #
    # print("Total Length of List: " + str(len(AllContents)))
    # print("Total Length of Set: " + str(len(set1)))
    # print()
    #
    # # for i in set1:
    # #     print(i)
    #
    # set2 = set(AllContents)
    # print(len(set2))
    # print(set2)
    #
    #
    # print('MasterIndex', MasterIndex)


if __name__ == '__main__':
    main()
