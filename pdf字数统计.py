import pdfplumber
import re


def count_pdf_words(file_path):
    total_text = ""

    # 读取 PDF
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                total_text += text + "\n"

    # 中文字符数
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', total_text)
    chinese_count = len(chinese_chars)

    # 英文单词数
    words = re.findall(r'\b[a-zA-Z]+\b', total_text)
    word_count = len(words)

    # 总字符数（去掉空白）
    total_chars = len(re.sub(r'\s', '', total_text))

    print("===== 统计结果 =====")
    print(f"总字符数（不含空格）: {total_chars}")
    print(f"中文字符数: {chinese_count}")
    print(f"英文单词数: {word_count}")


if __name__ == "__main__":
    file_path = r"D:\Study\VSCode_Project\GZHU_TeX_Master_Template_1.5.0\樊如斌硕士论文.pdf"  # ← 改这里
    count_pdf_words(file_path)