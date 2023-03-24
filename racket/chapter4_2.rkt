;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter4_2) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp")) #f)))
;; interest-rate : number -> number
;; determines interest rate when amount >= 0
(define (interest-rate amount)
  (cond
    [(<= amount 1000) 0.040]
    [(<= amount 5000) 0.045]
    [else 0.050]))

;; interest : number -> number
;; calculates the amount of interest for d dollars.
;; EXAMPLES
;; the interest for $500 is $20
;; the interest for $2000 is $90
;; the interest for $10000 is $500
(define (interest d)
  (cond
    [(<= d 1000) (* d (/ 4 100))]
    [(<= d 5000) (* d (/ 45 1000))]
    [(> d 5000) (* d (/ 5 100))]))

;; Examples turned into tests
(interest 500) "should be" 20
(interest 2000) "should be" 90
(interest 10000) "should be" 500

;; tax : number -> number
;; to determine the amount of tax owed, for a given gross-pay
(define (tax gross-pay)
  (cond
    [(<= gross-pay 240) 0]
    [(<= gross-pay 480) (* gross-pay .15)]
    [else (* gross-pay .28)]))

;; EXAMPLES AS TESTS
(tax 10) "should be" 0
(tax 240) "should be" 0
(tax 300) "should be" 45
(tax 480) "should be" 72
(tax 500) "should be" 140

;; netpay : numbet -> number
;; to determine the amount of income, after taxes.
(define (netpay hours-worked)
  (- (* hours-worked 12)
     (tax (* hours-worked 12))))

;; EXAMPLES AS TESTS
(netpay 1) "should be" 12
(netpay 40) "should be" 408
