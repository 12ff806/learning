;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter6_9) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
(define-struct movie (title producer))
(movie-title (make-movie 'ThePhantomMenace 'Lucas))
"should be" 'ThePhantomMenace
(movie-producer (make-movie 'TheEmpireStrikesBack 'Lucas))
"should be" 'Lucas

; for any values x and y,
; (movie-title (make-movie x y)) = x
; for any values x and y,
; (movie-producer (make-movie x y)) = y