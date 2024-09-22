import csv
import os


# Folder where the CSV files are stored  
folder_path = "meets"
output_file = "deliv2.html"


# Initialize a string for the rows of the table
table_rows = ""


# Read all CSV files
for csv_filename in os.listdir(folder_path):
    if csv_filename.endswith(".csv"):
        csv_file_path = os.path.join(folder_path, csv_filename)
       
        with open(csv_file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)


            # Extract meet details
            meet_name = data[0][0]  
            meet_date = data[1][0]  
            race_comment = data[3][0]  


            # Searching for "Ann Arbor Skyline" cell to extract team place
            team_place = None
            for row in data:
                if "Ann Arbor Skyline" in row:
                    team_place = row[row.index("Ann Arbor Skyline") - 1]
                    break


            # Adding rows to the table
            table_rows += f'''
            <tr>
                <td>{meet_name}</td>
                <td>{meet_date}</td>
                <td>{team_place}</td>
                <td>{race_comment}</td>
            </tr>
            '''


# HTML template WITH Table
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <title>Meets</title>
    /* <style>
         table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            }
    </style> */
</head>
<body>
    <header>
        <h1>Meet Results</h1>
    </header>
   
    <table>
        <tr>
            <th>Meet Name</th>
            <th>Meet Date</th>
            <th>Team Place</th>
            <th>Coach's Comments</th>
        </tr>
        {table_rows}
    </table>
</body>
</html>
'''


# Replacing the placeholder for real table rows
html_content = html_template.format(table_rows=table_rows)


# Output file
output_file_path = os.path.join(".", output_file)  # Save in the current directory


# Opening HTML file content
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(html_content)



