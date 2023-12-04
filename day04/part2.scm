(import (ice-9 rdelim)
        (ice-9 regex)
        (srfi 1))

(define (numbers s)
  (map (compose string->number match:substring)
       (list-matches "[0-9]+" s)))

(define cards
  (list->vector
   (let lp ()
     (let ([line (read-line)])
       (if (eof-object? line)
           '()
           (let* ([l (string-split line #\|)]
                  [l1 (cdr (numbers (car l)))]
                  [l2 (numbers (cadr l))]
                  [n (length (lset-intersection = l1 l2))])
             (cons n (lp))))))))

(let lp ([a 0] [q (iota (vector-length cards))])
  (if (null? q)
      (display a)
      (let* ([i (car q)]
             [n (vector-ref cards i)]
             [l (iota n (+ i 1))])
        (lp (+ a 1) (append l (cdr q))))))
(newline)
