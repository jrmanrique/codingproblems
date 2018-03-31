#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NEWLINE "\n"


long get_next_prime (long num) {
    for (long d = 2; d <= num; ++d) {
        if (num % d == 0) {
            return d;
        } 
    }
    return num;
}


int main(void) {
    long num = 600851475143;
    
    long best = 0;
    while (num != 1) {
        long div = get_next_prime(num);
        if (div > best) {
            best = div;
        
        num = num / div;
    }
    printf("%ld%s", best, NEWLINE);

    return EXIT_SUCCESS;
}