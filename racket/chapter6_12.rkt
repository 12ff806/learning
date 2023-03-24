;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter6_12) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
;; a letter is a symbol, one of 'a ... 'z.
;; a word is
;; (make-word FIRST SECOND THIRD)
;; where FIRST is a letter,
;;       SECOND is a letter, and
;;       THIRD is a letter.
(define-struct word (first second third))

;; DATA EXAMPLES
(make-word 'a 'p 'e)
(make-word 'b 'i 'g)
(make-word 'c 'a 't)
(make-word 'd 'o 'g)
(make-word 'e 'l 'm)
(make-word 'f 'i 't)
(make-word 'g 'a 's)


(define-struct student (last first teacher))

(define (subst-teacher a-student a-teacher)
  (cond
    [(symbol=? (student-teacher a-student) 'Fritz)
     (make-student (student-last a-student)
                   (student-first a-student)
                   a-teacher)]
    [else a-student]))

(subst-teacher (make-student 'Find 'Matthew 'Fritz) 'Elise)
(subst-teacher (make-student 'Find 'Matthew 'Amanda) 'Elise)
