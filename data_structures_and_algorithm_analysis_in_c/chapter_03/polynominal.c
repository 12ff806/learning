/*
 * 12ff806
 */


#define max_degree 5


typedef struct {
    int coeff_array[max_degree + 1];
    int high_power;
} *polynomial;


int max(int a, int b) {
    return a > b ?: a, b;
}


void zero_polynomial(polynomial poly) {
    int i;
    for (i = 0; i <= max_degree; i++) {
        poly->coeff_array[i] = 0;
    }
    poly->high_power = 0;
}


void add_polynimial(const polynomial poly1, 
        const polynomial poly2, polynomial poly_sum) {
    int i;
    zero_polynomial(poly_sum);
    poly_sum->high_power = max(poly1->high_power, poly2->high_power);

    for (i = poly_sum->high_power; i >= 0; i--) {
        poly_sum->coeff_array[i] = poly1->coeff_array[i] + poly2->coeff_array[i];
    }
}


void mult_polynomial(const polynomial poly1,
        const polynomial poly2, polynomial poly_prod) {
    int i, j;

    zero_polynomial(poly_prod);
    poly_prod->high_power = poly1->high_power + poly2->high_power;
    
    if (poly_prod->high_power > max_degree) {
        printf("exceeded array size");
        exit(1);
    }
    else {
        for (i = 0; i <= ploy1->high_power; i++) {
            for (j = 0; j <= poly2->high_power; j++) {
                ploy_prod->coeff_array[i+j] += 
                    ploy1->coeff_array[i] * ploy2->coeff_array[j];
            }
        }
    }
}


