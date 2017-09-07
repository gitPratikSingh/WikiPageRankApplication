from __future__ import print_function

import re
import sys
import itertools

from operator import add
from pyspark import SparkContext

# import the parser
from sql-to-csv-parser.parse_wiki import *

# import the helper functions  computeContribs and iteratehelper
from pagerank_helper_functions import *

# parse the page file, and generate a csv file 'output/page.csv'
parse_file('wikidumps/simplewiki-20170901-page.sql', 'output')

# parse the page file, and generate a csv file 'output/pagelinks.csv'
parse_file('wikidumps/simplewiki-20170901-pagelinks.sql', 'output')


# Initializing the spark context.
sc = SparkContext(appName="PythonPageRank")

#create a pageRdd and filter the pages in namesspace 0
pageRdd = (sc.textFile('page.csv')
             .map(lambda line:line.split(','))
	     .filter(lambda x:x[1]=='0')
	     .map(lambda x:(x[0],x[2]))
	     .cache())

#create a linksFrmToRdd and filter the pageslinks in namesspace 0
linksFrmToRdd=(sc.textFile('pagelinks.csv')
		 .map(lambda line:line.split(','))
		 .filter(lambda x:x[1]=='0' and x[3]=='0')
		 .map(lambda x:(x[0].replace('\"',''),x[2].replace('\"','').replace("\'",'')))
		 .cache())

#create a groupsRdd. Each tuple of this Rdd will be (fromURL, (Python iterator of all the URLs which be reached from this URL))
groupRdd=linksFrmToRdd.groupByKey().cache()

# create a ranks rdd with the initail ranks of each URL as 1.
ranks=groupRdd.map(lambda url:(url[0], 1))

# lets contribute the initail contribution of the URLs towards each of the outgoing links
# The structure of the intermediate Rdd 'groupRdd.join(ranks)' is a set a tuples like (URL, ((Python iterator of all the URLs which be reached from this URL), rank of the url key))  
# computeContribs function ia a generator function which yields tuples (outgoingURL, rankoftheParentURL/(number of the outgoingURLs))
contributionRdd= groupRdd.join(ranks)
			.flatMap(lambda urlcontribs: computeContribs(urlcontribs[1][0], urlcontribs[1][1]))

# Calculate the new ranks
ranks=contributionRdd.reduceByKey(lambda x,y:x+y).mapValues(lambda rank:rank*0.85 + 0.15)

# Lets iterate this process using a function 'iteratehelper' from pagerank_helper_functions module 
# Here I have used a hadcoded value 1000 which is the number of iterations we want the page rank algorithm to run. We can take this 
# argument from the command line
ranks=iteratehelper(groupRdd, ranks, contributionRdd, 1000)

#display the top 1000 ranked pages!
for (url, rank) in ranks.takeOrdered(1000, key=lambda url_rank_tuple: -1*url_rank_tuple[1]):
    print ('URL: %s, Rank: %s' %(url,rank))

sc.stop()
