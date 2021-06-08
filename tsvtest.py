import gluonnlp.data as data
import os
from gluonnlp.base import get_home_dir
from .csdata import WeiboData
print(os.path.abspath(os.path.dirname(__file__)))
dirr=os.path.abspath(os.path.dirname(__file__))+'/data/weibo_3/test_weibo_3.tsv'
dataset = WeiboData('train')

print(len(dataset))
