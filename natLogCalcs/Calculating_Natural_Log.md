

# Calculating Natural Log

Will this Python code calculate the Natural Log value of '5'?

```

from mpmath import mp

mp.dps = 1005

val_ln5 = mp.ln('5')

print(f"ln(5): {val_ln5}")

```

Yes, that code will correctly calculate and print the natural logarithm of 5 ( ***ln(5)*** ) to 1,005 decimal digits of precision[1].

Here is a breakdown of why it works:

1. **from mpmath import mp**: Imports the arbitrary-precision floating-point arithmetic context[[3](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFM8kGHOpsZnZnSeNFcjaMr6T56chKwypVSC4TsV_89SgY6P_ICPpJz9Xen4mkg58Kri-Cs9Pb6tQqrThBQf6Ivpkb6d6OtNXbuUwCt9f-Azj5RPdw%3D)].
2. **mp.dps = 1005**: Sets the decimal places of precision (dps) to 1,005 digits[[4](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHfgq35ZwLmJDEYTFpxvcq5Cwdpo6YueeH6C7BOJOizuQ09WKbi9VN2B97u7zjLj53bEjVu3884-vPrAxdKGgJ9G79nNxC87xJZlSDB0BQAFYbxWQnyBh7NveBts5llDBVxLyTe_8yOnHKPbQ4%3D)]. Any subsequent computations will be evaluated to this precision.
3. **val_ln5 = mp.ln('5')**:mp.ln() computes the natural logarithm (base `ee`)[[5](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFnixQ08y2x7KqUUQl_JYhBzI5stkIU-ibPExsL5AYcZitPe_-cWISq5TgOK-MWBjUqOnpswNvfFpI7zyCF2d1jl1PZ47prsD5cxuPE4TwQS5CYHJeiqKC0HKOVX0ExEA%3D%3D)]. It is equivalent to calling mp.log() with a single argument[[5](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFnixQ08y2x7KqUUQl_JYhBzI5stkIU-ibPExsL5AYcZitPe_-cWISq5TgOK-MWBjUqOnpswNvfFpI7zyCF2d1jl1PZ47prsD5cxuPE4TwQS5CYHJeiqKC0HKOVX0ExEA%3D%3D)].Passing '5' as a string is fully supported[[6](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGFy26RhYE9CpMpM5aI2QwuEvKtYvtZ5NzwReqY-CKaazZgPeDQ5TuuxUBWXMtTL86iXKzVmE4_JQUwBwRUvDFvfDMrCRUrpoXLAL-rZE58A2i7wZeNXkSDjFOTJo0bQwz1VwIHwHLiujMrKt_87wF4ZDvdJJJKjXri1XmD4B8%3D)]. mpmath automatically converts the string directly into an internal arbitrary-precision float (mpf)[[2]
4. **print(f"ln(5): {val_ln5}")**: Correctly formats and outputs the high-precision result (starting with 1.6094379124... followed by 1,005 significant digits)[[5](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFnixQ08y2x7KqUUQl_JYhBzI5stkIU-ibPExsL5AYcZitPe_-cWISq5TgOK-MWBjUqOnpswNvfFpI7zyCF2d1jl1PZ47prsD5cxuPE4TwQS5CYHJeiqKC0HKOVX0ExEA%3D%3D)].

*(Note: While passing '5' as an integer mp.ln(5) also works identically because integers have no floating-point rounding issues, passing strings like '5' or '0.2' is standard best practice in mpmath to prevent Python's built-in 64-bit float from introducing representation errors before mpmath receives the number.)*

Sources

1. [mpmath.org](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFM8kGHOpsZnZnSeNFcjaMr6T56chKwypVSC4TsV_89SgY6P_ICPpJz9Xen4mkg58Kri-Cs9Pb6tQqrThBQf6Ivpkb6d6OtNXbuUwCt9f-Azj5RPdw%3D)
2. [deepwiki.com](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHXw9fVbFBGHqrSFKhGA5Doi0D8mcu3gfWwih2_DqQGGqutOfOSeARWS9Vy9KKnaE5d23nZLPLhao5X0qI_SLpqoOZnYsBcufenduraJ_u4FIFmRfEjp_tD)
3. [mpmath.org](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFM8kGHOpsZnZnSeNFcjaMr6T56chKwypVSC4TsV_89SgY6P_ICPpJz9Xen4mkg58Kri-Cs9Pb6tQqrThBQf6Ivpkb6d6OtNXbuUwCt9f-Azj5RPdw%3D)
4. [mpmath.org](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHfgq35ZwLmJDEYTFpxvcq5Cwdpo6YueeH6C7BOJOizuQ09WKbi9VN2B97u7zjLj53bEjVu3884-vPrAxdKGgJ9G79nNxC87xJZlSDB0BQAFYbxWQnyBh7NveBts5llDBVxLyTe_8yOnHKPbQ4%3D)
5. [mpmath.org](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFnixQ08y2x7KqUUQl_JYhBzI5stkIU-ibPExsL5AYcZitPe_-cWISq5TgOK-MWBjUqOnpswNvfFpI7zyCF2d1jl1PZ47prsD5cxuPE4TwQS5CYHJeiqKC0HKOVX0ExEA%3D%3D)
6. [github.com](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGFy26RhYE9CpMpM5aI2QwuEvKtYvtZ5NzwReqY-CKaazZgPeDQ5TuuxUBWXMtTL86iXKzVmE4_JQUwBwRUvDFvfDMrCRUrpoXLAL-rZE58A2i7wZeNXkSDjFOTJo0bQwz1VwIHwHLiujMrKt_87wF4ZDvdJJJKjXri1XmD4B8%3D)