;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter3_3) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp")) #f)))
;; CONSTANTS
(define cm-per-inch 2.54)
(define inches-per-foot 12)
(define feet-per-yard 3)
(define yards-per-rod (+ 5 1/2))
(define rods-per-furlong 40)
(define furlongs-per-mile 8)

;; inches->cm : number[inches] -> number[cm]
;; to determine the number of cm in some number of inches
(define (inches->cm inches)
  (* cm-per-inch inches))

;; feet->inches : number[feet] -> number[inches]
;; to determine the number of inches in some number of feet
(define (feet->inches feet)
  (* inches-per-foot feet))

;; volume-cylinder : number number -> number
;; to determine to volume of a cylinder from its radius and height
(define (volume-cylinder radius height)
  (* (area-circle radius) height))

;; area-circle : number -> number
;; to determine the area of a circle
;;(define (area-circle radius)
;;  (* radius radius pi))

;; area-pipe-one-def: number number number -> number
;; to determine the area of a pipe with given inner radius, length, and thickness
;; this version does not use any helper functions
(define (area-pipe-one-def inner len thickness)
  (+ (* 2 (- (* pi (+ inner thickness) (+ inner thickness))
             (* pi inner inner)))
     (* (* 2 pi (+ inner thickness)) len)
     (* (* 2 pi inner) len)))

;; area-pipe : number number number -> number
;; to determine the area of a pipe with given inner radius, length, and thickness
(define (area-pipe inner len thickness)
  (+ (* 2 (area-donut inner (+ inner thickness)))
     (* len (* 2 pi (+ inner thickness)))
     (* len (* 2 pi inner))))

;; area-donut : number number -> number
;; finds the area of a circle with a chunk missing
;; the entire circle has radius outer and the missing
;; middle portion has radius inner.
(define (area-donut inner outer)
  (- (area-circle outer)
     (area-circle inner)))

;; area-circle : number -> number
;; determines the area of a circle with given radius
(define (area-circle r)
  (* pi r r))

;; circumference : number -> number
;; determines the circumference of a circle with given radius
(define (circumference r)
  (* 2 pi r))


;; EXAMPLES AS TESTS
(area-circle 1)
(volume-cylinder 3 2)

(area-pipe 2 3 4)
(area-pipe-one-def 2 3 4)

(inches->cm 10)
(feet->inches 10)