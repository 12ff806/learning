;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter6_1) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp")) #f)))
;; distance-to-0 : posn -> number
(define (distance-to-0 a-posn)
  (sqrt
   (+ (* (posn-x a-posn) (posn-x a-posn))
      (* (posn-y a-posn) (posn-y a-posn)))))

;; distance-to-0-v2: posn -> number
(define (distance-to-0-v2 a-posn)
  (sqrt
   (+ (sqr (posn-x a-posn))
      (sqr (posn-y a-posn)))))

(distance-to-0 (make-posn 0 5))
(distance-to-0-v2 (make-posn 0 5))
(distance-to-0 (make-posn 3 4))
(distance-to-0 (make-posn (* 2 3) (* 2 4)))
(distance-to-0 (make-posn 12 (- 6 1)))