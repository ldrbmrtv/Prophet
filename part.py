def parts(n):
    a = [1]*n
    y = -1
    v = n
    while v > 0:
        v -= 1
        x = a[v] + 1
        while y >= 2 * x:
            a[v] = x
            y -= x
            v += 1
        w = v + 1
        while x <= y:
            a[v] = x
            a[w] = y
            yield a[:w + 1]
            x += 1
            y -= 1
        a[v] = x + y
        y = a[v] - 1
        yield a[:w]

def k_parts(n, k):

    a = [1]*n
    y = -1
    v = n
    while v > 0:
        v -= 1
        x = a[v] + 1
        while y >= 2 * x:
            a[v] = x
            y -= x
            v += 1
        w = v + 1
        while x <= y:
            a[v] = x
            a[w] = y
            l = w + 1
            if l == k:
                yield a[:l]
            x += 1
            y -= 1
        a[v] = x + y
        y = a[v] - 1
        if w == k:
            yield a[:w]
