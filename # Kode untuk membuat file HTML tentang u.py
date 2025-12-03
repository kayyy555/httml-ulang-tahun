# Kode untuk membuat file HTML tentang ulang tahun
# Konten HTML sebagai string
html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selamat Ulang Tahun!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f8ff;
            color: #333;
        }
        h1 {
            color: #ff69b4;
        }
        img {
            max-width: 300px;
            height: auto;
            border-radius: 10px;
        }
        p {
            font-size: 18px;
        }
</style>
</head>
<body>
    <h1>Selamat Ulang Tahun!</h1>
    <img src="https://example.com/birthday-cake.jpg" alt="Kue Ulang Tahun" />  <!-- Ganti URL dengan gambar ulang tahun Anda -->
    <p>Semoga hari ulang tahunmu penuh kebahagiaan, kesehatan, dan kesuksesan!</p>
    <p>Dari: [Noah]</p>
</body>
</html>
"""
# Menulis konten ke file HTML
with open("ulang_tahun.html", "w", encoding="utf-8") as file:
    file.write(html_content)
print("File HTML 'ulang_tahun.html' telah dibuat! Buka di browser untuk melihatnya.")
