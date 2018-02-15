
/*
 * pi_by_coprime.c
 *
 * Approximates the value of pi by using the mathmatical proof
 * that states that the probability that two random numbers are co-prime is 
 * 6 / pi^2.  This program generates pairs of random numbers for a given 
 * number of iterations, and then gets the percentage of those numbers that
 * were co-prime and then uses this number to aproximate pi.
 *
 * Inspired by a video from Matt Parker (standupmaths) for Pi Day, 2017. 
 *   https://www.youtube.com/watch?v=RZBhSi_PwHU
 *
 * Command line arguments:
 *   <pairs> - generate this number of random pairs to approximate pi.  This
 *     number must be greater than 10.
 *   [<max_number>] - Optional, specify maximum number for the random number.
 *     If no max_number is speficied, numbers will be generated between 1 and 
 *     RAND_MAX.
 *
 * Author: E. Chris Pedro
 * Date: 2017-03-13
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>


/**
 * gcd - Uses Euclid's Algorithm to recursively calculate the GCD of two
 *       numbers, m and n
 * @m: integer 1
 * @n: integer 2
 * Return the GCD of m and n as an integer.
 */
long gcd(long m, long n)
{
  if (m == 0) 
    return n;
  return gcd(n % m, m);
}

/**
 * percentage_difference - Calculates percentage difference between two double
 *                         values and returns a double value
 * @m: double 1
 * @n: double 2
 * Return the percentage differance of m and n
 */
double percentage_difference(double m, double n)
{
  double pdiff, avg, abdiff;

  avg = (m + n) / 2;
  abdiff = fabs(m - n);
  pdiff = (abdiff / avg) * 100;

  return pdiff;
}

/**
 * approx_pi - Estimate the value of pi using Euclid's algorithm.  Prints out
 *             out both the approximation calculate, the "real" value and a
 *             percentage difference between the two
 * @pairs: number of pairs of number to use
 * @max_number: the maximum number to be used when generating random numbers
 */
void approx_pi(int pairs, long max_number)
{
  int i, sum_coprime = 0;
  long rand1, rand2;
  double percentage_coprime, pi_approx, pi = M_PI, pdiff;

  /* Generate random pairs and keep track of pairs that were co-prime */
  srandomdev();
  for (i = 0; i < pairs; ++i)
  {
    rand1 = random() % max_number;
    rand2 = random() % max_number;

    if (gcd(++rand1, ++rand2) == 1)
      ++sum_coprime;
  }

  /* Approximate pi */
  percentage_coprime = (double)sum_coprime / pairs;
  pi_approx = sqrt(6/percentage_coprime);
  pdiff = percentage_difference(pi_approx, pi);

  /* Print out results along with 'real' value and percentage difference */
  printf("Generated %d pairs of random numbers between 1 and %ld\n", 
    pairs, max_number);
  printf("Number of co-primes pairs: %d\n", sum_coprime);
  printf("----------------------------\n");
  printf("Pi approximation is %lf\n", pi_approx);
  printf("Pi real value is %lf\n", pi);
  printf("Percentage difference is %lf%%\n", pdiff);
}

/*
 * main
 */
int main(int argc, char *argv[])
{
  int pairs;
  long max_number = LONG_MAX;
  
  if (argc < 2)
  {
    printf("usage: %s <pairs> [<max_number>]\n", argv[0]);
    return EXIT_FAILURE;
  }

  /* Using atoi and atol because it works for this simple program */
  pairs = atoi(argv[1]);
  if (argc > 2)
    max_number = atol(argv[2]);

  if (pairs < 10)
  {
    printf("%d must be greater than 10.\n", pairs);
    return EXIT_FAILURE;
  }

  approx_pi(pairs, max_number);
  
  return EXIT_SUCCESS;
}


