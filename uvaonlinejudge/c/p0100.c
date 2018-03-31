#include <stdio.h>
#include <stdlib.h>


int collatz(int num) {
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
    const char NEWLINE = '\n';
    int size;
    int i, j;
    
    char line[512];

    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d", &size);

    int input[size][2];
    for (int s = 0; s < size; ++s) {
        fgets(line, sizeof(line), stdin);
        sscanf(line, "%d %d", &input[s][0], &input[s][1]);
    }

    for (int s = 0; s < size; ++s) {
        i = input[s][0];
        j = input[s][1];
        int max = maxcollatz(i, j);
        printf("%d %d %d", i, j, max);
        printf("%c", NEWLINE);
    }

    return EXIT_SUCCESS;
}