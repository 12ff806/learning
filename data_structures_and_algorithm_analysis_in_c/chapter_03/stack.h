#ifndef _stack_h

struct node;
typedef struct node *ptr_to_node;
typedef ptr_to_node stack;


int is_empty(stack s);
stack create_stack(void);
void dispose_stacl(stack s);
void make_empty(stack s);
void push(element_type x, stack s);
element_type top(stack s);
void pop(stack s);

#endif /* _stack_h */

