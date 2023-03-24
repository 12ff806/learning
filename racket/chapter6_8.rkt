;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter6_8) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
(define-struct movie (title producer))
;; make-movie
;; movie?
;; movie-title
;; movie-producer

(define-struct boyfriend (name hair eyes phone))
;; make-boyfriend
;; boyfriend?
;; boyfriend-name
;; boyfriend-hair
;; boyfriend-eyes
;; boyfriend-phone

(define-struct cheerleader (name number))
;; make-cheerleader
;; cheerleader?
;; cheerleader-name
;; cheerleader-number

(define-struct CD (artist title price))
;; make-CD
;; CD?
;; CD-artist
;; CD-title
;; CD-price

(define-struct sweater (material size producer))
;; make-sweater
;; sweater?
;; sweater-material
;; sweater-size
;; sweater-producer