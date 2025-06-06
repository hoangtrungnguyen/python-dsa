#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the number of bits for the OAAT hash function
#define HASH_FUNCTION_BITS 17
// Define the hash table size based on the number of bits (2^HASH_FUNCTION_BITS)
#define SIZE (1UL << HASH_FUNCTION_BITS)

// Structure for a snowflake node in the hash table's linked list
typedef struct snowflake_node {
    int snowflake[6];          // Arm lengths of the snowflake
    struct snowflake_node *next; // Pointer to the next snowflake in the same bucket
} snowflake_node;

// --- OAAT Hash Function and its helper macros ---
// Calculates 2^n
#define hashsize(n) ((unsigned long)1 << (n))
// Creates a bitmask for the lower n bits (2^n - 1)
#define hashmask(n) (hashsize(n) - 1)