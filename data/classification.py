# Copyright 2018 The Google AI Language Team Authors and DMLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""BERT classification/regression datasets."""


__all__ = [
    'MRPCTask', 'QQPTask', 'QNLITask', 'RTETask', 'STSBTask',
    'CoLATask', 'MNLITask', 'WNLITask', 'SSTTask', 'XNLITask','Weibo3Task','WaimaiTask','StockTask','MeituanTask','MovieTask'
]

from mxnet.metric import Accuracy, F1, MCC, PearsonCorrelation, CompositeEvalMetric
from gluonnlp.data import GlueCoLA, GlueSST2, GlueSTSB, GlueMRPC
from gluonnlp.data import GlueQQP, GlueRTE, GlueMNLI, GlueQNLI, GlueWNLI
try:
    from .baidu_ernie_data import BaiduErnieXNLI, BaiduErnieLCQMC, BaiduErnieChnSentiCorp
except ImportError:
    from baidu_ernie_data import BaiduErnieXNLI, BaiduErnieLCQMC, BaiduErnieChnSentiCorp
from .csdata import WeiboData,WaimaiData,StockData,MeituanData,MovieData

class GlueTask:
    """Abstract GLUE task class.

    Parameters
    ----------
    class_labels : list of str, or None
        Classification labels of the task.
        Set to None for regression tasks with continuous real values.
    metrics : list of EValMetric
        Evaluation metrics of the task.
    is_pair : bool
        Whether the task deals with sentence pairs or single sentences.
    label_alias : dict
        label alias dict, some different labels in dataset actually means
        the same. e.g.: {'contradictory':'contradiction'} means contradictory
        and contradiction label means the same in dataset, they will get
        the same class id.
    """
    def __init__(self, class_labels, metrics, is_pair, label_alias=None):
        self.class_labels = class_labels
        self.metrics = metrics
        self.is_pair = is_pair
        self.label_alias = label_alias

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for the task.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments.

        Returns
        -------
        TSVDataset : the dataset of target segment.
        """
        raise NotImplementedError()

    def dataset_train(self):
        """Get the training segment of the dataset for the task.

        Returns
        -------
        tuple of str, TSVDataset : the segment name, and the dataset.
        """
        return 'train', self.get_dataset(segment='train')

    def dataset_dev(self):
        """Get the dev segment of the dataset for the task.

        Returns
        -------
        tuple of (str, TSVDataset), or list of tuple : the segment name, and the dataset.
        """
        return 'dev', self.get_dataset(segment='dev')

    def dataset_test(self):
        """Get the test segment of the dataset for the task.

        Returns
        -------
        tuple of (str, TSVDataset), or list of tuple : the segment name, and the dataset.
        """
        return 'test', self.get_dataset(segment='test')

class MRPCTask(GlueTask):
    """The MRPC task on GlueBenchmark."""
    def __init__(self):
        is_pair = True
        class_labels = ['0', '1']
        metric = CompositeEvalMetric()
        metric.add(Accuracy())
        metric.add(F1(average='micro'))
        super(MRPCTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for MRPC.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'train', 'dev', 'test'.
        """
        return GlueMRPC(segment=segment)

