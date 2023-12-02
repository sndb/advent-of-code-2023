(import (ice-9 rdelim)
        (ice-9 regex))

(define limits
  '(("red" . 12)
    ("green" . 13)
    ("blue" . 14)))

(let lp ([i 1] [a 0])
  (let ([line (read-line)])
    (if (eof-object? line)
        (display a)
        (lp (+ i 1)
            (call/cc
             (lambda (k)
               (for-each
                (lambda (m)
                  (let* ([t (string-split (match:substring m) #\space)]
                         [n (string->number (car t))]
                         [c (cadr t)])
                    (when (> n (cdr (assoc c limits)))
                      (k a))))
                (list-matches "[0-9]+ (red|green|blue)" line))
               (+ a i)))))))
(newline)
