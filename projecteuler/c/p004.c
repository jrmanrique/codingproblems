#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define NEWLINE "\n"


int strip(const char *input, char *output) {
    int len = strlen(input);
    if(len > 0)
        strcpy(output, ++input);
    if(len > 1)
        output[len - 2] = '\0';

    return EXIT_SUCCESS;
}


int ispalindrome (char *str) {
    if (strlen(str) <= 1) {
        return 1;
    } else if (str[0] == str[strlen(str) - 1]) {
        char sentinel[127];
        strip(str, sentinel);
        return ispalindrome(sentinel);
    }
    return 0;
}


int isspecial (int num) {
    for (int div = 100; div <= 999; ++div) {
        if (num % div == 0) {
            if (100 <= num / div & num / div <= 999) {
                return 1;
            }
        }
    }
    return 0;
}


int main(void) {
    int num;
    char charnum[128];
    
    for (num = 998001; num >= 10000; --num) {
        sprintf(charnum, "%d", num);
        if (ispalindrome(charnum) & isspecial(num)) {
            printf("%d%s", num, NEWLINE);
            break;
        }
    }

    return EXIT_SUCCESS;
}