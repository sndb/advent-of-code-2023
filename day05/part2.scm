(import (ice-9 rdelim)
        (ice-9 regex)
        (srfi 1))

(define (numbers s)
  (map (compose string->number match:substring)
       (list-matches "[0-9]+" s)))

(define (in? a b)
  (let* ([a0 (car a)]
         [a1 (+ a0 (cdr a))]
         [b0 (car b)]
         [b1 (+ b0 (cdr b))])
    (<= a0 b0 b1 a1)))

(define (projection a b)
  (filter (lambda (p)
            (in? a p))
          (intersect a b)))

(define (intersect a b)
  (let* ([a0 (car a)]
         [a1 (+ a0 (cdr a))]
         [b0 (car b)]
         [b1 (+ b0 (cdr b))]
         [h (min a0 b0)]
         [i (max a0 b0)]
         [j (min a1 b1)]
         [k (max a1 b1)])
    (if (or (< b1 a0) (< a1 b0))
        `(,a)
        (filter (lambda (p)
                  (positive? (cdr p)))
                `((,h . ,(- i h))
                  (,i . ,(- j i))
                  (,j . ,(- k j)))))))

(define (correspond a r)
  (let* ([d (car r)]
         [b (cdr r)]
         [o (- d (car b))])
    (call-with-values
        (lambda ()
          (partition (lambda (p)
                       (in? b p))
                     (projection a b)))
      (lambda (m r)
        (values (map (lambda (p)
                       (cons (+ (car p) o) (cdr p)))
                     m)
                r)))))

(define (correspond* a rs)
  (call-with-values
      (lambda ()
        (correspond a (car rs)))
    (lambda (m r)
      (if (null? (cdr rs))
          (append m r)
          (let ([q (append-map (lambda (p)
                                 (correspond* p (cdr rs)))
                               r)])
            (append m q))))))

(define (solve cs as)
  (if (null? cs)
      as
      (solve (cdr cs)
             (append-map (lambda (a)
                           (correspond* a (car cs)))
                         as))))

(define lines
  (let lp ()
    (let ([l (read-line)])
      (if (eof-object? l) '() (cons l (lp))))))

(define categories
  (let lp ([l (cdddr lines)] [c '()])
    (if (null? l)
        `(,c)
        (let ([a (car l)])
          (if (equal? a "")
              (cons c (lp (cddr l) '()))
              (let* ([n (numbers a)]
                     [r `(,(car n) ,(cadr n) . ,(caddr n))])
                (lp (cdr l) (cons r c))))))))

(define seeds
  (let lp ([l (numbers (car lines))])
    (if (null? l)
        '()
        (cons (cons (car l) (cadr l))
              (lp (cddr l))))))

(display (apply min (map car (solve categories seeds))))
(newline)
