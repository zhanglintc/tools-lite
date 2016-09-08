#include "stdio.h"

int main(int argc, char const *argv[]) {
    unsigned char uc1 = 0x7f;
    signed   char sc1 = 0x7f;

    unsigned char uc2 = 0x80;
    signed   char sc2 = 0x80;

    printf("uc1: %d\n", uc1);
    printf("sc1: %d\n", sc1);

    printf("\n");

    printf("uc2: %d\n", uc2);
    printf("sc2: %d\n", sc2);

    return 0;
}