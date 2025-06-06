#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 100000



int identical_right(int snow1[], int snow2[], int start){
    int offset, snow2_index;
    for(offset =0; offset < 6; offset ++){
        snow2_index = start + offset;
        if(snow2_index >= 6){
            snow2_index = snow2_index - 6;
        }
        if(snow1[offset] != snow2[snow2_index]){
                return 0;
            }
    }
    return 1;
}

int identical_left(int snow1[], int snow2[], int start){
    int offset, snow2_index;
    for(offset = 0; offset < 6; offset ++){
        snow2_index = start - offset;

        if(snow2_index < 0){
            snow2_index = snow2_index + 6;
        }

        if(snow1[offset] != snow2[snow2_index]){
            return 0;
        }
    }

    return 1;
}

int are_identical(int snow1[], int snow2[]){
    int start;
    for(start = 0; start < 6; start ++){
        if(identical_right(snow1, snow2, start)){
            return 1;
        }
        if(identical_left(snow1, snow2, start)){
            return 1;
        }
    }

    return 0;
}



int code(int snowflake[]){
    return (snowflake[0] + snowflake[1] + snowflake[2] + snowflake[3] + snowflake[4] + snowflake[5]) % SIZE;
}

typedef struct snowflake_node {
    int snowflake[6];
    struct snowflake_node *next;
} snowflake_node;




void identify_identical(snowflake_node *snowflakes[]){
    snowflake_node  *node1, *node2;
    int i;
    for(i =0; i < SIZE; i ++){
        node1 = snowflakes[i];
        while(node1 != NULL){
            node2 = node1->next;
            while(node2 != NULL){
                if(are_identical(node1->snowflake, node2 -> snowflake)){
                    printf("Twin snowflakes found.\n");
                    return;
                }
                node2 = node2 -> next;
            }

            node1 = node1->next;
        }
    }

    printf("No two integers are alike.\n");
}

#define hashsize(n) ((unsigned  long) 1 << (n))
#define hashmask(n) (hashsize(n) - 1)

unsigned long oaat(char *key, unsigned  long len, unsigned  long bits){
    unsigned  long hash, i;
    for (hash = 0, i = 0; i < len; i ++){
        hash += key[i];
        hash += (hash << 10);
        hash ^= (hash >> 6);
    }

    hash += (hash << 3);
    hash ^= (hash >> 11);
    hash += (hash << 15);
    return hash & hashmask(bits);
}

int main(void) {
//    long snowflake[] = {1, 2, 3, 4, 5, 6};
    //2^17 is the smallest power of 2 that is at least 100000  Hash Tables 17
//    unsigned long code = oaat((char *)snowflake, sizeof(snowflake), 17);
//    printf("%lu\n", code);
//    return 0;
    static snowflake_node  *snowflakes[SIZE] = {NULL};// one dimensional array of snowflake_node with SIZE
    snowflake_node *snow;

    int n,i,j, snowflake_code;
    scanf("%d", &n);
    for(i = 0; i < n; i ++){
        snow = malloc(sizeof(snowflake_node));
        if( snow == NULL){
            fprintf(stderr, "malloc error\n");
            exit(1);
        }

        for(j = 0; j < 6; j ++){
            scanf("%d", &snow->snowflake[j]);
        }
        //generate code
        snowflake_code = oaat((char *) snow -> snowflake, sizeof(snowflakes), 17);

        //assign new next node to position: snowflake_code
        snow->next = snowflakes[snowflake_code];
        snowflakes[snowflake_code] = snow;
    }

    identify_identical(snowflakes);

    return 0;
}