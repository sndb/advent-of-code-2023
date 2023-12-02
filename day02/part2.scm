(import (ice-9 rdelim)
        (ice-9 regex))

(let lp ([i 1] [a 0])
  (let ([line (read-line)])
    (if (eof-object? line)
        (display a)
        (lp (+ i 1)
            (let ([h (make-hash-table)])
              (for-each
               (lambda (m)
                 (let* ([t (string-split (match:substring m) #\space)]
                        [n (string->number (car t))]
                        [c (cadr t)])
                   (when (> n (hash-ref h c 0))
                     (hash-set! h c n))))
               (list-matches "[0-9]+ (red|green|blue)" line))
              (+ a (apply * (hash-map->list (lambda (k v) v) h))))))))
(newline)
