# Pi by Co-prime

Two stand-alone programs, one written in Python, the other in C. Both
approximate the value of π by using the mathmatical proof that states that the
probability that two random numbers are co-prime is 6/π².

These programs generate pairs of random numbers for a given number of
iterations, and then gets the percentage of those numbers that were co-prime and
then uses this number to aproximate π.

Inspired by a video from Matt Parker (standupmaths) for Pi Day, 2017.
[![Generating π from 1,000 random numbers](http://img.youtube.com/vi/RZBhSi_PwHU/0.jpg)](http://www.youtube.com/watch?v=RZBhSi_PwHU)

Info on the proof: <https://www.cut-the-knot.org/m/Probability/TwoCoprime.shtml>

## Python Script Running

At a minimum, you have to give the program the number of random integer pairs to
generate (must be >= 10).  You can also specify the maximum number when
generating a random number as a second command line parameter.  If `max_number`
is not specified, `sys.maxsize` will be used.  Random numbers that are generated
will be between 1 and `max_number`.

```
$ python3 pi_by_coprime.py -h
usage: pi_by_coprime.py [-h] [-m MAX_NUMBER] [-d] pairs

Aproximate the value of Pi.

positional arguments:
  pairs                 Generate this number of random pairs to approximate
                        pi. This number must be greater than 10.

optional arguments:
  -h, --help            show this help message and exit
  -m MAX_NUMBER, --max-number MAX_NUMBER
                        Specify maximum number for the random number. This
                        number must be greater than 10. If no max_number is
                        speficied, numbers will be generated between 1 and
                        sys.maxsize.
  -d, --debug           Turn on debug output.
```

Output will show the number of pairs, along with the range, the number of pairs
that were co-prime.  Then it will output the approximation of Pi calculated,
along with the "real" value from `math.h` and the percentage difference between
our calculated approximation and the real value.

```
$ python3 pi_by_coprime.py 1000
Generated 1000 pairs of random numbers between 1 and 9223372036854775807
Number of co-primes pairs: 620
----------------------------
Pi approximation is 3.141592653589793
Pi real value is 3.1108550841912757
Percentage difference is 0.99%
```

```
$ python3 pi_by_coprime.py -m 1000 1000
Generated 1000 pairs of random numbers between 1 and 1000
Number of co-primes pairs: 609
----------------------------
Pi approximation is 3.141592653589793
Pi real value is 3.1388241028717223
Percentage difference is 0.09%
```

The debug command line arguement can be set to cause the program to output pairs
generated along with the running state of the co-prime count.

```
$ python3 pi_by_coprime.py -d -m 10 10
Pair 1 generated: <4,6>
 GCD = 2 Co-prime count = 0
Pair 2 generated: <2,6>
 GCD = 2 Co-prime count = 0
Pair 3 generated: <7,6>
 GCD = 1 Co-prime count = 1
Pair 4 generated: <1,8>
 GCD = 1 Co-prime count = 2
Pair 5 generated: <2,8>
 GCD = 2 Co-prime count = 2
Pair 6 generated: <2,7>
 GCD = 1 Co-prime count = 3
Pair 7 generated: <4,5>
 GCD = 1 Co-prime count = 4
Pair 8 generated: <6,10>
 GCD = 2 Co-prime count = 4
Pair 9 generated: <10,3>
 GCD = 1 Co-prime count = 5
Pair 10 generated: <5,1>
 GCD = 1 Co-prime count = 6
Generated 10 pairs of random numbers between 1 and 10
Number of co-primes pairs: 6
----------------------------
Pi approximation is 3.141592653589793
Pi real value is 3.1622776601683795
Percentage difference is 0.65%
```

## C Code Compiling and Running

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

The DEBUG macro can be defined during compile time to cause the program to
output pairs generated along with the running state of the co-prime count.

```
$ gcc -DDEBUG pi_by_coprime.c -o approxpi
$ ./approxpi 10 10
Pair 1 generated: <7,7>
  Co-prime count is at 0
Pair 2 generated: <7,6>
  Co-prime count is at 1
Pair 3 generated: <3,6>
  Co-prime count is at 1
Pair 4 generated: <6,3>
  Co-prime count is at 1
Pair 5 generated: <7,10>
  Co-prime count is at 2
Pair 6 generated: <4,10>
  Co-prime count is at 2
Pair 7 generated: <2,7>
  Co-prime count is at 3
Pair 8 generated: <2,3>
  Co-prime count is at 4
Pair 9 generated: <4,5>
  Co-prime count is at 5
Pair 10 generated: <2,9>
  Co-prime count is at 6
Generated 10 pairs of random numbers between 1 and 10
Number of co-primes pairs: 6
----------------------------
Pi approximation is 3.162278
Pi real value is 3.141593
Percentage difference is 0.656264%
```

