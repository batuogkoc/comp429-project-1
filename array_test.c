#include "omp.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
void task(int array[2][2])
{
    array[0][0] = 1;
    printf("out %d\n", array[0][0]);
    int(*new_array)[2] = malloc(sizeof(array));
    memcpy(new_array, &array[0][0], sizeof(array));
#pragma omp task
    {
        printf("in %d\n", new_array[0][0]);
        free(new_array);
    }
    array[0][0] = 0;
}

int main(int argc, char const *argv[])
{
    int array[2][2] = {{0, 0},
                       {0, 0}};
#pragma omp parallel
    {
#pragma omp single
        {

#pragma omp task
            {

                task(array);
            }
        }
    }
    return 0;
}
