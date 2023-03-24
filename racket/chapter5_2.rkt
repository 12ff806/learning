;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter5_2) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp")) #f)))
;; check-guess3 : number number number number -> number
;; determines if the number represented by ones, tens, hundreds is
;; more or less than the target.

;; EXAMPLES
;; Ones digit 1, tens digit 2, hundreds digit 3 and target 500
;; produces 'TooSmall
;; Ones digit 1, tens digit 2, hundreds digit 3 and target 100
;; produces 'TooLarge
;; Ones digit 1, tens digit 2, hundreds digit 3 and target 321
;; produces 'Perfect

;; To write this program, we need too combine two functions.
;; The first combines digits together into a number,
;; and the second compares the chosen guess with the
;; target. Luckily, each of these functions were the subject
;; of earlier exercises!
(define (check-guess3 ones tens hundreds target)
  (check-guess (digits ones tens hundreds) target))

;; digits : number number number -> number
;; given ones, tens and hundreds digits, produces the corresponding number

;; EXAMPLE
;; Ones digit 1, tens digit 2, hundreds digit 3 produces 321
(define (digits ones tens hundreds)
  (+ ones
     (* tens 10)
     (* hundreds 100)))

;; check-guess : number number -> symbol
;; to detemine whether guess is larger, smaller, or equal to target
;; EXAMPLES
;; if the guess is 1 and the target is 1,
;; the answer should be 'perfect!
;; if the guess is 1 and the target is 2,
;; the answer should be 'TooSmall
;; if the guess is 1 and the target is 0,
;; the answer should be 'TooLarge
(define (check-guess guess target)
  (cond
    [(= guess target) 'Perfect]
    [(< guess target) 'TooSmall]
    [(> guess target) 'TooLarge]))

;; EXAMPLES TURNED INTO TESTS:
(check-guess 1 1) "should be" 'Perfect
(check-guess 1 2) "should be" 'TooSmall
(check-guess 1 0) "should be" 'TooLarge

(digits 1 2 3) "should be" 321

(check-guess3 1 2 3 500) "should be" 'TooSmall
(check-guess3 1 2 3 100) "should be" 'TooLarge
(check-guess3 1 2 3 321) "should be" 'Perfect

;; after setting teachpack to guess.ss
;(repl3 check-guess3)
