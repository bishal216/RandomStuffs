from scipy import stats
question = '07 05 96 14 10 90 21 15 84 28 20 78 35 25 72 42 30 66 49 35 60 56 40 54 63 45 48 70 50 42 77 55 36 84 60 30 91 65 24 98 70 18 07 75 12 14 80 06 21 85 96 28 90 35 95 84 42 05 78 49 10 72 56 15 66 63 20 60 70 25 54 77 30 48 84 35 42 91 40 36 98 45 30 07 50 24 14 55 18 21'

input = [int(i) for i in question.split()]
input.sort()
def cdf(x,sample):
    # Counts how many observations are below x
    cdf = sum(sample <= x)
    # Divides by the total number of observations
    cdf = cdf / len(sample)
    return cdf

def ks_norm(sample):
    # Evaluates the KS statistic
    D_ks = [] # KS Statistic list
    for x in sample:
        cdf_normal = stats.norm.cdf(x = x, loc = 0, scale = 1)
        cdf_sample = cdf(sample = sample, x  = x)
        D_ks.append(abs(cdf_normal - cdf_sample))
    ks_stat = max(D_ks)
    # Calculates the P-Value based on the two-sided test
    # The P-Value comes from the KS Distribution Survival Function (SF = 1-CDF)
    p_value = stats.kstwo.sf(ks_stat, len(sample))
    return {"ks_stat": ks_stat, "p_value" : p_value}
    
ks_norm(input)