import numpy as np

def get_st_table(a):
    n = len(a)
    logn = np.ceil(np.log2(n))
    m = np.zeros((n, logn), dtype=np.int32)

    for i in xrange(n):
        m[i,0] = i

    j = 1
    while 1<<j <= n:
        i = 0
        while i + (1<<j) - 1 < n:
            m[i,j] = min((m[i,j-1], m[i+(1<<(j-1)),j-1]),
                        key=a.__getitem__)
            i += 1
        j += 1
    return m

def rmq(a, m, i, j):
    ''' m is st table of a. i <= j.
    a[rmq(i,j)] is minimium in a[i:j+1]. '''
    k = int(np.floor(np.log2(j-i+1)))
    return min(m[i,k], m[j-(1<<k)+1,k], key=a.__getitem__)

if __name__ == '__main__':
    a = [2,4,3,1,6,7,8,9,1,7]
    n, m = len(a), get_st_table(a)
    for i in xrange(n):
        for j in xrange(i, n):
            assert a[rmq(a,m,i,j)] == min(a[i:j+1])
    print 'OK'
