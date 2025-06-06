#include <stdatomic.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NUM_BITS 17

#define hashsize(n) ((unsigned  long) 1 << (n))
#define hashmask(n) (hashsize(n) - 1)

char *read_line(int size){

    char *str;
    int ch;
    int len = 0;
    str = malloc(size);

    if(str == NULL){
        fprintf(stderr, "malloc error\n");
        exit(1);
    }


    while((ch = getchar()) != EOF && (ch != '\n')){
        str[len++] = ch;
        if( len == size) {
            size = size * 2;
            str = realloc(str, size);
            if( str == NULL) {
                fprintf(stderr, "realloc error\n");
                exit(1);
            }
        }
    }

    str[len] = '\0';
    return str;
}

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

typedef struct word_node {
    char **word;
    struct word_npde *next;
} word_node;

int in_hash_table(word_node *hash_table[], char *find, unsigned  find_len){
    unsigned word_code;
    word_node *wordptr;
    word_code = oaat(find, find_len, NUM_BITS);
    wordptr = hash_table[word_code];
    while(wordptr){
        if(
            (strlen(*(wordptr -> word)) == find_len)
            && (strncmp(*(wordptr -> word), find, find_len) == 0)
            ){
            return 1;
        }

        wordptr = wordptr->next;
    }
    return 0;
}