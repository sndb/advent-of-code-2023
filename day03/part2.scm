(import (ice-9 rdelim)
        (srfi 1))

(define lines
  (let f ()
    (let ([l (read-line)])
      (if (eof-object? l) '() (cons l (f))))))

(define rows (length lines))
(define cols (string-length (car lines)))

(define (lines-ref r c)
  (string-ref (list-ref lines r) c))

(define (adjacent r c)
  (append-map
   (lambda (dr)
     (filter-map
      (lambda (dc)
        (let ([ar (+ r dr)] [ac (+ c dc)])
          (and (<= 0 ar (- rows 1))
               (<= 0 ac (- cols 1))
               (not (= 0 dr dc))
               `(,ar ,ac))))
      (iota 3 -1)))
   (iota 3 -1)))

(define (adjacent-gears r c)
  (filter
   (lambda (p)
     (let ([x (apply lines-ref p)])
       (char=? x #\*)))
   (adjacent r c)))

(define (char->number c)
  (- (char->integer c) (char->integer #\0)))

(define gears (make-hash-table))

(define (gears-add! g n)
  (let ([l (hash-ref gears g '())])
    (hash-set! gears g (cons n l))))

(let lp1 ([r 0])
  (if (< r rows)
      (let lp2 ([c 0] [n 0] [j '()])
        (if (< c cols)
            (let ([x (lines-ref r c)])
              (if (char-numeric? x)
                  (let* ([d (char->number x)]
                         [k (adjacent-gears r c)]
                         [u (lset-union equal? j k)])
                    (lp2 (+ c 1) (+ (* n 10) d) u))
                  (begin
                    (for-each (lambda (g) (gears-add! g n)) j)
                    (lp2 (+ c 1) 0 '()))))
            (begin
              (for-each (lambda (g) (gears-add! g n)) j)
              (lp1 (+ r 1)))))))

(define ratios
  (hash-map->list
   (lambda (k v)
     (if (= (length v) 2)
         (apply * v)
         0))
   gears))

(display (apply + ratios))
(newline)
