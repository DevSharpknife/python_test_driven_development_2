def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]

def hi_to_low_scores(scores):
    return sorted(scores, reverse=True)


