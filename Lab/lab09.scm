(define (over-or-under num1 num2)
  (if (= num1 num2)
    0
    (if (< num1 num2)
      -1
      1
      )))

(define (make-adder num)
  (lambda (add) (+ add num))
  )

(define (composed f g)
  (lambda (x) (f (g x)))
  )

(define (repeat f n)
  (if (< n 1)
    (lambda (x) x)
    (composed f (repeat f (- n 1)))
    )
  )

(define (max a b)
  (if (> a b)
    a
    b))

(define (min a b)
  (if (> a b)
    b
    a))

(define (gcd a b)
  (if (= b 0)
    a
    (gcd b (modulo a b))))

(define (duplicate lst)
  (if (null? lst)
    ()
    (append (list (car lst) (car lst)) (duplicate (cdr lst)))
    )
  )

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s)
  (if (null? s)
    ()
    (if (list? (car s))
      (cons (deep-map fn (car s)) (deep-map fn (cdr s)) )
      (cons (fn (car s)) (deep-map fn (cdr s)))
      )
    )
  )
