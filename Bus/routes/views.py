<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bus Info</title>
</head>
<body>
    <table style="color:blue;">
        <thead >
            <tr>
                <td>Bus_num</td><td>route</td><td>Fees</td>
            </tr>
        </thead>
        <tbody>
        {% for bus in buses %}
        <tr>
            <td>{{ bus.Bus_num }}</td><td>{{ bus.route }}</td><td>{{ bus.fees }}</td>
        </tr>
        {% endfor %}
        </tbody>
    </table> 
    
</body>
</html>