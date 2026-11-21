



# Python Floating Point Calculations

## 1. Available Floating Point Types in Python

### Built-In `float`

* Python's built-in `float` is typically an IEEE-754 double-precision binary floating-point value.
* Provides approximately 15-17 significant decimal digits.
* Very fast.
* Suitable for most applications but not for high-precision numerical verification.

Example:

```python
x = 1.0 / 3.0
print(x)
# 0.3333333333333333
```

### `decimal.Decimal`

* Included in Python's standard library.
* Implements decimal floating-point arithmetic rather than binary floating-point arithmetic.
* Precision is user configurable.
* Can represent values such as `0.1` exactly.
* Commonly used for financial and accounting applications.
* Supports arbitrary precision, although performance decreases as precision increases.

Example:

```python
from decimal import Decimal, getcontext

getcontext().prec = 100

x = Decimal(1) / Decimal(3)
print(x)
```

### `mpmath.mpf`

* The primary floating-point type provided by the `mpmath` library.
* Supports arbitrary precision.
* Precision controlled through `mp.dps` (decimal places).
* Designed specifically for scientific and numerical computation.
* Excellent support for transcendental functions, logarithms, exponentials, special functions, root finding, and numerical analysis.

Example:

```python
from mpmath import mp

mp.dps = 1000

x = mp.mpf(1) / 3
print(x)
```

---

## 2. Evaluation of `mpmath` and Alternatives

### Recommendation: `mpmath`

For your stated goal, I recommend using `mpmath`.

Advantages:

* Arbitrary-precision floating-point arithmetic.
* User-controlled precision.
* Mature implementation of:
  * powers
  * logarithms
  * exponentials
  * trigonometric functions
  * hyperbolic functions
  * special functions
  * numerical integration
  * root-finding algorithms
* Widely used for generating high-precision reference values.
* Well-suited for validating numerical algorithms implemented in Go.

Example:

```python
from mpmath import mp

mp.dps = 2000

x = mp.mpf("1.23456789")
result = x ** 37

print(result)
```

### Alternative: `gmpy2`

If maximum performance becomes important, consider `gmpy2`.

Advantages:

* Built on GMP/MPFR



# ***mpmath*** Library



## Example Usage

```python
from mpmath import mp

mp.dps = 2000

x = mp.mpf("1.23456789")
result = x ** 37

print(result)
```



## What is `mp.dps`?

Yes. `mp.dps` is a calculation parameter.

More specifically, it is the **working precision** used by the `mpmath` library.

The abbreviation stands for:

```text
dps = decimal places
```

or more accurately:

```text
dps = decimal digits of precision
```

Example:

```python
from mpmath import mp

mp.dps = 15
```

This tells `mpmath` to perform all calculations using approximately 15 decimal digits of precision.

Example:

```python
from mpmath import mp

mp.dps = 15

print(mp.pi)
```

Output:

```text
3.14159265358979
```

Now increase the precision:

```python
from mpmath import mp

mp.dps = 50

print(mp.pi)
```

Output:

```text
3.1415926535897932384626433832795028841971693993751
```

The value of `mp.dps` affects:

* Addition
* Subtraction
* Multiplication
* Division
* Powers
* Logarithms
* Trigonometric functions
* All other `mpmath` calculations

---

## Why Set `mp.dps` Higher Than Required?

Suppose you want a final answer accurate to 1000 digits.

A common technique is:

```python
mp.dps = 1050
```

The extra 50 digits are called **guard digits**.

These help absorb rounding errors that may occur during intermediate calculations.

After the calculation completes, you can round or truncate the result to the desired 1000 digits.

---

## What is `mp.mpf("1.23456789")`?

Yes.

`mpf()` is a function that constructs an arbitrary-precision floating-point number.

Think of it as the high-precision equivalent of Python's built-in `float()`.

Example:

```python
x = float("1.23456789")
```

creates a standard IEEE-754 double-precision value.

Whereas:

```python
from mpmath import mp

x = mp.mpf("1.23456789")
```

creates an arbitrary-precision `mpmath` floating-point value.

The resulting object type is:

```python
mpmath.ctx_mp_python.mpf
```

Example:

```python
from mpmath import mp

x = mp.mpf("1.23456789")

print(type(x))
```

Output:

```text
<class 'mpmath.ctx_mp_python.mpf'>
```

---

## Why Pass a String?

When high precision matters, always prefer:

```python
mp.mpf("1.23456789")
```

instead of:

```python
mp.mpf(1.23456789)
```

Reason:

```python
1.23456789
```

is first converted into a standard Python `float`.

Any rounding errors introduced by the IEEE-754 representation have already occurred before `mpmath` sees the value.

