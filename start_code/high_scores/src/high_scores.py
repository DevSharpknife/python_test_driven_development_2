def latest(scores):
    return scores[-1]


def personal_best(scores):
    sorted_scores = sorted(scores)
    return sorted_scores[-1]


def personal_top_three(scores):
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[0:3]

def hi_to_low_scores(scores):
     sorted_scores = sorted(scores, reverse=True)
     return sorted_scores