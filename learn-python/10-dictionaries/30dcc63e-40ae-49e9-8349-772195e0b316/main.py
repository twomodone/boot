def merge(dict1, dict2):
    score_dict = {}
    for score in dict1:
        score_dict[score] = dict1[score]
    for score in dict2:
        score_dict[score] = dict2[score]
    return score_dict

def total_score(score_dict):
    sum_of_scores = 0
    for score in score_dict:
        sum_of_scores += score_dict[score]
    return sum_of_scores
