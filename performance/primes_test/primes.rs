use std::time::Instant;
const NUM_PRIMES: u64 = 100_000;

fn is_prime(number: u64) -> bool {
    let limit = (number as f64).sqrt() as u64 + 1;
    for d in 2..limit {
        if number % d == 0 {
            return false;
        }
    }
    return true;
}

fn gen_primes(mut num_primes: u64) {
    let mut v = 2;
    while num_primes > 0 {
        if is_prime(v) {
            println!("{}", v);
            num_primes -= 1;
        }
        v += 1
    }
}

fn main() {
    eprintln!("Generating {} prime numbers...", NUM_PRIMES);
    let start_time = Instant::now();
    gen_primes(NUM_PRIMES);
    let duration = start_time.elapsed();
    eprintln!("gen_primes({}) took {:.6} seconds.",
            NUM_PRIMES,
            duration.as_secs_f64()
    );
}
