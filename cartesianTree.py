
def build_cartesian_tree(ks, vs):
    n = len(ks)
    p, l, r = [-1]*n, [-1]*n, [-1]*n
    st, top = [-1]*n, -1
    # insert as k is increasing, may be optimized
    for _, i in sorted(zip(ks, range(n))):
        t = top

        while t >= 0 and vs[st[t]] > vs[i]:
            t -= 1

        if t != -1:
            p[i] = st[t]
            r[st[t]] = i

        if t < top:
            p[st[t+1]] = i
            l[i] = st[t+1]

        st[t+1] = i
        top = t+1

    return p, l, r


if __name__ == '__main__':
    for l in build_cartesian_tree(range(10),
            [2,4,3,1,6,7,8,9,1,7]):
        print l
