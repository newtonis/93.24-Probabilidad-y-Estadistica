
import numpy
import matplotlib.pyplot as plt


def comp_m(n, m):
    items = numpy.random.permutation(range(1, n+1))[:m]
    max_value = 0
    for val in items:
        max_value = max(max_value, val)
    return max_value


def get_hist(r, n, m):

    data = [comp_m(n, m) for _ in range(r)]

    freq = [ 0 for i in range(101) ]

    for i in range(len(data)):
        freq[data[i]] += 1

    return freq

def main():
    data = get_hist(r = 1000, n = 100, m = 10)

    fig, ax = plt.subplots()

    #print(data[100])

    (markerline, stemlines, baseline) = ax.stem(range(0, 101) , data )
    plt.setp(baseline,'linewidth',1)

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


