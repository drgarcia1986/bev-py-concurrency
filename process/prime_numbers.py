from concurrent.futures import as_completed, ProcessPoolExecutor

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
    waits = {}
    with ProcessPoolExecutor() as executor:
        waits = {
            executor.submit(primes_until, i): i
            for i in TO_CALCULATE
        }
        print({
            waits[future]: future.result()
            for future in as_completed(waits)
        })
