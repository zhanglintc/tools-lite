#include <stdlib.h>
#define SIZE 1024

#define testSize 1024

static int (**hnew())[2] {
    return (int (**)[2])calloc(sizeof(int**), SIZE);
}

static void hdel(int (**e)[2]) {
    for (int i = 0; i < SIZE; i++) free(e[i]); free(e);
}

static int (**hget(int (**t)[2], int k))[2] {
    // for (int h = k & (SIZE - 1); **t && ***t != k; h = ((h + 1) & (SIZE - 1)), t += h);
    int h = k & (SIZE - 1);

    while(**t && ***t != k) {
        h = ((h + 1) & (SIZE - 1));
        t += h;
    }

    return t;
}

static void hset(int (**t)[2], int k, int v) {
    // for (int (**a)[2] = hget(t, k); !*a && (*a=(int (*)[2])malloc(sizeof(**t))); (**a)[0]=k,(**a)[1]=v);
    int (**a)[2] = hget(t, k);

    if(!*a && (*a=(int (*)[2])malloc(sizeof(**t)))) {
        (**a)[0]=k,(**a)[1]=v;
    }

    else {
        (**a)[0]=k,(**a)[1]=v;
    }
}

// TEST DRIVER
#include <stdio.h>
int main() {
    // initialize hash table
    int (**table)[2] = hnew();

    /***** example of typical use *****
    hset(table, 10, 10);
    hset(table, 20, 20);
    int (**a)[2] = hget(table, 10);
    int (**b)[2] = hget(table, 20);
    printf("%d:%d\n", (**a)[0], (**a)[1]);
    printf("%d:%d\n", (**b)[0], (**b)[1]);
    ***********************************/

    for(int i = 0; i < testSize; i++) {
        hset(table, i, i);
    }

    for(int i = 0; i < testSize; i++) {
        printf("%d:%d\n", **(hget(table, i))[0], **hget(table, i)[0]);
    }

    // delete hash table
    hdel(table);

    // pause to see the result
    getchar();
}
