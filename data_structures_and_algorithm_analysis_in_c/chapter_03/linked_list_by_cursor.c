/*
 * number29
 */

#define space_size 10

typedef int element_type;
typedef int ptr_to_node;
typedef ptr_to_node list;
typedef ptr_to_node position;


struct node {
    element_type element;
    position     next;
};


struct node cursor_space[space_size];


static position cursor_alloc(void) {
    position p;
    
    p = cursor_space[0].next;
    cursor_space[0].next = cursor_space[p].next;
    return p;
}


static void cursor_free(position p) {
    cursor_space[p].next = cursor_space[0].next;
    cursor_space[0].next = p;
}


int is_empty(list l) {
    return cursor_space[l].next == 0;
}


int is_last(position p, list l) {
    return cursor_space[p].next == 0;
}


position find(element_type x, list l) {
    position p;
    p = cursor_space[l].next;
    while (p && cursor_space[p].element != x) {
        p = cursor_space[p].next;
    }
    return p;
}


void delete(element_type x, list l) {
    position p, tmp_cell;
    
    p = find_previous(x, l);
    if (!is_last(p, l)) {
        tmp_cell = cursor_space[p].next;
        cursor_space[p].next = cursor_space[tmp_cell].next;
        cursor_free(tmp_cell);
    }
}


void insert(element_type x, list l, position p) {
    position tmp_cell;
    
    tmp_cell = cursor_alloc();
    if (tmp_cell == 0) {
        printf("out of space!!!");
        exit(1);
    }
    
    cursor_space[tmp_cell].element = x;
    cursor_space[tmp_cell].next = cursor_space[p].next;
    cursor_space[p].next = tmp_cell;
}

