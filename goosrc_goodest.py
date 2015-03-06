import sys, os, time
import mongoengine as meng
# PYBASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../science") ) 
# sys.path.append(PYBASE)

#
# in real-world app, we would import our source and destination collections
#
class goosrc(meng.Document):
    num = meng.IntField(primary_key = True)

class goodest(meng.Document):
    numnum = meng.StringField()

#
# source field to use for partitioning (must be unique and orderable)
#
KEY = 'num'

#
# optional query:
#
QUERY = {'num__ne': 9}

#
# called on initialization of processing (incremental)
#
# def init():
#     pass

#
# called on full reset
#
# def reset():
#     pass

#
# called for each chunk (concurrent)
# source is mongoengine cursor; dest is mongoengine object class
# both are associated with db connections
#
def process(source, dest):
    print "  process %d from" % source.count(), source._collection, "to", dest.objects._collection
    for x in source:
        if x.num != 15:
            print "    goosrc_goodest.process:", x.num
            d = dest()
            d.numnum = str(x.num*2)
            d.save()
        else:
            print "    goosrc_goodest: skipping", x.num