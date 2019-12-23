#!/usr/bin/env python3
"""
File: pi_by_coprime.py

Approximates the value of pi by using the mathmatical proof
that states that the probability that two random numbers are co-prime is
6 / pi^2.  This program generates pairs of random numbers for a given
number of iterations, and then gets the percentage of those numbers that
were co-prime and then uses this number to aproximate pi.

Inspired by a video from Matt Parker (standupmaths) for Pi Day, 2017.
  https://www.youtube.com/watch?v=RZBhSi_PwHU

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

Author: E. Chris Pedro
Version: 2019-12-23

MIT License

Copyright (c) 2018 Chris Pedro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import math
import random
import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def approx_pi(num_pairs, max_number, debug):
    output = ('Generated {0} pairs of random numbers between 1 and {1}\n'
    'Number of co-primes pairs: {2}\n'
    '----------------------------\n'
    'Pi approximation is {3}\n'
    'Pi real value is {4}\n'
    'Percentage difference is {5:.2f}%')

    generator = random.SystemRandom()

    sum_coprime = 0
    for i in range(num_pairs):
        rand1 = generator.randint(1, max_number)
        rand2 = generator.randint(1, max_number)
        rand_gcd = gcd(rand1, rand2)

        if rand_gcd == 1: sum_coprime += 1

        if debug:
            print('Pair {} generated: <{},{}>'.format(i + 1, rand1, rand2))
            print(' GCD = {} Co-prime count = {}'.format(rand_gcd, sum_coprime))

    percent_coprime = sum_coprime / num_pairs
    pi_approx = math.sqrt(6.0/percent_coprime)
    pdiff = abs(float(((math.pi - pi_approx) * 100) / pi_approx))

    print(output.format(num_pairs, max_number, sum_coprime, math.pi, pi_approx,
        pdiff))

    return 0


def parse_args(args):
    parser = argparse.ArgumentParser(description='Aproximate the value of Pi.')
    parser.add_argument('-m', '--max-number', type=int, default=sys.maxsize,
        help='Specify maximum number for the random number. This number must '
        'be greater than 10. If no max_number is speficied, numbers will be '
        'generated between 1 and sys.maxsize.')
    parser.add_argument('-d', '--debug', help='Turn on debug output.',
        action='store_true')
    parser.add_argument('pairs', type=int, help='Generate this number of random'
        ' pairs to approximate pi.  This number must be greater than 10.')

    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    num_pairs = args.pairs
    max_number = args.max_number

    if num_pairs < 10:
        print('Pairs must be greater than 10.')
        return 1

    if max_number < 10:
        print('Maximum number must be greater than 10.')
        return 1

    return approx_pi(num_pairs, max_number, args.debug)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


