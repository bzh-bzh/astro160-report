from scipy.optimize import fsolve


def gaia_passband_to_b_minus_v(gbp_minus_grp):
    def fit(b_minus_v):
        return gbp_minus_grp - (0.03147 + 1.456 * b_minus_v - 0.6043 * b_minus_v**2 + 0.1750 * b_minus_v**3)
    
    result = fsolve(fit, 1)
    
    return result[0]

def teff(b_minus_v):
    return 4600 * ((1 / (0.92 * b_minus_v + 1.7)) + (1 / (0.92 * b_minus_v + 0.62)))