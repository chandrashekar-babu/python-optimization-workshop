#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

#include "stop_watch.h"

#define NUM_PRIMES 100000

bool is_prime(unsigned int number) {
    unsigned int limit = sqrt(number) + 1;

    for (unsigned int d=2; d < limit; d++) {
        if (number % d == 0)
            return false;
    }
    return true;
}

void gen_primes(unsigned int num_primes)
{

    for (unsigned int v=2; num_primes > 0; v++) {
        if (is_prime(v)) {
            printf("%u\n", v);
            --num_primes;
        }
    }
}

int main()
{
    stop_watch_t watch;

    fprintf(stderr, "Generating first %u prime numbers...\n", NUM_PRIMES);

    start_watch(&watch);
    gen_primes(NUM_PRIMES);
    stop_watch(&watch);

    fprintf(stderr, "gen_primes(%u) took %3.6Lf seconds.\n",
                    NUM_PRIMES, duration(&watch));

    return EXIT_SUCCESS;
}
