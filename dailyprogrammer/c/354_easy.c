#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <math.h>

#define NEWLINE "\n"
#define MAXDIM 256


long complexity(long num) {
    long a, b;
    long i, j;
    long score = INT_MAX;
    
    for (i = 1; i <= sqrt(num) + 1; ++i) {
        if (num % i == 0) {
            a = i;
            b = num / i;
            if (a + b < score) {
                score = a + b;
            } 
        }
    }

    return score;
}


int main(void) {
    long n;

    char line[MAXDIM];
    fgets(line, sizeof(line), stdin);
    sscanf(line, "%ld", &n);

    long score = complexity(n);
    printf("%ld => %ld", n, score);

    printf("%s", NEWLINE);
    return EXIT_SUCCESS;
}