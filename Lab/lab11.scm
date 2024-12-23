(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
  (list keys values)
  )

(define (get-keys-kwlist1 kwlist)
  (car kwlist)
  )

(define (get-values-kwlist1 kwlist)
  (cadr kwlist)
  )

(define (make-kwlist2 keys values)
  (if (or (null? keys) (null? values))
    '()
    (cons (list (car keys) (car values))
      (make-kwlist2 (cdr keys) (cdr values))
      )
    )
  )

(define (get-keys-kwlist2 kwlist)
  (if (null? kwlist)
    '()
    (cons (car (car kwlist))
      (get-keys-kwlist2 (cdr kwlist))
      )
    )
  )

(define (get-values-kwlist2 kwlist)
  (if (null? kwlist)
    '()
    (cons (cadr (car kwlist))
      (get-values-kwlist2 (cdr kwlist))
      )
    )
  )

(define (add-to-kwlist kwlist key value)
  (make-kwlist
    (append (get-keys-kwlist kwlist) (list key))
    (append (get-values-kwlist kwlist) (list value))
    )
  )

(define (get-first-from-kwlist kwlist key)
  (if (null? (get-keys-kwlist kwlist))
    '()
    (if (equal? key (car (get-keys-kwlist kwlist)))
      (car (get-values-kwlist kwlist))
      (get-first-from-kwlist
           (make-kwlist (cdr (get-keys-kwlist kwlist))
                        (cdr (get-values-kwlist kwlist)))
           key)
      )
    )
  )

