import os
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
from whoosh.qparser import QueryParser


def createIndex():
    # 创建schema, stored为True表示能够被检索
    schema = Schema(title=TEXT(stored=True),
                    path=ID(stored=True),
                    content=TEXT(stored=True)
                    )
    # 存储schema信息至indexdir目录
    indexdir = '/Users/andrew_asa/Documents/code/github/andrew-asa/exec/python/out'
    if not os.path.exists(indexdir):
        os.mkdir(indexdir)
    ix = create_in(indexdir, schema)
    return ix
def createDocumtent(ix):
    writer = ix.writer()
    writer.add_document(title=u"my document", content=u"this is my document", path=u"/a" )
    writer.add_document(title=u"my second document", content=u"this is my second document", path=u"/b")
    writer.commit()
def doSearch(ix):
    searcher = ix.searcher()
    try:
        searcher = ix.searcher()
        query = QueryParser("content", ix.schema).parse("second")
        result = searcher.search(query)
        return result[0]
    finally:
        searcher.close()
if __name__ == "__main__":
    ix = createIndex()
    createDocumtent(ix)
    result = doSearch(ix)
    print(result)