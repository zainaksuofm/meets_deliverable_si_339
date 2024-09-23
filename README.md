Explanation of Code:
This Python script processes multiple CSV files from a folder named "meets" and generates an HTML file (deliv2.html) that displays the meet content (meet name, meet date, team ranking, and coaches comments) in a table format. 

The script first reads in each CSV file in the “meets” folder and then gathers the necessary information by indexing each file:  the meet name (from the first row), the meet date (from the second row), and race comments (from the fourth row).  To find the team’s place, the script searches for the string "Ann Arbor Skyline" in the file, and the corresponding number is stored in the team_place variable.

Once the necessary information is extracted, it is formatted into a table by using HTML tags and appending all the information to a string. The script then inserts these table rows into an HTML template with the placeholders for the meet information. The final HTML content is written to a file called deliv2.html, which displays the meet results in table format.
Running the Script:
1. Download the folder “meets” with all the CSV files and have it in the same directory as the python script
2. Run the python script with VS Code which will generate an HTML file
3. Right click on the new HTML file and preview it to see the formatted table with the meet data
