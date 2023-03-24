;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter3_1) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp")) #f)))
;; profit-left : number -> number
;; determines the profit of the program
(define (profit-left ticket-price)
  (- (revenue ticket-price)
     (cost ticket-price)))

;; revenue : number -> number
;; determines the revenue for a particular ticket price.
(define (revenue ticket-price)
  (*  (attendees ticket-price) ticket-price))

;; cost : number -> number
;; determines the cost for a particular ticket price.
(define (cost ticket-price)
  (* 1.50 (attendees ticket-price)))

;; attendees : number -> number
;; determines the number of attendees for a particular ticket price.
(define (attendees ticket-price)
  (+ 120
     (* (/ 15 .10) (- 5.00 ticket-price))))


;; profit-right : number -> number
;; determines the profit of the program
(define (profit-right ticket-price)
  (- (* (+ 120
           (* (/ 15 .10)
              (- 5.00 ticket-price)))
        ticket-price)
     (* 1.50 (+ 120
                (* (/ 15 .10)
                   (- 5.00 ticket-price))))))

;; EXAMPLES AS TESTS

(profit-left 3.00) "should be"
(profit-right 3.00)
(profit-left 4.00) "should be"
(profit-right 4.00)
(profit-left 5.00) "should be"
(profit-right 5.00)