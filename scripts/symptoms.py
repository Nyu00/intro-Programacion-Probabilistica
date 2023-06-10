def calc_bayes(prior_A, prob_B_since_A, prob_B):
    return(prior_A * prob_B_since_A)/ prob_B

if __name__ == '__main__':
    prob_cancer = 1 / 100000
    prob_no_cancer = 1 - prob_cancer

    prob_symptoms_since_cancer = 1
    prob_symptoms_since_no_cancer = 10 / 99999

    prob_symptoms = (prob_symptoms_since_cancer * prob_cancer) + (prob_symptoms_since_no_cancer * prob_no_cancer)

    prob_cancer_since_sintomas = calc_bayes(prob_cancer, prob_symptoms_since_cancer, prob_symptoms)

    print(f"There's a {round(prob_cancer_since_sintomas,4) * 100}% chance that you have cancer since a have symptoms")


    