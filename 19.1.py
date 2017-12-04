#coding:utf-8

def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes
    returns: int """
    if k == 0:
        return 1
    if n == 0:
        return 0
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res

if __name__ == '__main__':
    print binomial_coeff(4,3)
