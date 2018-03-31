#include <stdio.h>
#include <stdlib.h>

#define NEWLINE "\n"


int main(void) {
    int limit = 1000;
    int sum = 0;
    for (int i = 1; i <= limit; ++i) {
        if (i % 3 == 0 | i % 5 == 0) {
            sum += i;
        }
    }
    printf("%d%s", sum, NEWLINE);

    return EXIT_SUCCESS;
}