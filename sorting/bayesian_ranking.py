
def score(self, ratings, rating_prior, rating_utility):
    '''
        score: [int], [int], [float] -> float
        Return the expected value of the rating for an item with known ratings
        specified by `ratings`, prior belief specified by `rating_prior`, and a utility
        function specified by `rating_utility`, assuming the ratings are a
        multinomial distribution and the prior belief is a Dirichlet distribution.
    '''
    ratings = [r + p for (r, p) in zip(ratings, rating_prior)]
    score = sum(r * u for (r, u) in zip(ratings, rating_utility)) / sum(ratings)
    return score
