import os

if os.path.exists('index.html') or os.path.exists('style.css') or os.path.exists('main.js'):
    print("Error: Project already initialized")
    exit(1)

html = open("index.html", "w")
html.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css" type="text/css">
    <title>Document</title>
</head>
<body>
    
</body>
<script src="main.js"></script>
</html>
''')
html.close()

css = open("style.css", "w")
css.write(''':root {
    
}

body {
    margin: 0;
}

button, input[type="reset"], input[type="submit"], .button {

}

button:hover, input[type="reset"]:hover, input[type="submit"]:hover, .button:hover {
    
}

a {

}

header {

}

footer {
    
}
''')


open("main.js", "w").close()
