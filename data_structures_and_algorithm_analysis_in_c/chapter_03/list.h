#ifndef _list_h

struct node;
typedef struct node *ptr_to_node;
typedef ptr_to_node list;
typedef ptr_to_node position;

list make_empty(list l);
int is_empty(list l);
int is_last(position p, list l);
position find(element_type x, list l);
void delete(element_type x, list l);
position find_previous(element_type x, list l);
void insert(element_type x, list l, position p);
void delete_list(list l);
position header(list l);
position first(list l);
position advance(position p);
element_type retrieve(position p);

#endif  /*_list_h*/

