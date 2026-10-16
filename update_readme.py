import requests
import re

def main():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            meme_url = data.get("url")
            meme_title = data.get("title", "Dev Meme")
            
            with open("README.md", "r", encoding="utf-8") as f:
                content = f.read()
            
            new_meme_html = f'<img src="{meme_url}" alt="{meme_title}" width="500" style="border-radius: 8px;" />'
            
            pattern = r"(<!--START_SECTION:meme-->)(.*?)(<!--END_SECTION:meme-->)"
            new_content = re.sub(pattern, f"\\1\n  {new_meme_html}\n  \\3", content, flags=re.DOTALL)
            
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Đã cập nhật meme thành công!")
        else:
            print("Không thể gọi API, mã lỗi:", response.status_code)
    except Exception as e:
        print("Lỗi xảy ra:", e)

if __name__ == "__main__":
    main()
