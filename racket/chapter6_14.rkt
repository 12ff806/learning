;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname chapter6_14) (read-case-sensitive #t) (teachpacks ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "guess.rkt" "teachpack" "htdp") (lib "master.rkt" "teachpack" "htdp") (lib "draw.rkt" "teachpack" "htdp")) #f)))
;; A time is:
;; (make-time HOURS MINUTES SECONDS)
;; where SECONDS is a number,
;;       MINUTES is a number, and
;;       HOURS is a number.
(define-struct time (hours minutes seconds))

;; time->seconds : time -> number
;; computes the number of seconds since midnight for this time

;; EXAMPLES
;; midnight is 0 seconds after midnight
;; 12:00:01 is 1 seconds after midnight
;; 12:01:00 is 60 seconds after midnight
;; 1:00:00 is 3600 seconds after midnight
;; 1:03:02 is 3782 seconds after midnight

(define (time->seconds t)
  (+ (time-seconds t)
     (* 60 (time-minutes t))
     (* 60 60 (time-hours t))))

;; EXAMPLES TURNED INTO TESTS
(time->seconds (make-time 0 0 0)) "should be" 0
(time->seconds (make-time 0 0 1)) "should be" 1
(time->seconds (make-time 0 1 0)) "should be" 60
(time->seconds (make-time 1 0 0)) "should be" 3600
(time->seconds (make-time 1 3 2)) "should be" 3782