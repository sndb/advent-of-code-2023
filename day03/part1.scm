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

(define (symbol-adjacent? r c)
  (any
   (lambda (p)
     (let ([x (apply lines-ref p)])
       (and (not (char-numeric? x))
            (not (char=? x #\.)))))
   (adjacent r c)))

(define (char->number c)
  (- (char->integer c) (char->integer #\0)))

(let lp1 ([r 0] [a1 0])
  (if (< r rows)
      (let lp2 ([c 0] [n 0] [a2 0] [j #f])
        (if (< c cols)
            (let ([x (lines-ref r c)])
              (if (char-numeric? x)
                  (let ([d (char->number x)]
                        [k (symbol-adjacent? r c)])
                    (lp2 (+ c 1) (+ (* n 10) d) a2 (or j k)))
                  (lp2 (+ c 1) 0 (+ a2 (if j n 0)) #f)))
            (lp1 (+ r 1) (+ a1 a2 (if j n 0)))))
      (display a1)))
(newline)
