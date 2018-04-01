#include <stdio.h>
#include <stdlib.h>

#define NEWLINE "\n"


int collatz(long num) {
    int counter = 1;

    while (num > 1) {
        num = (num % 2 == 0) ? (num / 2) : (3 * num + 1);
        counter++;
    }

    return counter;
}


int maxcollatz(int i, int j) {
    int n;
    int counter;
    int max = 0;

    for (n = i; n <= j; n++) {
        counter = collatz(n);
        if (counter > max) {
            max = counter;
        }
    }

    return max;
}


int main(void) {
    int i, j;
    int temp_i, temp_j, sentinel;
    
    while (scanf ("%d %d", &i, &j) != EOF) {
        if (i < j) {
            temp_i = i;
            temp_j = j;
        } else {
            temp_i = j;
            temp_j = i;
        }
        int max = maxcollatz(temp_i, temp_j);
        printf("%d %d %d", i, j, max);
        printf("%s", NEWLINE);
    }

    return EXIT_SUCCESS;
}