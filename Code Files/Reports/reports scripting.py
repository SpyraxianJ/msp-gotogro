#Generate PDF
# Executes and distributes the report to save a PDF
settings = {"path":"C:\\Users\\gotogro\\Desktop\\reports\\pdf", "fileName":report, "format":"pdf"}
system.report.executeAndDistribute(path="Sales Report", project="GotoGro", action="save", actionSettings=settings)

#Generate CSV
# Executes and distributes the report to save a csv
settings = {"path":"C:\\Users\\gotogro\\Desktop\\reports\\csv", "fileName":reportName, "format":"csv"}
system.report.executeAndDistribute(path="Sales Report", project="GotoGro", action="save", actionSettings=settings)

#View Reports
system.net.openURL("https://drive.google.com/drive/folders/1-8J87bGnvLSu8psG_dR9KrML1PpTHN7t?usp=sharing")