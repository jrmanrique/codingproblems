#include <stdio.h>
#include <stdlib.h>

#define NEWLINE "\n"


int compare(const void* a, const void* b) {
     int int_a = * ( (int*) a );
     int int_b = * ( (int*) b );

     if (int_a == int_b) return 0;
     else if (int_a < int_b) return -1;
     else return 1;
}


int main(void) {
    int i, j;
    int t;
    long salaries[3];
    char line[256];
    
    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d", &t);

    for (i = 1; i <= t; ++i) {
        salaries[3] = 0;
        fgets(line, sizeof(line), stdin);
        sscanf(line, "%ld %ld %ld", &salaries[0], &salaries[1], &salaries[2]);
        
        qsort(salaries, 3, sizeof(long), compare);
        printf("Case %d: %ld%s", i, salaries[1], NEWLINE);
    }
    
    return EXIT_SUCCESS;
}