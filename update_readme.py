import requests

def main():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            meme_url = data.get("url")
            meme_title = data.get("title", "Dev Meme")
            
            print(f"Lấy thành công meme URL: {meme_url}")
            
            # Đọc nội dung README.md
            with open("README.md", "r", encoding="utf-8") as f:
                content = f.read()
            
            # Chuẩn hóa xuống dòng
            content = content.replace("\r\n", "\n")
            
            start_marker = "<!--START_SECTION:meme-->"
            end_marker = "<!--END_SECTION:meme-->"
            
            if start_marker not in content or end_marker not in content:
                print("Lỗi: Không tìm thấy cặp thẻ comment meme trong README.md!")
                return
            
            # Tạo đoạn HTML ảnh meme mới
            new_meme_html = f'\n  <img src="{meme_url}" alt="{meme_title}" width="500" style="border-radius: 8px;" />\n  '
            
            # Cắt và ghép chuỗi thay thế chính xác giữa 2 mốc marker
            start_idx = content.find(start_marker) + len(start_marker)
            end_idx = content.find(end_marker)
            
            new_content = content[:start_idx] + new_meme_html + content[end_idx:]
            
            # Ghi đè file README.md
            with open("README.md", "w", encoding="utf-8", newline="\n") as f:
                f.write(new_content)
                
            print("Đã cập nhật meme vào README.md thành công!")
        else:
            print("Không thể gọi API, mã lỗi:", response.status_code)
    except Exception as e:
        print("Lỗi xảy ra:", e)

if __name__ == "__main__":
    main()
