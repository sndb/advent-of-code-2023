(import (ice-9 rdelim)
        (ice-9 regex)
        (srfi 1))

(define (numbers s)
  (map (compose string->number match:substring)
       (list-matches "[0-9]+" s)))

(let lp ([a 0])
  (let ([line (read-line)])
    (if (eof-object? line)
        (display a)
        (let* ([l (string-split line #\|)]
               [l1 (cdr (numbers (car l)))]
               [l2 (numbers (cadr l))]
               [i (length (lset-intersection = l1 l2))]
               [p (if (> i 0) (expt 2 (- i 1)) 0)])
          (lp (+ a p))))))
(newline)
