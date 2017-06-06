# -*- encoding:utf-8 -*-
#
import json
import os

from intellif.IntellifAutotestClass import DbData
from intellif.request_method import post, get


def search(feature, rows='1000', ip='192.168.2.33:8986'):
    source = {
        "q": "*%3A*",
        "fq": "type%3A1+AND+time%3A%5B2015-10-01T15%3A59%3A59Z+TO+2017-05-31T15%3A59%3A59Z%5D",
        "wt": "json",
        "indent": "true",
        "feature": "0@vu9lAMejG70kH1U9i/6WvfUPoj3mjXa9ow7ePFVdpb2lBQY%2BcmcKPp/kGT273Li9Fm%2B/vYZ9p72ElbQ95N44Pp4B37yMK7w9zxdkvBOlOj10SBO9AinwvI3hwTvY2bM9yrPqvdREV73OAfG84xQive05fr3OMDa9zDU2Pp/CCr3sB/e9scQ6vRqR1jdI2kQ%2B0qwHPLsEkz0JL%2BK7QRCavQsmPz2LbKQ9n6SrPSDrIr7%2BxYW7XtJEPpZJVrzym%2B09Bba/vZGfJz6YOrE9qlvjPIrmzj0WOlu9jtktPVI1hL3kapE9opk9vThrGrwqxGO%2BBGoYvruzF77XIaS9zsjXOwld0T1xOFQ9HCHavC3sFj4W82m7b%2Bd3PLa4pjwxB0y9KMogvm3aKTzNNfQ9%2BUj2vSpwfz2VUHY8%2BfH0vKQ6RD09M%2Bu9MeIavTzL1rz3eQo9%2BS4NOxauYr2grkC9HzH1PB0T5T18wKS9th9RvWPjXDto9169Qh01vhGSCb34jzS%2Bh3/hudc6rL23j9i90fSNvGYRuzyeMr08lFMTPRvgkjxALbs9xdchPlcs2TvG1R%2B%2BANinvagGkDw5lg8%2BK6QEPTHQ4D1Pozg9bJhdPgqCCz581Z2952AfO7zCTj2LtS69EI16vcJBkLq4Tt09/6VGvdVbVj3C3Ri9ssKaPAGio71rIzk%2BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%3D%3D;1@vu9lADqlKr2uI0w9wf2OvcUHoD1e1YK9E2boPPKKq72VlQY%2BJ4sNPkrNLT2LJ8K9nAe6veacqr06W7w9eUE5PtnYC70vQL09O2mLvACOTz2/dAK9xYELvdhTyDtrEaU9nmr8vdfjWL2QGAG9%2B4IlvbOVZb0kPjq96%2Bk0PgYiCL0I9O%2B9u5suvV/SPzwOZkg%2BmEtlOmUThD27cfu7SOGcvVoISD36Eak9agG0PXIuJb5MSgC8CadKPnH3ibzOz/A9jYHJvfU%2BKT7Errk9r9u4PIYNxz17NIG9JRAwPcBVgr0lX409154rvT/tFrw4J1%2B%2BIOoRvlo5FL6gg6C9JXqzO4tNzT0uu1Y97aiovBz7Fj6CWUG79GmPPB5kxjxEklm9PyMdvphEvDsbiuE9D4zuvYk6jj2hdo48Pof/vLHFKT2T6%2B%2B9ejcWvYyT4LxvUg894MtIOsFcVL18ija9QUDYPOUi5j3qpae9R8RuvRygGDuXhWC98IQ4vnL09LwCUTi%2BKfmEOmjzor2AN9q9pXFRvNuAnjx4asU8tN8ZPSCjkzxivr09Ed8bPnCwYTzE3Ru%2B%2BYeuvflOcTwWNg8%2BiEYEPSyj2z1xpFg9Xe5aPnlrCj4tPpy9A7DKOhkJUj0pJi296e5%2BvYKzaLu8pNE9%2BkMwvX87YT3cCf%2B8X1SaPLUztb2uETk%2BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%3D%3D",
        "featureAmount": "2",
        "iff": "true",
        "threshold": "0.97",
        "sort": "score",
        "rows": "1000"
    }
    param = ''
    listResult = []
    source["feature"] = feature
    source["rows"] = rows
    for key in source.keys():
        param = param + key + "=" + source[key] + "&"
    # print(param)

    searchResult = get(param, ip, '/solr/intellifusion/topsearch?')
    # print(searchResult)
    # print(type(json.loads(searchResult)["docs"]))
    # 将返回结果中docs的值转化为列
    listDocs = json.loads(searchResult)["docs"]
    # 取列中的id和file存到新的列中
    for i in listDocs:
        listResult.append(dict(id=i["id"], file=i["file"]))
    return json.loads(searchResult)["result_count"], listResult

