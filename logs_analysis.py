# !/usr/bin/env python2.7

import psycopg2
from time import gmtime, strftime


def getTopArticles(c, iamount):
    c.execute("""select articles.title, count(log.path)
            from log, articles
            where concat('/article/', articles.slug) = log.path
            group by articles.title
            order by count(log.path) desc LIMIT %s""", (iamount,))
    return c.fetchall()


def printTopArticles(r, f):
    printStr(str(len(r))+" Most Popular Articles Of All Time:", f)
    for x in range(0, len(r)):
        printStr('\t"%s"' % r[x][0] + " - " + str(r[x][1]) + " views", f)


def getTopAuthors(c, iamount):
    c.execute("""select authors.name, count(articles.author)
            from log, articles, authors
            where concat('/article/', articles.slug) = log.path
            and autHors.id = articles.author
            group by authors.name
            order by count(articles.author) desc limit %s""", (iamount,))
    return c.fetchall()


def printTopAuthors(r, f):
    printStr("\n"+str(len(r))+" Most Popular Authors Of All Time:", f)
    for x in range(0, len(r)):
        printStr("\t" + r[x][0] + " - " + str(r[x][1]) + " views", f)


def getDailyErrors(c, iamount):
    c.execute("""select distinctDate, error
            from (select distinct time::date as distinctDate,
            (cast(count(case status when '404 NOT FOUND'
            then 1 else null end) as float)
            / count(method)) * 100 as error from log group by time::date)
            as result where error > %s""", (iamount, ))
    return c.fetchall()


def printErrors(r, f, iamount):
    printStr("\n404 Errors Over " + str(iamount) + "% In Any Given Day:", f)
    for x in range(0, len(r)):
        d = r[x][0].strftime("%B %d, %Y")
        printStr("\t" + d + " - "+("%.1f" % r[x][1])+"%", f)


def printStr(s, f):
    print(s)
    f.write(s + "\n")


def main():
    # connect to database
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    # open text file to write results
    f = open('report.txt', 'w')

    # get and print top articles
    r = getTopArticles(c, 3)
    printTopArticles(r, f)

    # get and print top authors
    r = getTopAuthors(c, 3)
    printTopAuthors(r, f)

    # get and print errors < 1%
    r = getDailyErrors(c, 1.0)
    printErrors(r, f, 1.0)

    # close access to database
    db.close()

    # close text file
    f.close()
    return


if __name__ == '__main__':
    main()
