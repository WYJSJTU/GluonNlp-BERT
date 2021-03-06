# GluonNLP-BERT
Sentiment Analysis on Chinese and English Datasets based on GluonNlp BERT model
## Requirements
* Python 3.7
* CUDA 10.2
* Cudatoolkit 10.2.89
* MXNet mxnet-cu102-1.7.0.post1
* GluonNLP 0.9.2

## Datasets
* **waimai_10k**: Chinese cutomer review on takeaway app with sentiment annotation of positive and negetive, 2 categories classification task.
* **simplifyweibo_4_moods**: Chinese users posts on Sina Weibo with sentiment annotation of joy, angry and disgust，3 categories classification task.
* **Meituan ASAP**: Chinese restaurant review with star annotation from 1 to 5, 5 categories classification task.
* **Movie comment_50k**: English polar movie review with sentiment annotation of positive and negetive, 2 categories classification task.
## Data Preperation
Please download datasets from this link:
Link：https://pan.baidu.com/s/1dRe7gwVvZxwBlJloO4ExfA 
Password：y5d3 

And place the folders to the ./data directory

## Training and Testing
```shell
python3 finetune_classifier.py --gpu 4 --task_name ${TASK} --batch_size 8 --seed 0 --lr 2e-5 --warmup_ratio 0.1 --epochs 5 --log_interval 100 --accumulate 4
```
Task names:

* **waimai_10k**: waimai
* **simplifyweibo_4_moods**: weibo3
* **Meituan ASAP**: meituan
* **Movie comment_50k**: movie

