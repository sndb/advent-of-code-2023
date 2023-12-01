(import (srfi 1)
        (ice-9 rdelim))

(define (has-prefix? p l)
  (or (null? p)
      (and (pair? l)
           (equal? (car p) (car l))
           (has-prefix? (cdr p) (cdr l)))))

(define numbers
  '((1 . "one")
    (2 . "two")
    (3 . "three")
    (4 . "four")
    (5 . "five")
    (6 . "six")
    (7 . "seven")
    (8 . "eight")
    (9 . "nine")))

(define (digits l)
  (cond
   [(null? l) '()]
   [(find (lambda (a)
            (let ([p (string->list (cdr a))])
              (has-prefix? p l)))
          numbers)
    => (lambda (a)
         (cons (car a) (digits (cdr l))))]
   [(char-numeric? (car l))
    (let ([d (- (char->integer (car l))
                (char->integer #\0))])
      (cons d (digits (cdr l))))]
   [else (digits (cdr l))]))

(let lp ([n 0])
  (let ([line (read-line)])
    (if (eof-object? line)
        (display n)
        (let* ([ds (digits (string->list line))]
               [d1 (car ds)]
               [d2 (last ds)])
          (lp (+ n (+ (* d1 10) d2)))))))
(newline)
