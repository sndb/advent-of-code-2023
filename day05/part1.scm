(import (ice-9 rdelim)
        (ice-9 regex))

(define (numbers s)
  (map (compose string->number match:substring)
       (list-matches "[0-9]+" s)))

(define (correspond cs x)
  (if (null? cs)
      x
      (let lp ([c (car cs)])
        (if (null? c)
            (correspond (cdr cs) x)
            (let* ([r (car c)]
                   [d (- x (cadr r))])
              (if (<= 0 d (- (caddr r) 1))
                  (correspond (cdr cs) (+ (car r) d))
                  (lp (cdr c))))))))

(define lines
  (let lp ()
    (let ([l (read-line)])
      (if (eof-object? l) '() (cons l (lp))))))

(define categories
  (let lp ([l (cdddr lines)]
           [c '()])
    (if (null? l)
        `(,c)
        (let ([a (car l)])
          (if (equal? a "")
              (cons c (lp (cddr l) '()))
              (lp (cdr l) (cons (numbers a) c)))))))

(define seeds
  (numbers (car lines)))

(define locations
  (map (lambda (s) (correspond categories s)) seeds))

(display (apply min locations))
(newline)
