/*
 * number29
 */

#include "stack.h"


struct node {
    element_type element;
    ptr_to_node  next;
}


int is_empty(stack s) {
    return s->next == NULL;
}


stack create_stack(void) {
    stack s;
    s = malloc(sizeof(struct node));
    if (s == NULL) {
        printf("out of space!!!");
        exit(1);
    }

    s->next == NULL;
    make_empty(s);
    return s;
}


void make_empty(stack s) {
    if (s == NULL) {
        printf("must ust create_stack first");
    }
    else {
        while (!is_empty(s)) {
            pop(s);
        }
    }
}


void push(element_type x, stack s) {
    ptr_to_node tmp_cell;
    
    tmp_cell = malloc(sizeof(struct node));
    if (tmp_cell == NULL) {
        printf("out of space!!!");
        exit(1);
    }
    else {
        tmp_cell->element = x;
        tmp_cell->next = s->next;
        s->next = tmp_cell;
    }
}


element_type top(stack s) {
    if (!is_empty(s)) {
        return s->next->element;
    }
    printf("empty stack");
    return 0;
}


void pop(stack s) {
    ptr_to_node first_cell;
    
    if (is_empty(s)) {
        printf("empty stack");
    }
    else {
        first_cell = s->next;
        // s->next = first_cell->next;
        s->next = s->next->next;
        free(first_cell);
    }
}

