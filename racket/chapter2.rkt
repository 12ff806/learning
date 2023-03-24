;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname area) (read-case-sensitive #t) (teachpacks ((lib "convert.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "convert.rkt" "teachpack" "htdp")) #f)))
;; total-profit : number -> number
(define (total-profit customers)
  (- (* 5 customers)
     (+ 20
        (* 0.50 customers))))
(total-profit 2)

(define (sum-coins p n d q)
  (+ (* p 1)
     (* n 5)
     (* d 10)
     (* q 25)))
(sum-coins 1 1 1 1)

(define (wage h)
  (* 12 h))

(define (tax w)
  (* 0.15 w))
(tax 1000)

(define (netpay h)
  (- (wage h) (tax (wage h))))
(netpay 40)

(define (f3 n)
  (- 2 (/ 1 n)))
(f3 2)
(f3 9)

(define (f2 n)
  (+ 20 (* (/ 1 2) (* n n))))
(f2 2)
(f2 9)

(define (f1 n)
  (+ 10 (* n n)))
(f1 2)
(f1 9)

(define (f n)
  (+ (/ n 3) 2))
(f 2)
(f 5)
(f 9)

(define (convert3 a b c)
  (+ a (+ (* 10 b) (* 100 c))))
(convert3 1 2 3)

(define (triangle a h)
  (* 1/2 (* a h)))
(triangle 10 10)

(define (dollar->euro d)
  (* d 0.9210))
(dollar->euro 100)

(define (area-of-disk r)
  (* 3.14 (* r r)))
(area-of-disk 10)
(area-of-disk 5)

(define (area-of-ring outer inner)
  (- (area-of-disk outer)
     (area-of-disk inner)))
(area-of-ring 10 5)
(area-of-ring 5 3)

(define (Fahrenheit->Celsius f)
  (* (/ 5 9) (- f 32)))
(Fahrenheit->Celsius 212)
;;(convert-gui Fahrenheit->Celsius)
;;(convert-repl Fahrenheit->Celsius)
;;(convert-file "in.dat" Fahrenheit->Celsius "out.dat")
