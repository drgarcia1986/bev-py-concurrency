TO_CALCULATE = range(1000, 15000, 1000)


def primes_until(num):
    result = []
    for p in range(2, num+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            result.append(p)
    return result


if __name__ == "__main__":
    print({i: primes_until(i) for i in TO_CALCULATE})