def compare(ip1, ip2, feature="0@vu9lAMejG70kH1U9i/6WvfUPoj3mjXa9ow7ePFVdpb2lBQY%2BcmcKPp/kGT273Li9Fm%2B/vYZ9p72ElbQ95N44Pp4B37yMK7w9zxdkvBOlOj10SBO9AinwvI3hwTvY2bM9yrPqvdREV73OAfG84xQive05fr3OMDa9zDU2Pp/CCr3sB/e9scQ6vRqR1jdI2kQ%2B0qwHPLsEkz0JL%2BK7QRCavQsmPz2LbKQ9n6SrPSDrIr7%2BxYW7XtJEPpZJVrzym%2B09Bba/vZGfJz6YOrE9qlvjPIrmzj0WOlu9jtktPVI1hL3kapE9opk9vThrGrwqxGO%2BBGoYvruzF77XIaS9zsjXOwld0T1xOFQ9HCHavC3sFj4W82m7b%2Bd3PLa4pjwxB0y9KMogvm3aKTzNNfQ9%2BUj2vSpwfz2VUHY8%2BfH0vKQ6RD09M%2Bu9MeIavTzL1rz3eQo9%2BS4NOxauYr2grkC9HzH1PB0T5T18wKS9th9RvWPjXDto9169Qh01vhGSCb34jzS%2Bh3/hudc6rL23j9i90fSNvGYRuzyeMr08lFMTPRvgkjxALbs9xdchPlcs2TvG1R%2B%2BANinvagGkDw5lg8%2BK6QEPTHQ4D1Pozg9bJhdPgqCCz581Z2952AfO7zCTj2LtS69EI16vcJBkLq4Tt09/6VGvdVbVj3C3Ri9ssKaPAGio71rIzk%2BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%3D%3D;1@vu9lADqlKr2uI0w9wf2OvcUHoD1e1YK9E2boPPKKq72VlQY%2BJ4sNPkrNLT2LJ8K9nAe6veacqr06W7w9eUE5PtnYC70vQL09O2mLvACOTz2/dAK9xYELvdhTyDtrEaU9nmr8vdfjWL2QGAG9%2B4IlvbOVZb0kPjq96%2Bk0PgYiCL0I9O%2B9u5suvV/SPzwOZkg%2BmEtlOmUThD27cfu7SOGcvVoISD36Eak9agG0PXIuJb5MSgC8CadKPnH3ibzOz/A9jYHJvfU%2BKT7Errk9r9u4PIYNxz17NIG9JRAwPcBVgr0lX409154rvT/tFrw4J1%2B%2BIOoRvlo5FL6gg6C9JXqzO4tNzT0uu1Y97aiovBz7Fj6CWUG79GmPPB5kxjxEklm9PyMdvphEvDsbiuE9D4zuvYk6jj2hdo48Pof/vLHFKT2T6%2B%2B9ejcWvYyT4LxvUg894MtIOsFcVL18ija9QUDYPOUi5j3qpae9R8RuvRygGDuXhWC98IQ4vnL09LwCUTi%2BKfmEOmjzor2AN9q9pXFRvNuAnjx4asU8tN8ZPSCjkzxivr09Ed8bPnCwYTzE3Ru%2B%2BYeuvflOcTwWNg8%2BiEYEPSyj2z1xpFg9Xe5aPnlrCj4tPpy9A7DKOhkJUj0pJi296e5%2BvYKzaLu8pNE9%2BkMwvX87YT3cCf%2B8X1SaPLUztb2uETk%2BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%3D%3D"):
    count1, listResult1 = search(ip=ip1, feature=feature)
    for i in listResult1:
        print(i)
    print(count1)

    # ANN solr
    count2, listResult2 = search(ip=ip2, feature=feature)
    for i in listResult2:
        print(i)
    print(count2)
    if count1 > count2:
        col5 = count1 - count2
        col6 = False
    else:
        col5 = False
        col6 = count2 - count1

    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    result = os.path.join(current_dir, 'result.txt')
    with open(result, 'a') as f:
        f.write(str(listResult1) + "," + str(listResult2) + "---" + str(count1) + "," + str(count2) + "," + str(
            col5) + "," + str(col6) + "\n")

if __name__ == '__main__':
    listFeatures = DbData(ip='192.168.2.27').query(t_name='t_face_1', count=100)
    # print(listFeatures[0])
    # normal solr
