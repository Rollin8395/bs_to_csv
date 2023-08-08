import openpyxl

# Create a new Excel workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Define headings
headings = ["Project Name", "Company Name", "Stipend Amount"]

# Write headings to the first row
sheet.append(headings)

# Save the workbook to a file
excel_file_path = "scraped_data.xlsx"
workbook.save(excel_file_path)






