;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter3) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp")) #f)))
;; attendance : number -> number
;; to compute how many attendees we get at some price
;; Examples:
;; at $5.0, 120 people will attend.
;; at $4.9, 135 people will attend.
;; at $4.0, 270 people will attend.
;; at $3.0, 420 people will attend.
(define (attendance price)
  (+ (* (/ 15 .10) (- 5.00 price))
     120))
(attendance 5.0)
;;(attendance 4.9)
(attendance 4)
(attendance 3)

;; revenue : number -> number
;; Examples:
;; at $5.0, we get 600.
;; at $4.0, we get 1080.
;; at $3.0, we get 1260.
(define (revenue price)
  (* (attendance price) price))
(revenue 5.0)
(revenue 4)
(revenue 3)

;; cost : number -> number
;; Examples:
;; at $5.0, we get 184.8
;; at $4.0, we get 190.8
;; at $3.0, we get 196.8
(define (cost price)
  (+ 180 (* 0.04 (attendance price))))
(cost 5.0)
(cost 4)
(cost 3)

;; profit : number -> number
;; 对于给定 price, 利润是收入和成本之差
;; Examples:
;; at $5.0, we get 415.2
;; at $4.0, we get 889.2
;; at $3.0, we get 1063.2
(define (profit price)
  (- (revenue price)
     (cost price)))
(profit 5.0)
(profit 4)
(profit 3)

;; How not to design a program
(define (profit-right price)
  (- (* (+ 120
           (* (/ 15 .10)
              (- 5.00 price)))
        price)
     (+ 180
        (* .04
           (+ 120
              (* (/ 15 .10)
                 (- 5.00 price)))))))
(profit-right 5.00)
(profit-right 4.00)
(profit-right 3.00)

(define (cost-2 price)
  (* 1.50 (attendance price)))

(define (profit-2 price)
  (- (* (attendance price) price)
     (cost-2 price)))

(profit-2 5.00)
(profit-2 4.00)
(profit-2 3.00)