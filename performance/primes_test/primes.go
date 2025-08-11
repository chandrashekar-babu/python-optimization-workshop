package main

import (
    "fmt"
    "math"
    "time"
	"os"
)

const NUM_PRIMES = 100_000

func isPrime(number int) bool {
    limit := int(math.Sqrt(float64(number))) + 1
    for d := 2; d < limit; d++ {
        if number % d == 0 {
            return false
        }
    }
    return true
}

func genPrimes(numPrimes int) {
    for v := 2; numPrimes > 0; v++ {
        if isPrime(v) {
            fmt.Println(v)
            numPrimes--
        }
    }
}

func main() {
    fmt.Fprintf(os.Stderr, "Generating %d prime numbers...\n", NUM_PRIMES)
    startTime := time.Now()
    genPrimes(NUM_PRIMES)
    duration := time.Since(startTime).Seconds()
    fmt.Fprintf(os.Stderr, "genPrimes(%d) took %.6f seconds",
	            NUM_PRIMES, duration)
}
