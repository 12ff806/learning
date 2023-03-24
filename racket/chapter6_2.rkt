;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter6_2) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
(start 300 300)
;(draw-solid-line (make-posn 20 20) (make-posn 300 300) 'green)
;(draw-solid-rect (make-posn 20 20) 50 100 'red)
;(draw-solid-disk (make-posn 100 100) 50 'blue)
;(draw-circle (make-posn 200 200) 100 'brown)

(draw-solid-line (make-posn 1 1) (make-posn 5 5) 'red)
(draw-solid-rect (make-posn 20 10) 50 200 'blue)
(draw-circle (make-posn 200 10) 50 'red)
;(draw-solid-disk (make-posn 200 10) 50 'green)
;(stop)