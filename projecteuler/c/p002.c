#include <stdio.h>
#include <stdlib.h>

#define NEWLINE "\n"


int main(void) {
    int LIMIT = 4000000;
    int a, b, c;
    int sum = 0;
    
    a = 1;
    b = 1;
    while (b < LIMIT) {
        c = a + b;
        if (c % 2 == 0) {
            sum += c;
        }
        a = b;
        b = c;
    }
    printf("%d%s", sum, NEWLINE);

    return EXIT_SUCCESS;
}