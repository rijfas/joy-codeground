from joy import SVG, Rectangle, Line, Point

def render(*shapes, output_file_name='index.html'):
    """Renders given `*shapes` as html to the file `output_file_name` 
    """
    markers = [
        Rectangle(width=300, height=300, stroke="#ddd"),
        Line(start=Point(x=-150, y=0), end=Point(x=150, y=0), stroke="#ddd"),
        Line(start=Point(x=0, y=-150), end=Point(x=0, y=150), stroke="#ddd")
    ]
    shapes = markers + list(shapes)
    data = SVG(shapes)
    generate_html = lambda svg : f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Jow OutPut</title>
    </head>
    <body>
        {svg}
    </body>
    </html>
    '''
    with open(output_file_name, 'w') as outputFile:
        outputFile.write(generate_html(data))