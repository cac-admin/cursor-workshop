# Mini methods brief: Two-group mean difference with bootstrap CI

Workshop stand-in for a short methods paper. Not a real publication.

## Research question

Do treatment measurements differ in mean from control measurements on the same assay?

## Algorithm box

```
Algorithm 1: Bootstrap confidence interval for mean difference
Input: control values C, treatment values T, B replicates, alpha
1. observed <- mean(T) - mean(C)
2. for b in 1..B:
3.     C_b <- sample(C with replacement, |C|)
4.     T_b <- sample(T with replacement, |T|)
5.     d_b <- mean(T_b) - mean(C_b)
6. lo <- alpha/2 quantile of {d_b}
7. hi <- (1 - alpha/2) quantile of {d_b}
8. return observed, (lo, hi)
```

## Reported defaults in the "paper"

- B = 2000
- alpha = 0.05 (95% CI)
- Empty or non-numeric values are excluded before analysis
- Units are arbitrary assay units (au)

## Acceptance checks for your replication

1. Code implements Algorithm 1 (not a closed-form t-interval only).
2. Using `exercises/uc2-analysis/data/measurements.csv`, print observed difference and 95% CI.
3. Re-running with the same random seed reproduces the same CI endpoints.
4. A short note states what you did and did not replicate from this brief.
