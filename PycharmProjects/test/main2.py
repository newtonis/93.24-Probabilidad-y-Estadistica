
import numpy
import matplotlib.pyplot as plt


def comp_m(n, m):
    items = numpy.random.permutation(range(1, n+1))[:m]
    max_value = 0
    for val in items:
        max_value = max(max_value, val)
    return max_value


def get_hist_b(r, n, m):

    data = [comp_m(n, m) for _ in range(r)]

    freq = [ 0 for i in range(n+1) ]

    for i in range(len(data)):
        freq[data[i]] += 1

    return freq

def get_hist(r, n, m):

    data = [comp_m(n, m) for _ in range(r)]

    return data

def prom(data):
    sum = 0
    for val in data:
        sum += val
    return sum / len(data)

def main():
    mvals = [5,10,15]

    for mi in mvals:
        data = get_hist(r = 1000, n = 100, m = mi)

        print("m =",mi,":",prom(data))

    #norm_data = [val/r for val in data]

    #esp = 0
    #for i in range(n):
    #    esp += norm_data[i] * i

    #print(esp)

if __name__ == "__main__":
    main()


