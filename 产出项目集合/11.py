# 安装必要的库
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments

# 设置国内镜像
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# 数据准备
# 创建数据集
data = {
    'text': [
        "This movie is absolutely fantastic! I loved every minute of it.",
        "Terrible movie, waste of time. Poor acting and weak plot.",
        "It was okay, not great but not bad either.",
        "One of the best films I've seen this year. Highly recommended!",
        "Disappointing. Expected much more from this director.",
        "A masterpiece of cinema. Brilliant performances all around.",
        "Boring and predictable. Fell asleep halfway through.",
        "Interesting concept but poor execution.",
        "Heartwarming story with great character development.",
        "Confusing plot with too many unnecessary subplots."
    ],
    'label': [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # 1=正面, 0=负面
}

# 创建DataFrame
df = pd.DataFrame(data)

# 划分训练集和验证集
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df['text'], df['label'], test_size=0.2, random_state=42
)

# 打印数据集大小
print("训练集大小:", len(train_texts))
print("验证集大小:", len(val_texts))

# 加载预训练模型和分词器
model_name = "bert-base-uncased"

try:
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)
    print("成功加载BERT模型")
except Exception as e:
    print(f"加载BERT模型失败: {e}")
    print("请检查网络连接或使用国内镜像")
    exit()

# 数据预处理
# 对训练集文本进行分词和编码
train_encodings = tokenizer(
    train_texts.tolist(),
    truncation=True,
    padding=True,
    max_length=128,
    return_tensors="pt"
)

# 对验证集文本进行分词和编码
val_encodings = tokenizer(
    val_texts.tolist(),
    truncation=True,
    padding=True,
    max_length=128,
    return_tensors="pt"
)


# 创建自定义PyTorch数据集类
class ReviewDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels.iloc[idx])
        return item

    def __len__(self):
        return len(self.labels)


# 创建训练和验证数据集实例
train_dataset = ReviewDataset(train_encodings, train_labels)
val_dataset = ReviewDataset(val_encodings, val_labels)

# 设置训练参数
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=16,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    eval_strategy="epoch",  # 修正参数名
)

# 创建Trainer实例
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

# 开始训练
print("开始训练...")
trainer.train()
print("训练完成!")


# 定义预测函数
def predict(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    model.eval()

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1)
    predicted_class_id = torch.argmax(probabilities, dim=1).item()

    return predicted_class_id, probabilities[0].tolist()


# 测试预测
test_texts = [
    "This movie is great!",
    "I didn't like this film at all.",
    "It was an average movie, nothing special."
]

print("\n测试预测结果:")
for text in test_texts:
    pred, probs = predict(text)
    sentiment = "正面" if pred == 1 else "负面"
    print(f"文本: {text}")
    print(f"情感: {sentiment} (置信度: {max(probs):.4f})")
    print(f"负面概率: {probs[0]:.4f}, 正面概率: {probs[1]:.4f}")
    print("-" * 50)

# 保存模型和分词器
model.save_pretrained("./my_sentiment_model")
tokenizer.save_pretrained("./my_sentiment_model")
print("模型已保存到 ./my_sentiment_model 目录")

# 验证加载功能
try:
    loaded_model = BertForSequenceClassification.from_pretrained("./my_sentiment_model")
    loaded_tokenizer = BertTokenizer.from_pretrained("./my_sentiment_model")
    print("模型加载成功!")
except Exception as e:
    print(f"模型加载失败: {e}")