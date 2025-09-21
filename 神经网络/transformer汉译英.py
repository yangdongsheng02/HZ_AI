from transformers import AutoModelWithLMHead,AutoTokenizer,pipelines

#指定模型
model_name = 'liam168/trans-opus-mt-zh-en'
#加载机器翻译模型
model = AutoModelWithLMHead.from_pretrained(model_name)
#加载词嵌入模型
tokenizer = AutoTokenizer.from_pretrained(model_name)
#使用pipelines来做处理,指定translation_zh_to_en来做机器翻译,tokenizer词嵌入
translate = pipelines('translation_zh_to_en',model=model,tokenizer=tokenizer)

print(translate('我是一个学生'))