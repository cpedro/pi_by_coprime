Pi by Co-prime
==============

A stand-alone C program that approximates the value of π by using the
mathmatical proof that states that the probability that two random numbers are
co-prime is 6/π².  

This program generates pairs of random numbers for a given number of iterations,
and then gets the percentage of those numbers that were co-prime and then uses
this number to aproximate π.

Inspired by a video from Matt Parker (standupmaths) for Pi Day, 2017.
[![Generating π from 1,000 random numbers](http://img.youtube.com/vi/RZBhSi_PwHU/0.jpg)](http://www.youtube.com/watch?v=RZBhSi_PwHU)

Info on the proof: <https://www.cut-the-knot.org/m/Probability/TwoCoprime.shtml>

Compiling and Running
---------------------
```
$ gcc pi_by_coprime.c -o approxpi
```

At a minimum, you have to give the program the number of random integer pairs to
generate (must be >= 10).  You can also specify the maximum number when
generating a random number as a second command line parameter.  If `max_number`
is not specified, `LONG_MAX` from `limits.h` will be used.  Random numbers that
are generated will be between 1 and `max_number`.

```
$ ./approxpi
usage: ./approxpi <pairs> [<max_number>]
```

Output will show the number of pairs, along with the range, the number of pairs
that were co-prime.  Then it will output the approximation of Pi calculated,
along with the "real" value from `math.h` and the percentage difference between
our calculated approximation and the real value.

```
$ ./approxpi 1000
Generated 1000 pairs of random numbers between 1 and 9223372036854775807
Number of co-primes pairs: 617
----------------------------
Pi approximation is 3.118409
Pi real value is 3.141593
Percentage difference is 0.740699%
```

```
$ ./approxpi 1000 1000
Generated 1000 pairs of random numbers between 1 and 1000
Number of co-primes pairs: 608
----------------------------
Pi approximation is 3.141404
Pi real value is 3.141593
Percentage difference is 0.005995%
```

