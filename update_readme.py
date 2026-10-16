import requests
import time
import re

def main():
    api_url = "https://meme-api.com/gimme/ProgrammerHumor"
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            image_url = data.get("url")
            meme_title = data.get("title", "Dev Meme")
            
            print(f"Lấy link dev meme thành công: {image_url}")
            
            # Tải ảnh về lưu đè vào file meme.png
            img_data = requests.get(image_url, timeout=15).content
            with open("meme.png", "wb") as handler:
                handler.write(img_data)
                
            # Đọc README.md và cập nhật link ảnh kèm timestamp để phá cache GitHub
            with open("README.md", "r", encoding="utf-8") as f:
                content = f.read()
            
            timestamp = int(time.time())
            new_img_tag = f'<img src="./meme.png?v={timestamp}" alt="{meme_title}" width="500" style="border-radius: 8px;" />'
            
            # Thay thế thẻ img bên trong phần meme
            pattern = r"(<!--START_SECTION:meme-->)(.*?)(<!--END_SECTION:meme-->)"
            new_content = re.sub(pattern, f"\\1\n  {new_img_tag}\n  \\3", content, flags=re.DOTALL)
            
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_content)
                
            print("Đã tải meme mới và cập nhật cache timestamp thành công!")
        else:
            print(f"Lỗi khi gọi API, mã lỗi: {response.status_code}")
    except Exception as e:
        print(f"Xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
