;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter5_3) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp")) #f)))
;; how-many : number number number -> symbol
;; computes the number of solutions a quadratic equation with
;; coefficients a, b and c.
(define (how-many a b c)
  (cond
    [(= a 0) 'degenerate]
    [(> (discriminant a b c) 0) 'two]
    [(= (discriminant a b c) 0) 'one]
    [(< (discriminant a b c) 0) 'none]))

;; discriminant : number number number -> number
;; computes the discriminant of the quadratic equation with
;; coefficients a, b and c.
(define (discriminant a b c)
  (- (* b b) (* 4 a c)))

;; Examples
(discriminant 1 2 1) "should be" 0
(discriminant 2 4 1) "should be" 8
(discriminant 2 4 3) "should be" -8

(how-many 1 2 1) "should be" 'one
(how-many 2 4 1) "should be" 'two
(how-many 2 4 3) "should be" 'none
(how-many 1 0 -1) "should be" 'two
(how-many 2 4 2) "should be" 'one
(how-many 0 1 1) "should be" 'degenerate
