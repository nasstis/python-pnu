import cgi
import html
import os
import http.cookies

form = cgi.FieldStorage()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
counter = int(cookie.get("counter", 0).value) if cookie.get("counter") else 0

counter += 1

cookie["counter"] = str(counter)
print(f"Set-Cookie: counter={counter}; Path=/")

name = form.getvalue("name")
age = form.getvalue("age")
name = html.escape(name)
age = html.escape(age)

sex = form.getvalue("sex", default = "стать не вибрано")

colors = ["red", "green", "blue", "yellow", "another"]
colors_checkbox = {}
for color in colors:
    value_choice = form.getvalue(color)
    if value_choice is not None:
        colors_checkbox[color] = value_choice
colors_text = ', '.join(colors_checkbox)
if not colors_checkbox:
    colors_text = "не обрано жодного кольору"

template_html = f"""
<!DOCTYPE html>
<html lang="eu">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обробка форми</title>
</head>
<body>
    <h3>Привіт, {name}</h3>
    <h3>Ви вибрали, що ваш вік: {age}</h3>
    <h3>Ваша стать: {sex} </h3>
    <h3>Ваші улюблені кольори: {colors_text} </h3>
    <h3>Кількість заповнених форм: {counter}</h3>
    <form action="/cgi-bin/clear_cookies.py" method="post">
        <input type="submit" value="Видалити всі cookies">
    </form>
</body>
</html>
"""

print(template_html)