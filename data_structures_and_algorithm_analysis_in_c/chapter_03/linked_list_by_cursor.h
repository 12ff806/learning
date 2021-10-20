#ifndef _cursor_h

typedef int element_type;

typedef int ptr_to_node;
typedef ptr_to_node list;
typedef ptr_to_node position;

void initialize_cursor_space(void);

list make_empty(list l);
int is_empty(const list l);
int is_last(const position p, const list l);
position find(element_type x, const list l);
void delete(element_type x, const list l);
position find_previous(element_type x, const list l);
void insert(element_type x, list l, position p);
void delete_list(list l);
position header(const list l);
position first(const list l);
position advance(const position p);
element_type retrieve(const position p);

#endif  /*_cursor_h*/


struct node {
    element_type element;
    position     next;
};

struct node cursor_space[space_size];

