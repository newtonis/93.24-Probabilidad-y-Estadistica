
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

    return data

def get_hist_random(r , m):
    data = []
    vec_n = []
    for i in range(r):
        n = numpy.random.randint(100,400)
        m = n / 10
        data.append( comp_m(n , m) )
        vec_n.append( n )
    return data , vec_n


def prom(data):
    sum = 0
    for val in data:
        sum += val
    return sum / len(data)

def calcular_estimador(data , r , n , m):
    data_ans = []
    for val in data:
        data_ans.append( int( round( (m+1) * val / m - 1)) )
    return data_ans

def calcular_error(data_n , vec_n):
    err_vec = []
    for i in range(len(data_n)):
        err_vec.append( abs( data_n[i] - vec_n[i] ) * 100 / vec_n[i])

    return err_vec

def freq(data , n ):
    freq_arr = [ 0 for _ in range(0,n) ]

    for val in data:
        freq_arr[val] += 1

    return freq_arr

def media(var):
    ans = 0
    for i in range(len(var))


def main():

    data , vec_n = get_hist_random(r = 10000)

    data_n = calcular_estimador(data , r = 10000, n = 100 , m = 10)

    
    #data_err = calcular_error(data_n , vec_n)


    #freq_arr = freq(data_n,n = 120)


    #fig, ax = plt.subplots()
    #(markerline, stemlines, baseline) = ax.stem(range(0, 120), freq_arr)
    #plt.setp(baseline, 'linewidth', 1)

    #fig.tight_layout()
    #plt.show()

    #norm_data = [val/r for val in data]

    #esp = 0
    #for i in range(n):
    #    esp += norm_data[i] * i

    #print(esp)

if __name__ == "__main__":
    main()
