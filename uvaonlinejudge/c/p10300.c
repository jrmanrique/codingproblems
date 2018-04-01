#include <stdio.h>
#include <stdlib.h>

#define NEWLINE "\n"


int main(void) {
    int i, j;
    int t, f;
    long land_size, animals, ef_score;
    long burden;
    char line[512];
    
    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d", &t);

    for (i = 0; i < t; ++i) {
        fgets(line, sizeof(line), stdin);
        sscanf(line, "%d", &f);
        burden = 0;

        for (j = 0; j < f; ++j) {
            fgets(line, sizeof(line), stdin);
            sscanf(line, "%ld %ld %ld", &land_size, &animals, &ef_score);

            burden += land_size * ef_score;
        }
        printf("%ld%s", burden, NEWLINE);
    }

    return EXIT_SUCCESS;
}
