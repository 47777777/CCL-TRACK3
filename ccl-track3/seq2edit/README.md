### 代码结构
```
├── command
│   └── train.sh       # 训练脚本
├── data
├── logs
├── pretrained_model
└── src
    ├── __init__.py
    ├── baseline       # baseline系统
    ├── corrector.py   # 文本校对入口
    ├── evaluate.py    # 指标评估
    ├── metric.py      # 指标计算文件 
    ├── prepare_for_upload.py  # 生成要提交的结果文件
    └── train.py       # 训练入口
```


### 训练

```
CUDA_VISIBLE_DEVICES=0,1,2,3 python -m src.train \
--in_model_dir "pretrained_model/chinese-roberta-wwm-ext" \
--out_model_dir "model/ctc_train" \
--epochs "50" \
--batch_size "158" \
--max_seq_len "128" \
--learning_rate "5e-5" \
--train_fp "data/comp_data/preliminary_a_data/preliminary_train.json" \
--test_fp "data/comp_data/preliminary_a_data/preliminary_val.json" \
--random_seed_num "42" \
--check_val_every_n_epoch "0.5" \
--early_stop_times "20" \
--warmup_steps "-1" \
--dev_data_ratio "0.01" \
--training_mode "ddp" \
--amp true \
--freeze_embedding false
```

- 其中所用的预训练为:[chinese-roberta-wwm-ext](https://huggingface.co/hfl/chinese-roberta-wwm-ext)
- 若使用Macbert可能会有进一步的提升


### 开始训练

```
cd command && sh train.sh
```
