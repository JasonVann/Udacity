#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

int main()
{
    int x;
    assert(x == 0);
    bool res = x == 0;

    printf("res is %d", res);
}
