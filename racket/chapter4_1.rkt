;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter4_1) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp")) #f)))
;; is-5? : number -> boolean
;; is n equals 5?
(define (is-5? n)
  (= n 5))

;; is-between-5-6? : number -> boolean
;; is n between 5 and 6?
(define (is-between-5-6? n)
  (and (< 5 n) (< n 6)))

;; is-between-5-6-or-over-10? : number -> boolean
;; is n between 5 and 6 or over 10
(define (is-between-5-6-or-over-10? n)
  (or (is-between-5-6? n) (>= n 10)))

;; interval-1 : number -> boolean
;; determines if n is in the interval (3,7]
;; Examples
;; -1, 3, and 10 are outside
;; 5 and 7 are inside
(define (interval-1 n)
  (and (> n 3)
       (<= n 7)))

;; Examples turned into tests
(interval-1 -1) "should be" false
(interval-1 3) "should be" false
(interval-1 5) "should be" true
(interval-1 7) "should be" true
(interval-1 10) "should be" false

;; interval-2 : number -> boolean
;; determines if n is in the interval [3, 7]
;; Examples
;; -1 and 10 are outside the interval
;; 3, 5, and 7 are inside the interval
(define (interval-2 n)
  (and (>= n 3)
       (<= n 7)))

;; EXAMPLES TURNED INTO TESTS
(interval-2 -1) "should be" false
(interval-2 3) "should be" true
(interval-2 5) "should be" true
(interval-2 7) "should be" true
(interval-2 10) "should be" false

;; interval-3 : number -> boolean
;; determines if n is in the interval [3, 9)
;; EXAMPLES
;; -1, 9, 10 are all outside the interval
;; 3 and 5 are inside the interval
(define (interval-3 n)
  (and (>= n 3)
       (< n 9)))

(interval-3 -1) "should be" false
(interval-3 3) "should be" true
(interval-3 5) "should be" true
(interval-3 9) "should be" false
(interval-3 10) "should be" false

;; interval-4 : number -> boolean
;; determines if n is in the combination of (1, 3) and (9, 11)
;; EXAMPLES
;; 1, 3, 5, 9, 11, and 50 are all outside the interval
;; 2, and 10 are inside the interval
(define (interval-4 n)
  (or (and (> n 1)
           (< n 3))
      (and (> n 9)
           (< n 11))))

(interval-4 1) "should be" false
(interval-4 2) "should be" true
(interval-4 3) "should be" false
(interval-4 5) "should be" false
(interval-4 9) "should be" false
(interval-4 10) "should be" true
(interval-4 11) "should be" false
(interval-4 50) "should be" false

;; interval-5 : number ->boolean
;; to determine if n is outside [1, 3]
;; EXAMPLES
;; -100 and 100 are in the interval
;; 1 and 3 are outside the interval
(define (interval-5 n)
  (or (< n 1)
      (> n 3)))

(interval-5 -100) "should be" true
(interval-5 1) "should be" false
(interval-5 3) "should be" false
(interval-5 100) "should be" true

;; 1.
;; f : number -> boolean
;; to determine if n is a solution to the equation:
;; 4*n + 2 = 62
(define (f n)
  (= (+ (* 4 n) 2) 62))

(f 10) "should be" false
(f 12) "should be" false
(f 14) "should be" false
(f 15) "should be" true

;; 2.
;; g : number -> boolean
;; to determine if n is a solution to the equation:
;; 2*(n^2) = 102
(define (g n)
  (= (* 2 n n) 102))

(g 10) "should be" false
(g 12) "should be" false
(g 14) "should be" false

;; 3.
;; h : number -> boolean
;; to determine if n is a solution to the equation:
;; 4*(n^2) + 6*n + 2 = 462
(define (h n)
  (= (+ (* 4 n n) (* 6 n) 2) 462))

(h 10) "should be" true
(h 12) "should be" false
(h 14) "should be" false
