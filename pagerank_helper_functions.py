def computeContribs(urls, rank):
    """Calculates URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)


def iteratehelper(links, ranks, contributer, count):
    """Calculates and updates URL ranks continuously using PageRank algorithm"""
    
    ranks=ranks.cache()
    links=links.cache()
    contributer=contributer.cache()
    
    for iteration in range(count):
        print('Running %d iteration' %(iteration))
        contribs = links.join(ranks).flatMap(lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))
        
        ranks = contribs.reduceByKey(lambda x,y:x+y).mapValues(lambda rank: rank * 0.85 + 0.15)
        
        ranks.take(1)

    return ranks