class QQPTask(GlueTask):
    """The Quora Question Pairs task on GlueBenchmark."""
    def __init__(self):
        is_pair = True
        class_labels = ['0', '1']
        metric = CompositeEvalMetric()
        metric.add(Accuracy())
        metric.add(F1(average='micro'))
        super(QQPTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for QQP.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'train', 'dev', 'test'.
        """
        return GlueQQP(segment=segment)


class RTETask(GlueTask):
    """The Recognizing Textual Entailment task on GlueBenchmark."""
    def __init__(self):
        is_pair = True
        class_labels = ['not_entailment', 'entailment']
        metric = Accuracy()
        super(RTETask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for RTE.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'train', 'dev', 'test'.
        """
        return GlueRTE(segment=segment)

class QNLITask(GlueTask):
    """The SQuAD NLI task on GlueBenchmark."""
    def __init__(self):
        is_pair = True
        class_labels = ['not_entailment', 'entailment']
        metric = Accuracy()
        super(QNLITask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for QNLI.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'train', 'dev', 'test'.
        """
        return GlueQNLI(segment=segment)

class STSBTask(GlueTask):
    """The Sentence Textual Similarity Benchmark task on GlueBenchmark."""
    def __init__(self):
        is_pair = True
        class_labels = None
        metric = PearsonCorrelation(average='micro')
        super(STSBTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for STSB

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'train', 'dev', 'test'.
        """
        return GlueSTSB(segment=segment)

class CoLATask(GlueTask):
    """The Warstdadt acceptability task on GlueBenchmark."""
    def __init__(self):
        is_pair = False
        class_labels = ['0', '1']
        metric = MCC(average='micro')
        super(CoLATask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for CoLA

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'train', 'dev', 'test'.
        """
        return GlueCoLA(segment=segment)

class SSTTask(GlueTask):
    """The Stanford Sentiment Treebank task on GlueBenchmark."""
    def __init__(self):
        is_pair = False
        class_labels = ['0', '1']
        metric = Accuracy()
        super(SSTTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for SST

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'train', 'dev', 'test'.
        """
        return GlueSST2(segment=segment)

class WNLITask(GlueTask):
    """The Winograd NLI task on GlueBenchmark."""
    def __init__(self):
        is_pair = True
        class_labels = ['0', '1']
        metric = Accuracy()
        super(WNLITask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for WNLI

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev', 'test', 'train'
        """
        return GlueWNLI(segment=segment)

class MNLITask(GlueTask):
    """The Multi-Genre Natural Language Inference task on GlueBenchmark."""
    def __init__(self):
        is_pair = True
        class_labels = ['neutral', 'entailment', 'contradiction']
        metric = Accuracy()
        super(MNLITask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for MNLI

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev_matched', 'dev_mismatched', 'test_matched',
            'test_mismatched', 'train'
        """
        return GlueMNLI(segment=segment)

    def dataset_dev(self):
        """Get the dev segment of the dataset for the task.

        Returns
        -------
        list of TSVDataset : the dataset of the dev segment.
        """
        return [('dev_matched', self.get_dataset(segment='dev_matched')),
                ('dev_mismatched', self.get_dataset(segment='dev_mismatched'))]

    def dataset_test(self):
        """Get the test segment of the dataset for the task.

        Returns
        -------
        list of TSVDataset : the dataset of the test segment.
        """
        return [('test_matched', self.get_dataset(segment='test_matched')),
                ('test_mismatched', self.get_dataset(segment='test_mismatched'))]

class XNLITask(GlueTask):
    """The XNLI task using the dataset released from Baidu

    <https://github.com/PaddlePaddle/LARK/tree/develop/ERNIE>.

    """
    def __init__(self):
        is_pair = True
        class_labels = ['neutral', 'entailment', 'contradiction']
        metric = Accuracy()
        super(XNLITask, self).__init__(class_labels, metric, is_pair,
                                       label_alias={'contradictory':'contradiction'})

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for XNLI.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev', 'test', 'train'
        """
        return BaiduErnieXNLI(segment)

class LCQMCTask(GlueTask):
    """The LCQMC task using the dataset released from Baidu

    <https://github.com/PaddlePaddle/LARK/tree/develop/ERNIE>.

    """
    def __init__(self):
        is_pair = True
        class_labels = ['0', '1']
        metric = Accuracy()
        super(LCQMCTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for LCQMC.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev', 'test', 'train'
        """
        return BaiduErnieLCQMC(segment)

class ChnSentiCorpTask(GlueTask):
    """The ChnSentiCorp task using the dataset released from Baidu

    <https://github.com/PaddlePaddle/LARK/tree/develop/ERNIE>.

    """
    def __init__(self):
        is_pair = False
        class_labels = ['0', '1']
        metric = Accuracy()
        super(ChnSentiCorpTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for ChnSentiCorp.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev', 'test', 'train'
        """
        return BaiduErnieChnSentiCorp(segment)

class Weibo3Task(GlueTask):
    """The Chinese sentiment analysis task
       Weibo2     4 classes
    """
    def __init__(self):
        is_pair = False
        class_labels = ['0', '1', '2']
        metric = Accuracy()
        super(Weibo3Task, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for CNSA.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev', 'test', 'train'
        """
        return WeiboData(segment)
class WaimaiTask(GlueTask):
    """The Chinese sentiment analysis task
       Weibo2     4 classes
    """
    def __init__(self):
        is_pair = False
        class_labels = ['0', '1']
        metric = Accuracy()
        super(WaimaiTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for CNSA.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev', 'test', 'train'
        """
        return WaimaiData(segment)

class StockTask(GlueTask):
    """The Chinese sentiment analysis task
       Weibo2     4 classes
    """
    def __init__(self):
        is_pair = False
        class_labels = ['0', '1','2']
        metric = Accuracy()
        super(StockTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for CNSA.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev', 'test', 'train'
        """
        return StockData(segment)

class MeituanTask(GlueTask):
    """The Chinese sentiment analysis task
       Weibo2     4 classes
    """
    def __init__(self):
        is_pair = False
        class_labels = ['0','1','2','3','4']
        metric = Accuracy()
        super(MeituanTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for CNSA.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev', 'test', 'train'
        """
        return MeituanData(segment)



    class MovieTask(GlueTask):
    """The Chinese sentiment analysis task
       Movie     2 classes
    """
    def __init__(self):
        is_pair = False
        class_labels = ['0', '1']
        metric = Accuracy()
        super(MovieTask, self).__init__(class_labels, metric, is_pair)

    def get_dataset(self, segment='train'):
        """Get the corresponding dataset for CNSA.

        Parameters
        ----------
        segment : str, default 'train'
            Dataset segments. Options are 'dev', 'test', 'train'
        """
        return MovieData(segment)