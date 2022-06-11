# Import math Library
import math 

print("""hello welcome to calculator
      please for function a arguoment inter number1 original and number2 for sample 
* for Multiplication
/ Division
% for Divide remaining

factorial => Returns the factorial of a number
acos => cosine (radian)  	Returns the arc cosine of a number
asin => Returns the arc sine of a number
acosh => Returns the inverse hyperbolic cosine of a number
asinh => Returns the inverse hyperbolic sine of a number
atan =>  Returns the arc tangent of a number in radians
atan2 =>  Returns the arc tangent of y/x in radians 
atanh => Returns the inverse hyperbolic tangent of a number
ceil =>Rounds a number up to the nearest integer
comb => Returns the number of ways to choose k items from n items without repetition and order
copysign => Returns a float consisting of the value of the first parameter and the sign of the second parameter
cos => Returns the cosine of a number
cosh => Returns the hyperbolic cosine of a number
degrees => Converts an angle from radians to degrees
dist => Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
erf => Returns the error function of a number
erfc => Returns the complementary error function of a number
exp => Returns E raised to the power of x
expm1 => Returns Ex - 1
fabs => Returns the absolute value of a number
floor => Rounds a number down to the nearest integer 
smod =>Returns the remainder of x/y
frexp => Returns the mantissa and the exponent, of a specified number
fsum => Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
gamma => Returns the gamma function at x
gcd => Returns the greatest common divisor of two integers
hypot =>Returns the Euclidean norm
isclose =>Checks whether two values are close to each other, or not
isfinite=>Checks whether a number is finite or not
isinf => Checks whether a number is infinite or not
isnan => Checks whether a value is NaN (not a number) or not
isqrt => Rounds a square root number downwards to the nearest integer
idexp => Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
lgamma => Returns the log gamma value of x
log => Returns the log gamma value of x
log => Returns the natural logarithm of a number, or the logarithm of number to base
log10 => Returns the base-10 logarithm of x
log1p => Returns the natural logarithm of 1+x
log2 => Returns the base-2 logarithm of x
perm => Returns the number of ways to choose k items from n items with order and without repetition
pow => Returns the value of x to the power of y
prod => Returns the product of all the elements in an iterable
radians => Converts a degree value into radians
remainder => Returns the closest value that can make numerator completely divisible by the denominator
sin => Returns the sine of a number
sinh => Returns the hyperbolic sine of a number
sqrt => Returns the square root of a number
tan => Returns the tangent of a number
tanh => Returns the hyperbolic tangent of a number
trunc => Returns the truncated integer parts of a number
e => Returns Euler's number (2.7182...)
inf => Returns a floating-point positive infinity
nan => Returns a floating-point NaN (Not a Number) value
""")

a=int(input("inter number{1} >> :")) 
b=int(input("inter number{2} >> :"))
c = input("inter action")

if c == "*":
       print(a*b)
elif c =="/":
        print(a/b)
elif c == " %":
    print(a%b)
elif c=="cos":
    print(math.acos(a))
elif c=="sin":
    print(math.asin(a))
elif c=="acosh":
    print(math.acosh(a))
elif c=="asinh":
    print(math.asinh(a))
elif c=="atan":
    print(math.atan(a))
elif c=="atan2":
    print(math.atan2(b,a ))
elif c=="atanh":
    print(math.atanh(a))
elif c=="ceil":
    print(math.ceil(a))
elif c=="comb":
    print(math.comb(a))
elif c=="copysign":
    print(math.copysign(a, b))
elif c=="cos":
    print(math.cos(a))
elif c=="cosh":
    print(math.cosh(a))
elif c=="degrees":
    print(math.degrees(a))
elif c=="dist":
    print(math.dist(a, b))
elif c=="erf":
    print(math.erf(a))
elif c=="erfc":
    print(math.erfc(a))
elif c=="exp":
    print(math.exp(a))
elif c=="expm1":
    print(math.expm1(a))
elif c=="fabs":
    print(math.fabs(a))
elif c=="floor":
    print(math.floor(a))
elif c=="smod":
    print(math.smod(a))
elif c=="flexp":
    print(math.flexp(a))
elif c=="fsum":
    print(math.fsum(a))
elif c=="gamma":
    print(math.gamma(a))
elif c=="gcd":
    print(math.gcd(a, b))
elif c=="hypot":
    print(math.hypot(a))
elif c=="isclose":
    print(math.isclose(a, b))
elif c=="isfinit":
    print(math.isfinite(a))
elif c=="isinf":
    print(math.isinf(a))
elif c=="isnan":
    print(math.isnan(a))
elif c=="isqrt":
    print(math.isqrt(a))
elif c=="idexp":
    print(math.idexp(a))
elif c=="lgamma":
    print(math.lgamma(a))
elif c=="log":
    print(math.log(a,b))
elif c=="log10":
    print(math.log10(a))
elif c=="log1p":
    print(math.log1p(a))
elif c=="log2":
    print(math.log2(a))
elif c=="prem":
    print(math.perm(a))
elif c=="pow":
    print(math.pow(a,b))
elif c=="prod":
    print(math.prod(a,b))
elif c=="radians":
    print(math.radians(a))
elif c=="remainder":  
    print(math.remainder(a,b))
elif c=="sin":
    print(math.sin(a))
elif c=="sinh":
    print(math.sinh(a))
elif c=="sqrt":
    print(math.sqrt(a))
elif c=="tan":
    print(math.tan(a))
elif c=="tanh":
    print(math.tanh(a))
elif c=="trunc":
    print(math.trunc(a))
elif c=="e":
    print(math.e())
elif c=="inf":
    print(math.inf(a))
else:
    print("""<>>>> please inter  value corrent <<<<>
    //>>>Do not worry, the program will run again now...<>""")
     










