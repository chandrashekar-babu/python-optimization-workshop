import java.math.*;

class Primes {
    public static final long NUM_PRIMES = 100_000;

    public static boolean isPrime(long number) {
        var limit = (long)Math.sqrt(number) + 1;

        for (var d=2; d < limit; d++) {
            if (number % d == 0)
                return false;
        }

        return true;
    }

    public static void generate(long numPrimes) {
        
        for (var v=2; numPrimes > 0; v++) {
            if (isPrime(v)) {
                System.out.println(v);
                --numPrimes;
            }
        }

    }

    public static void main(String[] args) {
        System.err.printf("Generating %d prime numbers...\n", NUM_PRIMES);

        var start_time = System.currentTimeMillis();
        Primes.generate(NUM_PRIMES);    
        var duration = (System.currentTimeMillis() - start_time) / 1000.0;
        
        System.err.printf("Primes.generate(%d) took %f seconds.\n",
                                                    NUM_PRIMES, duration);
    }
}
