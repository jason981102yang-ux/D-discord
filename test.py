
import re

pattern = r"(繪名名|～|啦|欸|耶|好棒|超|♡|✨|💕|:-D|\^_\^|:\)|：\)|XD|>_<|T_T|QAQ|orz)"
text = "今天好開心 QAQ"

if re.search(pattern, text):
    print("Matched style: mizuki")