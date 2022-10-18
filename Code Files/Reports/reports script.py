#Generate PDF
if event.source.parent.getComponent('report type').selected:
	reportName = system.tag.read('[default]GotoGro/reportName').value + ".pdf"
	# Executes and distributes the report to save a PDF
	settings = {"path":"C:\\Users\\gotogro\\Desktop\\reports\\Member Sales Summary Report\\pdf", "fileName":reportName, "format":"pdf"}
	system.report.executeAndDistribute(path="Member Sales Summary Report", project="GotoGro", action="save", actionSettings=settings)
else:
	reportName = system.tag.read('[default]GotoGro/reportName 2').value + ".pdf"
	# Executes and distributes the report to save a PDF
	settings = {"path":"C:\\Users\\gotogro\\Desktop\\reports\\Weekly Sales Report", "fileName":reportName, "format":"pdf"}
	system.report.executeAndDistribute(path="Weekly Sales Report", project="GotoGro", action="save", actionSettings=settings)
	

#Generate CSV
if event.source.parent.getComponent('report type').selected:
	reportName = system.tag.read('[default]GotoGro/reportName').value + ".csv"
	# Executes and distributes the report to save a PDF
	settings = {"path":"C:\\Users\\gotogro\\Desktop\\reports\\Member Sales Summary Report\\csv", "fileName":reportName, "format":"csv"}
	system.report.executeAndDistribute(path="Member Sales Summary Report", project="GotoGro", action="save", actionSettings=settings)
else:
	reportName = system.tag.read('[default]GotoGro/reportName 2').value + ".csv"
	# Executes and distributes the report to save a PDF
	settings = {"path":"C:\\Users\\gotogro\\Desktop\\reports\\Weekly Sales Report", "fileName":reportName, "format":"csv"}
	system.report.executeAndDistribute(path="Weekly Sales Report", project="GotoGro", action="save", actionSettings=settings)


#View Reports
system.net.openURL("https://drive.google.com/drive/folders/1-8J87bGnvLSu8psG_dR9KrML1PpTHN7t?usp=sharing")

#filename logic
reportName= "Member_" + {[.]selectedMemberID.value} + "_Sales_Report_" + dateFormat(now(1000), "yyyy-mm-dd hhmmss")

reportname 2 = "Weekly_Sales_Report_" + dateFormat(now(1000), "yyyy-mm-dd hhmmss")