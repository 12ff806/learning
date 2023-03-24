;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter6_7) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
(start 50 160)
(draw-solid-disk (make-posn 25 30) 20 'red)
(draw-circle (make-posn 25 80) 20 'yellow)
(draw-circle (make-posn 25 130) 20 'green)

;; clear-bulb : symbol -> true
;; to clear one of the traffic bulbs
(define (clear-bulb color)
  (cond
    [(symbol=? color 'red)
     (and (clear-solid-disk (make-posn 25 30) 20 'red)
          (draw-circle (make-posn 25 30) 20 'red))]
    [(symbol=? color 'yellow)
     (and (clear-solid-disk (make-posn 25 80) 20 'yellow)
          (draw-circle (make-posn 25 80) 20 'yellow))]
    [(symbol=? color 'green)
     (and (clear-solid-disk (make-posn 25 130) 20 'green)
          (draw-circle (make-posn 25 130) 20 'green))]))

;; tests
(clear-bulb 'red)

;; draw-bulb : symbol -> true
;; to draw a bulb on the traffic light
(define (draw-bulb color)
  (cond
    [(symbol=? color 'red)
     (draw-solid-disk (make-posn 25 30) 20 'red)]
    [(symbol=? color 'yellow)
     (draw-solid-disk (make-posn 25 80) 20 'yellow)]
    [(symbol=? color 'green)
     (draw-solid-disk (make-posn 25 130) 20 'green)]))

;; tests
(draw-bulb 'green)

;; switch : symbol symbol -> true
;; to switch the traffic light from one color to the next
(define (switch from to)
  (and (clear-bulb from)
       (draw-bulb to)))

;; tests
(switch 'green 'yellow)
(switch 'yellow 'red)

;; next : symbol -> symbol
;; to switch a traffic light's current color and to return the next one
(define (next current-color)
  (cond
    [(symbol=? current-color 'red)
     (switch 'red 'green)]
    [(symbol=? current-color 'yellow)
     (switch 'yellow 'red)]
    [(symbol=? current-color 'green)
     (switch 'green 'yellow)]))

;(next 'red)
;(next 'green)
;(next 'yellow)
;(next 'red)