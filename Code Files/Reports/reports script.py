#Generate PDF
reportName = system.tag.read('[default]GotoGro/reportName').value + ".pdf"
# Executes and distributes the report to save a PDF
settings = {"path":"C:\\Users\\gotogro\\Desktop\\reports\\pdf", "fileName":reportName, "format":"pdf"}
system.report.executeAndDistribute(path="Sales Report", project="GotoGro", action="save", actionSettings=settings)
report.executeAndDistribute(path="Sales Report", project="GotoGro", action="save", actionSettings=settings)

#Generate CSV
reportName = system.tag.read('[default]GotoGro/reportName').value + ".csv"
# Executes and distributes the report to save a PDF
settings = {"path":"C:\\Users\\gotogro\\Desktop\\reports\\csv", "fileName":reportName, "format":"csv"}
system.report.executeAndDistribute(path="Sales Report", project="GotoGro", action="save", actionSettings=settings)
#View Reports
system.net.openURL("https://drive.google.com/drive/folders/1-8J87bGnvLSu8psG_dR9KrML1PpTHN7t?usp=sharing")

#filename logic
reportName= "Member_" + {[.]selectedMemberID.value} + "_Sales_Report_" + dateFormat(now(1000), "yyyy-mm-dd hhmmss")