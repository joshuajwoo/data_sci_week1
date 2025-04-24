# 1  How do you assess the statistical-significance of an insight?
# 	1.	Formulate null (H₀) and alternative (H₁) hypotheses.
# 	2.	Choose a test suited to the data type & design (t-test, χ², ANOVA, regression, etc.).
# 	3.	Verify assumptions (normality, independence, equal variances…).
# 	4.	Compute the test statistic and its p-value.
# 	5.	Compare p-value with the chosen α (e.g., 0.05). If p < α, reject H₀ → the insight is statistically significant.
# 	6.	Report effect size & confidence interval—significance alone is not practical relevance.
#
# ⸻
#
# 2  Central Limit Theorem (CLT)
#
# For any population with finite mean μ and variance σ², the distribution of the sample mean \bar X approaches a normal distribution as sample size n → ∞, regardless of the population’s shape; specifically
#
# Why it matters
# 	•	Lets us apply z-scores, t-tests, CIs, etc. to real-world data whose parent distribution is unknown.
# 	•	Underpins A/B testing, regression inference, control-charting, bootstrapping accuracy estimates.
#
# ⸻
#
# 3  Statistical power
#
# Probability that a test correctly rejects a false null (1 – β). High power (≥ 0.8) means low risk of Type-II error. Determined by: effect size, variance, α level, and sample size. Used in sample-size calculations.
#
# ⸻
#
# 4  Controlling for biases
# 	•	Randomization (assignment, sampling)
# 	•	Blinding / double-blinding
# 	•	Stratification / blocking
# 	•	Matching / propensity scores
# 	•	Including covariates in regression (ANCOVA)
# 	•	Instrumental variables for endogeneity
# 	•	Rigorous data-cleaning to remove outliers, survivorship, measurement bias.
#
# ⸻
#
# 5  Confounding variables
#
# A variable correlated with both the independent variable and the outcome, giving a spurious association. Example: ice-cream sales ↔ drowning deaths; temperature is the confounder. Must be measured & adjusted (regression, stratification) or eliminated via randomization.
#
# ⸻
#
# 6  What is A/B testing?
#
# A controlled, randomized experiment comparing two (or more) variants—A (control) vs. B (treatment). Measure a key metric (conversion, CTR). Use statistical tests (z-test for proportions, t-test for means) to decide whether the observed difference is significant.
#
# ⸻
#
# 7  Confidence intervals (CI)
#
# A range built from sample data that, with a chosen confidence level (e.g., 95 %), is expected to contain the true population parameter.
# Interpretation: if we repeated the sampling many times, ≈ 95 % of such intervals would cover the true parameter—not that there’s a 95 % probability the parameter lies in any one computed interval.