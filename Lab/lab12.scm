(define (no-repeats s)
  (if (null? s)
    s
    (cons (car s)
      (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s)))
      )
    )
  )


(define (without-duplicates lst)
  (if (null? lst)
    lst
    (cons (car lst)
      (without-duplicates (filter (lambda (x) (not (= (car lst) x))) (cdr lst)))
      )
    )
  )

(define (reverse lst)
  (define (helper lst acc)
    (if (null? lst)
      acc
      (helper (cdr lst) (cons (car lst) acc))
      )
    )
  (helper lst '())
  )