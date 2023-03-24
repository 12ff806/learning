;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter6_13) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
(define-struct student (last first teacher))


(define a (make-student 'findler 'kathi 'matthias))


(define (check a-student a-teacher)
  (cond
    [(symbol=? (student-teacher a-student) a-teacher)
     (student-last a-student)]
    [else 'none]))

(check a 'matthias)
(check a 'barrl)


(define (transfer a-student a-teacher)
  (make-student (student-last a-student)
                (student-first a-student)
                a-teacher))