By passing a string:

```python
mp.mpf("1.23456789")
```

`mpmath` reads the exact decimal digits you supplied.

For generation of test vectors and reference values, I strongly recommend constructing values from strings.

---

## What Is the Maximum Length of the String?

For practical purposes:

```text
There is no fixed maximum number of digits.
```

Examples such as these are valid:

```python
mp.mpf("1.23456789")
```

```python
mp.mpf("3.14159265358979323846264338327950288419716939937510")
```

```python
mp.mpf("1." + "1234567890" * 1000)
```

You can create numbers containing:

* Hundreds of digits
* Thousands of digits
* Tens of thousands of digits
* Millions of digits

The real limits are:

1. Available memory
2. Available computation time
3. The precision setting (`mp.dps`)

---

## Important Relationship Between `mpf()` and `mp.dps`

Consider:

```python
from mpmath import mp

mp.dps = 20

x = mp.mpf(
    "1.2345678901234567890123456789012345678901234567890"
)

print(x)
```

Output:

```text
1.234567890123456789
```

Although the string contains many more digits, `mpmath` stores the value using approximately 20 digits because:

```python
mp.dps = 20
```

Therefore:

```text
mp.dps controls how many digits are retained internally.
```

If you need all 1000 digits:

```python
mp.dps = 1000

x = mp.mpf(long_string)
```

---

## For Your Planned Go Verification Work

I would recommend the following pattern:

```python
from mpmath import mp

mp.dps = 1050

base = mp.mpf(
    "1.23456789012345678901234567890123456789"
)

result = base ** 37

print(result)
```

Key rules:

1. Set `mp.dps` before creating test values.
2. Construct all high-precision inputs from strings.
3. Use 25-100 guard digits above your target precision.
4. Export expected values as decimal strings.
5. Use those strings as authoritative test vectors in Go.

For a mathematical verification framework such as the one you have been building for your Go numerical libraries, this is the approach I would consider best practice.



# ***`gmpy2`*** Math Package



## 1. Background Information on *`gmpy2`*

## What is `gmpy2`?

`gmpy2` is a Python extension module that provides access to three widely respected numerical libraries:

| Underlying Library | Purpose                                                      |
| ------------------ | ------------------------------------------------------------ |
| GMP                | High-performance arbitrary-precision integer arithmetic      |
| MPFR               | Correctly-rounded arbitrary-precision floating-point arithmetic |
| MPC                | Arbitrary-precision complex arithmetic                       |

Unlike `mpmath`, which is implemented primarily in Python, `gmpy2` delegates nearly all heavy numerical work to highly optimized native C libraries.

As a result:

* Extremely fast for large calculations.
* Designed specifically for arbitrary-precision arithmetic.
* Frequently used in computational mathematics and number-theory software.
* Commonly chosen when calculations involve thousands or millions of digits.

---

## Primary Numeric Types

### `mpz`

Arbitrary-precision integer.

Example:

```python
import gmpy2

x = gmpy2.mpz("123456789012345678901234567890")
```

---

### `mpfr`

Arbitrary-precision floating-point value.

Example:

```python
import gmpy2

x = gmpy2.mpfr("1.23456789")
```

This is the type most comparable to `mpmath.mpf`.

---

### `mpc`

Arbitrary-precision complex number.

Example:

```python
import gmpy2

z = gmpy2.mpc("1.5", "2.3")
```

---

## Precision Control

`gmpy2` measures precision in **bits** rather than decimal digits.

Example:

```python
import gmpy2

gmpy2.get_context().precision = 512
```

Approximate conversion:

```text
Decimal Digits ≈ Bits / 3.32193
```

Examples:

| Decimal Digits | Approximate Bits |
| -------------- | ---------------- |
| 15             | 53               |
| 100            | 333              |
| 1000           | 3322             |
| 10000          | 33220            |

---



## 2. When Would `gmpy2` Be Preferable to `mpmath`?

## Short Answer

For accuracy alone:

```text
Usually neither library has an advantage.
```

Both can produce extremely accurate results when configured with sufficient precision.

The real difference is normally:

```text
Performance
```

not

```text
Accuracy
```

---

## Important Distinction

Many developers incorrectly assume:

```text
gmpy2 is more accurate than mpmath
```

This is generally not true.

If both libraries are configured with enough precision:

```python
mp.dps = 1000
```

and

```python
gmpy2.get_context().precision = 3500
```

they should agree to approximately the requested precision.

The question is usually:

```text
How long does the computation take?
```

rather than

```text
How accurate is the answer?
```

---

## Situations Where `gmpy2` Has an Advantage

