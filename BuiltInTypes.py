# Truth Value Testing
"""
* constants defined to be false: None and False
* zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
* empty sequences and collections: '', (), [], {}, set(), range(0)
"""

# Boolean Operations — and, or, not
"""
Operation | Result 
x or y    | if x is true, then x, else y
x and y   | if x is false, then x, else y
not x     | if x is false, then True, else False
"""

# Comparisons
"""
Operation | Meaning
<         | strictly less than
<=        | less than or equal
>         | strictly greater than
>=        | greater than or equal
==        | equal
!=        | not equal
is        | object identity
is not    | negated object identity
"""

# Numeric Types — int, float, complex
"""
| Operation         | Result                                    |
|-------------------|-------------------------------------------|
| x + y             | sum of x and y                            |
| x - y             | difference of x and y                     |
| x * y             | product of x and y                        |
| x / y             | quotient of x and y                       |
| x // y            | floored quotient of x and y               |
| x % y             | remainder of x / y                        |
| -x                | x negated                                 |
| +x                | x unchanged                               |
| abs(x)            | absolute value or magnitude of x          |
| int(x)            | x converted to integer                    |
| float(x)          | x converted to floating point             |
| complex(re, im)   | a complex number with real part re, imaginary part im. im defaults to zero. |
| c.conjugate()     | conjugate of the complex number c         |
| divmod(x, y)      | the pair (x // y, x % y)                  |
| pow(x, y)         | x to the power y                          |
| x ** y            | x to the power y                          |
"""

# Bitwise Operations on Integer Types
"""
| Operation  | Result                        |
|------------|-------------------------------|
| x \| y     | bitwise or of x and y         |
| x ^ y      | bitwise exclusive or of x and y|
| x & y      | bitwise and of x and y        |
| x << n     | x shifted left by n bits      |
| x >> n     | x shifted right by n bits     |
| ~x         | the bits of x inverted        |
Notes:
    1. Negative shift counts are illegal and cause a ValueError to be raised.
    2. A left shift by n bits is equivalent to multiplication by pow(2, n).
    3. A right shift by n bits is equivalent to floor division by pow(2, n).
    4. Performing these calculations with at least one extra sign extension bit in a finite two’s complement representation (a working bit-width of 1 + max(x.bit_length(), y.bit_length()) or more) is sufficient to get the same result as if there were an infinite number of sign bits.
"""

