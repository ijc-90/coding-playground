def comparator(list):
    return lambda x: list[x]

def reviewContainsCompetitor(review, competitor):
    return review.find(' ' + competitor + ' ') >= 0 or \
    review.find(competitor + ' ') == 0 or \
    review.find(' ' + competitor) >= 0 and len(review) == len(' ' + competitor) + review.find(' ' + competitor) or \
    review == competitor


def topNCompetitors(numCompetitors, topNCompetitors, competitors,
                    numReviews, reviews):
    # WRITE YOUR CODE HERE
    print(competitors)
    competitors = list(dict.fromkeys(competitors))
    print(competitors)
    competitors = sorted(competitors)
    competitorsWithUsage = {}
    for competitor in competitors:
        competitorsWithUsage[competitor] = 0
    for review in reviews:
        for competitor in competitors:
            if reviewContainsCompetitor(review,competitor):
                competitorsWithUsage[competitor] += 1
    ranking = sorted(competitorsWithUsage, key= comparator(competitorsWithUsage), reverse= True)
    for competitor in competitors:
        if competitorsWithUsage[competitor] == 0:
            ranking.remove(competitor)
    return ranking[:min(numCompetitors,topNCompetitors, len(competitors))]

#a = topNCompetitors(5,2,['betacellular','anacell','aaaa'], 2,['aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa anacell  el mejor es ', 'aaaa betacellular blabla ', 'aaaa el anacell', 'aaaa betacellular', 'aaaa baba'])




#a = topNCompetitors(5,2,['aa','bb','cc','dd','ee'], 2,['aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa anacell  el mejor es ', 'aaaa betacellular blabla ', 'aaaa el anacell', 'aaaa betacellular', 'aaaa baba'])
#a = topNCompetitors(5,2,['anacell','bb','cc','dd','ee'], 2,['best anacell'])
#a = topNCompetitors(5,2,['anacell'], 2,['best anacell', 'anacell best anacell', 'anacell','blablaanacell',' anacell'])
a = topNCompetitors(5,2,['a', 'b', 'c', 'd', 'e', 'f', 'g', 'g', 'g', 'g', 'g'], 2,['best google glass', 'google best anacell', 'glass','google glasss',' anacell'])
print(a)