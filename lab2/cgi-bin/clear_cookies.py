import http.cookies

cookie = http.cookies.SimpleCookie()
cookie["counter"] = "0"

print(f"Set-Cookie: {cookie.output()}; Path=/")

template_html = f"""
<!DOCTYPE html>
<html lang="eu">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Видалити cookies</title>
</head>
<body>
    <h3>Усі cookies успішно видалено, можете повертатися до головної сторінки!</h3>
</body>
</html>
"""

print(template_html)