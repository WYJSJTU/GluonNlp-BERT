import gluonnlp
_, vocab = gluonnlp.model.bert_12_768_12(dataset_name='book_corpus_wiki_en_uncased',
                                         pretrained=False, root='./model')
tokenizer = gluonnlp.data.BERTTokenizer(vocab=vocab)
print(vocab.cls_token,vocab.sep_token)
sst2 = gluonnlp.data.SST_2('test')
print(tokenizer(sst2[0][0]))

   