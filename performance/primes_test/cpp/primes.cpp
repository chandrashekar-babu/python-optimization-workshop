#include <cmath>
#include <iostream>

#include "stop_watch.h"

const auto NUM_PRIMES  = 100000;

class Primes {
    public:
        auto isPrime(auto number) {
            unsigned int limit = sqrt(number) + 1;

            for (auto d=2; d < limit; d++) {
                if (number % d == 0)
                    return false;
            }
            return true;
        }

        void generate(auto numPrimes)
        {
            for (auto v=2; numPrimes > 0; v++) {
                if (isPrime(v)) {
                    std::cout << v << "\n";
                    --numPrimes;
                }
            }
        }
};

int main()
{
    Primes primes;
    StopWatch watch;

    std::cerr << "Generating first " << NUM_PRIMES << " prime numbers...\n";

    watch.start();
    primes.generate(NUM_PRIMES);
    watch.stop();

    std::cerr << "primes.generate(" << NUM_PRIMES << ") took "
              << watch.duration() << " seconds.\n";
    return 0;
}
