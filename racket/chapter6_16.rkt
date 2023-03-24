;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter6_16) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
;; teachpack: draw.ss

;; A rectangle is a structure:
;; (make-rectangle P W H C)
;; where P is a posn, W is a number and H is a number
(define-struct rectangle (nw-corner width height color))

;; DATA EXAMPLES
(define example-rectangle1 (make-rectangle (make-posn 20 20) 260 260 'red))
(define example-rectangle2 (make-rectangle (make-posn 60 60) 180 180 'blue))

#|
;; Template
(define (fun-for-rectangle a-rectangle)
  ... (rectangle-nw-corner a-rectangle) ...
  ... (rectangle-width a-rectangle) ...
  ... (rectangle-height a-rectangle) ...
  ... (rectangle-color a-rectangle) ...)
|#

;; --------------------------------------------------------------------------------

;; draw-a-rectangle : rectangle -> true
;; to draw a-rectangle
(define (draw-a-rectangle a-rectangle)
  (draw-solid-rect
   (rectangle-nw-corner a-rectangle)
   (rectangle-width a-rectangle)
   (rectangle-height a-rectangle)
   (rectangle-color a-rectangle)))

;; EXAMPLES
(start 300 300)
(draw-a-rectangle example-rectangle1)
(draw-a-rectangle example-rectangle2)

;; --------------------------------------------------------------------------------

;; in-rectangle? : rectangle posn -> boolean
;; to determine if a-posn is in a-rectangle, or not
(define (in-rectangle? a-rectangle a-posn)
  (and (<= (posn-x (rectangle-nw-corner a-rectangle))
           (posn-x a-posn)
           (+ (posn-x (rectangle-nw-corner a-rectangle))
              (rectangle-width a-rectangle)))
       (<= (posn-y (rectangle-nw-corner a-rectangle))
           (posn-y a-posn)
           (+ (posn-y (rectangle-nw-corner a-rectangle))
              (rectangle-height a-rectangle)))))

;; EXAMPLES AS TESTS
(in-rectangle? example-rectangle1 (make-posn 0 0)) "should be" false
(in-rectangle? example-rectangle1 (make-posn 25 0)) "should be" false
(in-rectangle? example-rectangle1 (make-posn 0 25)) "should be" false
(in-rectangle? example-rectangle1 (make-posn 25 25)) "should be" true

;; --------------------------------------------------------------------------------

;; translate-rectangle : rectangle number -> rectangle
;; to translate a-rectangle horizontally by x pixels
(define (translate-rectangle a-rectangle x)
  (make-rectangle (make-posn
                   (+ x (posn-x (rectangle-nw-corner a-rectangle)))
                   (posn-y (rectangle-nw-corner a-rectangle)))
                  (rectangle-width a-rectangle)
                  (rectangle-height a-rectangle)
                  (rectangle-color a-rectangle)))

;; EXAMPLES AS TESTS
(translate-rectangle example-rectangle1 30)
"should be"
(make-rectangle (make-posn 50 20) 260 260 'red)

;; --------------------------------------------------------------------------------

;; clear-a-rectangle : rectangle -> true
;; to clear a rectangle
(define (clear-a-rectangle a-rectangle)
  (clear-solid-rect
   (rectangle-nw-corner a-rectangle)
   (rectangle-width a-rectangle)
   (rectangle-height a-rectangle)))

;; EXAMPLES
(start 300 300)
(draw-a-rectangle example-rectangle1)
(draw-a-rectangle example-rectangle2)
(clear-a-rectangle example-rectangle1)
(clear-a-rectangle example-rectangle2)

;; --------------------------------------------------------------------------------


;; draw-and-clear-rectangle : rectangle -> true
(define (draw-and-clear-rectangle a-rectangle)
  (and (draw-a-rectangle a-rectangle)
       (sleep-for-a-while 1/2)
       (clear-a-rectangle a-rectangle)))

;; move-rectangle : number rectangle -> rectangle
(define (move-rectangle delta a-rectangle)
  (cond
    [(draw-and-clear-rectangle a-rectangle)
     (translate-rectangle a-rectangle delta)]
    [else a-rectangle]))

;; EXAMPLES AS TEST
(start 290 90)
(draw-a-rectangle
 (move-rectangle
  20 (move-rectangle
      20 (move-rectangle
          20 (move-rectangle
              20 (move-rectangle
                  20 (move-rectangle
                      20 (move-rectangle
                          20 (move-rectangle
                              20 (move-rectangle
                                  20 (move-rectangle
                                      20 (make-rectangle (make-posn 20 20) 50 50 'red))))))))))))