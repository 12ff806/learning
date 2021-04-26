/*
 * 12ff806
 */


#define empty_tos (-1)
#define min_stack_size (5)


struct stack_record {
    int capacity;
    int top_of_stack;
    element_type *array;
};


stack create_stack(int max_elements)
{
    stack s;
    if (max_elements < min_stack_size) {
        printf("stack size is too small!");
    }
    
    s = malloc(sizeof(struct stack_record));
    if (s == NULL) {
        printf("out of space!!!");
    }

    s->array = malloc(sizeof(element_type));
    if (s->array == NULL) {
        printf("out of space!!!");
    }
    s->capacity = max_elements;
    make_empty(s);

    return s;
}


void dispose_stack(stack s) {
    if (s != NULL) {
        free(s->array);
        free(s);
    }
}


int is_empty(stack s) {
    return s->top_of_stack == empty_tos;
}


void make_empty(stack s) {
    s->top_of_stack = empty_tos;
}


void push(element_type x, stack s) {
    if (is_full(s)) {
        printf("full stack");
    }
    else
        s->array[++s->top_of_stack] = x;
}


element_type top(stack s) {
    if (!is_empty(s)) {
        return s->array[s->top_of_stack];
    }
    printf("empty stack");
    return 0;
}


void pop(stack s) {
    if (is_empty(s)) {
        printf("Empty stack");
    }
    else
        s->top_of_stack--;
}


element_type top_and_pop(stack s) {
    if (!is_empty(s)) {
        return s->array[s->top_of_stack--]
    }
    printf("empty stack");
    return 0;
}
