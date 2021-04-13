/*
 * 12ff806
 * 2021 04 13
 */


#include <stdio.h>
#include <stdlib.h>
#include "list.h"


/* node implementation */
struct node
{
    element_type element;
    position     next;
}


/* Return true if l is empty */
int is_empty(list l)
{
    return l->next == NULL;
}


/* Return true if p is the last position in list l */
/* parameter l is unused in this implementation */
int is_last(position p, list l) {
    return p->next == NULL;
}


/* Return position of x in l, NULL if not found */
position find(element_type x, list l) {
    position p;
    
    p = l->next;
    while(p != NULL && p->element != x) {
        p = p->next;
    }
    return p;
}


/* If x is not found, then next field of returned */
/* position is NULL */
/* Assumes a header */
position find_previous(element_type x, list l) {
    position p;
    
    p = l;
    while(p->next != NULL && p->next->element != x) {
        p = p->next;
    }
    return p;
}


/* Delete first occurrence of x from a list */
/* Assume use of a header node */
void delete(element_type x, list l) {
    position p, tmp_cell;

    p = find_previous(x, l);
    /* Assumption of header use, x is found, delete it */
    if(!is_last(p, l)) {
        tmp_cell = p->next;
        p->next = tmp_cell->next;
        free(tmp_cell);
    }
}


/* Insert (after legal position p) */
/* Header implementation assumed */
/* parameter l is unused in this implementation */
void insert(element_type x, list l, position p) {
    position tmp_cell;
    
    tmp_cell = malloc(sizeof(struct node));
    if(tmp_cell == NULL) {
        printf("out of space!!!!");
        exit(1);
    }
    tmp_cell->element = x;
    tmp_cell->next = p->next;
    p->next = tmp_cell;
}



























