### Very Large Precision

Examples:

* 10,000 digits
* 100,000 digits
* 1,000,000 digits

In these cases MPFR's optimized algorithms often outperform pure-Python alternatives.

---

### Massive Test Generation

Suppose you are generating:

```text
10,000 logarithm test vectors
```

or

```text
100,000 exponentiation test vectors
```

for a Go library.

`gmpy2` will often complete the work substantially faster.

---

### Correctly Rounded Arithmetic

MPFR was designed around the concept of correctly-rounded arbitrary-precision floating-point arithmetic.

For extremely demanding numerical-validation projects, many researchers consider MPFR one of the reference implementations available.

---

## Situations Where `mpmath` Is Preferable

For your specific project, I would still lean toward `mpmath`.

Reasons:

### Simpler API

Natural logarithm:

```python
mp.log(x)
```

Power:

```python
x ** n
```

Pi:

```python
mp.pi
```

---

### Rich Mathematics Library

`mpmath` contains:

* numerical integration
* root finding
* special functions
* Bessel functions
* zeta functions
* matrix operations
* numerical calculus

In many projects, these capabilities matter more than raw arithmetic performance.

---

### Easier Precision Management

```python
mp.dps = 1000
```

is easier to reason about than:

```python
gmpy2.get_context().precision = 3322
```

because you think directly in decimal digits.

---

## My Recommendation for Your Go Validation Framework

If your target precision is:

```text
50 to 10,000 digits
```

and your goal is:

```text
Generate trusted reference values
```

then I would start with:

```python
mpmath
```

If you later discover that runtime becomes a bottleneck:

```python
gmpy2
```

becomes an excellent optimization path.

Accuracy would not be the reason to switch.

Performance would.

---



## 3. Sample Program: Natural Log of 5 to 45 Digits

Using `mpmath`

```python
from mpmath import mp

# Request slightly more precision than needed.
mp.dps = 55

x = mp.mpf("5")

result = mp.log(x)

# Print 45 digits after the decimal point.
print(f"{result:.45f}")
```

---

## Alternative `gmpy2` Version

```python
import gmpy2

# Approximately 60 decimal digits.
gmpy2.get_context().precision = 200

x = gmpy2.mpfr("5")

result = gmpy2.log(x)

print(result)
```

---

## Recommended Usage

When building the validation infrastructure for your Go numerical libraries:

1. Use `mpmath`.
2. Generate all reference values as strings.
3. Maintain 25-100 guard digits.
4. Store the expected values in test data files.
5. Periodically verify selected vectors against `gmpy2` or MPFR.

Agreement between independent implementations provides stronger evidence of correctness than relying on a single numerical package, regardless of how trusted that package may be.



# Exponentiation

In mpmath, exponentiation is generally performed using Python's exponentiation operator:

result = x ** y


or equivalently:

result = pow(x, y)


where x and/or y may be mpmath.mpf values.

Example:

from mpmath import mp

mp.dps = 50

x = mp.mpf("6.523478")

result = x ** 92

print(result)


There is not a commonly-used mpmath function with a name like:

mp.power(x, y)


or

mp.pow(x, y)


that would be preferred over **.

In fact, the ** operator is the idiomatic and recommended way to perform exponentiation with mpmath.

Why does mpmath work this way?

The mpf class overloads Python's arithmetic operators:

​		+
​		-
​		*
​		/
​		**


Therefore:

```python
x = mp.mpf("6.523478")

x ** 92
```


automatically dispatches to ***mpmath's*** arbitrary-precision exponentiation implementation.

Conceptually, Python is doing something similar to:

x.__pow__(92)


behind the scenes.

#### Three Different Operations

It may help to distinguish these:

**`x ** y`** Computes: **`x^y`**

**`mp.exp(x)`** Computes: **`e^x`**

**`mp.log(x)`** Computes: **`ln(x)`**

For Your Go Validation Work

If your objective is:

```bash
base^integerExponent
```


such as:

```bash
6.523478^92
```


I would write:

```python
base = mp.mpf("6.523478")
exponent = 92

result = base ** exponent
```


and consider that the canonical mpmath solution.

There is one subtle point worth noting. For an integer exponent, ***mpmath*** can often use algorithms based on repeated squaring, which are more efficient and numerically cleaner than forcing the computation through:

```python
mp.exp(exponent * mp.log(base))
```


So even though both expressions are mathematically equivalent,

```python
base ** exponent
```


is typically the better choice when the exponent is a positive integer.

For generating high-precision test vectors for a Go math library, I would use **`**`** for all integer-exponent test cases and reserve **`exp()`** for cases where I truly need to compute **`exe^x`**.
