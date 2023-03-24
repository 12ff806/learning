;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter4_3) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp")) #f)))
;; pay-back : number -> number
;; computes the amount of cash back the credit card holder receives.
;; Examples
;; $400 gets $1
;; $1400 gets $5.75
;; $2000 gets $10.00
;; $2600 gets $14.75
(define (pay-back a)
  (cond
    [(<= a 500)
     (pay-back-0-500 a)]
    [(and (> a 500) (<= a 1500))
     (pay-back-500-1500 a)]
    [(and (> a 1500) (<= a 2500))
     (pay-back-1500-2500 a)]
    [else
     (pay-back-2500+ a)]))

;; pay-back-0-500 : number -> number
;; computes the pay back for amounts between 0 and 500
(define (pay-back-0-500 a)
  (* a (* .25 1/100)))

;; pay-back-500-1500 : number -> number
;; computes the pay back for amounts between 500 and 1500
(define (pay-back-500-1500 a)
  (+ (pay-back-0-500 500)
     (* (- a 500) (* .50 1/100))))

;; pay-back-1500-2500 : number -> number
;; computes the pay back for amounts between 1500 and 2500
(define (pay-back-1500-2500 a)
  (+ (pay-back-500-1500 1500)
     (* (- a 1500) (* .75 1/100))))

;; pay-back-2500+ : number -> number
;; computes the pay back for amounts between 2500 and higher
(define (pay-back-2500+ a)
  (+ (pay-back-1500-2500 2500)
     (* (- a 2500) (* 1 1/100))))

;; EXAMPLES AS TESTS
(pay-back-0-500 400) "should be" 1
(pay-back 400) "should be" 1

(pay-back-500-1500 1400) "should be" 5.75
(pay-back 1400) "should be" 5.75

(pay-back-1500-2500 2000) "should be" 10.00
(pay-back 2000) "should be" 10.00

(pay-back-2500+ 2600) "should be" 14.75
(pay-back 2600) "should be" 14.75
