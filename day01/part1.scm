(import (srfi 1)
        (ice-9 rdelim))

(define (has-prefix? p l)
  (or (null? p)
      (and (pair? l)
           (equal? (car p) (car l))
           (has-prefix? (cdr p) (cdr l)))))

(define (digits l)
  (cond
   [(null? l) '()]
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
