
import os
import tarfile
from urllib.request import urlretrieve

from gluonnlp.base import get_home_dir
from gluonnlp.data.dataset import TSVDataset
from gluonnlp.data.registry import register





class _WeiboDataset(TSVDataset):
    def __init__(self, root, dataset_name, segment, **kwargs):
        self._root = root
        filename = os.path.join(self._root, dataset_name, '%s_weibo_3.tsv' % segment)
        super(_WeiboDataset, self).__init__(filename, **kwargs)


@register(segment=['train', 'dev', 'test'])
class WeiboData(_WeiboDataset):

    def __init__(self, segment='train',
                 root=os.path.join(os.path.dirname(os.path.abspath(__file__))),
                 return_all_fields=False):
        A_IDX, LABEL_IDX = 1, 0
        if segment in ['train', 'dev']:
            field_indices = [A_IDX, LABEL_IDX] if not return_all_fields else None
            num_discard_samples = 1
        elif segment == 'test':
            field_indices = [A_IDX] if not return_all_fields else None
            num_discard_samples = 1

        super(WeiboData, self).__init__(root, 'weibo_3', segment,
                                             num_discard_samples=num_discard_samples,
                                             field_indices=field_indices)

class _WaimaiDataset(TSVDataset):
    def __init__(self, root, dataset_name, segment, **kwargs):
        self._root = root
        filename = os.path.join(self._root, dataset_name, '%s_waimai.tsv' % segment)
        super(_WaimaiDataset, self).__init__(filename, **kwargs)


@register(segment=['train', 'dev', 'test'])
class WaimaiData(_WaimaiDataset):

    def __init__(self, segment='train',
                 root=os.path.join(os.path.dirname(os.path.abspath(__file__))),
                 return_all_fields=False):
        A_IDX, LABEL_IDX = 1, 0
        if segment in ['train', 'dev']:
            field_indices = [A_IDX, LABEL_IDX] if not return_all_fields else None
            num_discard_samples = 1
        elif segment == 'test':
            field_indices = [A_IDX] if not return_all_fields else None
            num_discard_samples = 1

        super(WaimaiData, self).__init__(root, 'waimai', segment,
                                             num_discard_samples=num_discard_samples,
                                             field_indices=field_indices)


class _StockDataset(TSVDataset):
    def __init__(self, root, dataset_name, segment, **kwargs):
        self._root = root
        filename = os.path.join(self._root, dataset_name, '%s_stock.tsv' % segment)
        super(_StockDataset, self).__init__(filename, **kwargs)


@register(segment=['train', 'dev', 'test'])
class StockData(_StockDataset):

    def __init__(self, segment='train',
                 root=os.path.join(os.path.dirname(os.path.abspath(__file__))),
                 return_all_fields=False):
        A_IDX, LABEL_IDX = 0, 1
        if segment in ['train', 'dev']:
            field_indices = [A_IDX, LABEL_IDX] if not return_all_fields else None
            num_discard_samples = 1
        elif segment == 'test':
            field_indices = [A_IDX] if not return_all_fields else None
            num_discard_samples = 1

        super(StockData, self).__init__(root, 'stock', segment,
                                             num_discard_samples=num_discard_samples,
                                             field_indices=field_indices)
                                
class _MeituanDataset(TSVDataset):
    def __init__(self, root, dataset_name, segment, **kwargs):
        self._root = root
        filename = os.path.join(self._root, dataset_name, '%s_meituan.tsv' % segment)
        super(_MeituanDataset, self).__init__(filename, **kwargs)


@register(segment=['train', 'dev', 'test'])
class MeituanData(_MeituanDataset):

    def __init__(self, segment='train',
                 root=os.path.join(os.path.dirname(os.path.abspath(__file__))),
                 return_all_fields=False):
        A_IDX, LABEL_IDX = 0, 1
        if segment in ['train', 'dev']:
            field_indices = [A_IDX, LABEL_IDX] if not return_all_fields else None
            num_discard_samples = 1
        elif segment == 'test':
            field_indices = [A_IDX] if not return_all_fields else None
            num_discard_samples = 1

        super(MeituanData, self).__init__(root, 'meituan', segment,
                                             num_discard_samples=num_discard_samples,
                                             field_indices=field_indices)