from memory_profiler import profile

@profile
def test_mem_usage():
    result = []
    print("Result: ", result)
    result = list(range(10_000))

if __name__ == '__main__':
    test_mem_usage()