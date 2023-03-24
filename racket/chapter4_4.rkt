;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter4_4) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp")) #f)))
;; how-many : number number number -> number
;; computes the number of solutions a quadratic equation with
;; coefficients a, b, and c.
;; EXAMPLES
;; x^2 + 2x + 1 = 0 has 1 solution
;; 2x^2 + 4x + 1 = 0 has 2 solutions
;; 2x^2 + 4x + 3 = 0 has no solutions
;; x^2 - 1 = 0 has no solutions
;; 2x^2 + 4x + 2 = 0 has 1 solution
(define (how-many a b c)
  (cond
    [(> (discriminant a b c) 0) 2]
    [(= (discriminant a b c) 0) 1]
    [(< (discriminant a b c) 0) 0]))

;; discriminant : number number number -> number
;; computes the discriminant of the quadratic equation with
;; coefficients a, b and c.
;; EXAMPLES
;; the discriminant of x^2 + 2x + 1 = 0 is 0
;; the discriminant of 2x^2 + 4x + 1 = 0 is 8
;; the discriminant of 4x^2 + 4x + 3 = 0 is -8
(define (discriminant a b c)
  (- (* b b) (* 4 a c)))

;; EXAMPLES TURNED INTO TESTS
(discriminant 1 2 1) "should be" 0
(discriminant 2 4 1) "should be" 8
(discriminant 2 4 3) "should be" -8

(how-many 1 2 1) "should be" 1
(how-many 2 4 1) "should be" 2
(how-many 2 4 3) "should be" 0
(how-many 1 0 -1) "should be" 2
(how-many 2 4 2) "should be" 1
