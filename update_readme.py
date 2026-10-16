import requests

def main():
    api_url = "https://meme-api.com/gimme/ProgrammerHumor"
    try:
        # Gọi API lấy JSON meme từ Reddit
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            image_url = data.get("url")
            
            print(f"Lấy link meme thành công: {image_url}")
            
            # Tải trực tiếp file ảnh về và lưu thành file 'meme.png' trong repo
            img_data = requests.get(image_url, timeout=15).content
            with open("meme.png", "wb") as handler:
                handler.write(img_data)
                
            print("Đã tải và lưu meme thành công vào file meme.png!")
        else:
            print(f"Lỗi khi gọi API, mã lỗi: {response.status_code}")
    except Exception as e:
        print(f"Xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
