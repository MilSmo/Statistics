# Statistics
This is a Python script that contains several statistical hypothesis testing functions. Here's a brief overview of each function:

- NEW(lista): This function calculates the sample variance of a list of numbers.
- HDS(probka, hip_sr, odchylenie, typ_hip, alfa): This function performs a hypothesis test for a single population mean using the t-distribution or normal distribution. It accepts the sample, the hypothesized population mean, the known or estimated population standard deviation, the type of hypothesis (left-tailed, right-tailed, or two-tailed), and the significance level.
- porownanie_srednich(probka1, probka2, wariancja1, wariancja2, ufnosc, typ_hip): This function performs a hypothesis test for the difference between two population means using the t-distribution. It accepts two samples, the known or estimated population variances, the type of hypothesis (left-tailed, right-tailed, or two-tailed), and the significance level.
- zmienne_zalezne(probka1, probka2, sr_roznica,typ_hip, ufnosc): This function performs a hypothesis test for the difference between paired samples using the t-distribution. It accepts two samples of paired data, the hypothesized population mean difference, the type of hypothesis (left-tailed, right-tailed, or two-tailed), and the significance level.
- wariancja(probka, hip_wart, alfa, typ_hip): This function performs a hypothesis test for a population variance using the chi-squared distribution. It accepts a sample, the hypothesized population variance, the type of hypothesis (left-tailed, right-tailed, or two-tailed), and the significance level.
- rozklad_rownomierny(probka, alfa): This function performs a hypothesis test for a uniform distribution using the chi-squared distribution. It accepts a sample and the significance level.

Overall, these functions can be useful for conducting various statistical hypothesis tests in Python.
