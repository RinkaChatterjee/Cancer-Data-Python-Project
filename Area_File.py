import csv
def open_area_file():
    #Step1(P)Open Final_project file to read.
    with open('Final_project.csv', 'r') as csv_file:
        #Step2(I)Reading the Final_project file using the csv DictReader
        csv_reader = csv.DictReader(csv_file)
        #Step3(P)Assign row headers to  variable headers
        headers = ['Cage','Strain','AnimalName','Parameter','Width','Length','Sex','Area','Status']
        #Step4(P)Open the area file to write data from Final_project file as area_file 
        with open('Area.csv', 'w') as area_file:
            #Step5(P)Assign writer to write on area_file along with headers
            writer = csv.DictWriter(area_file, fieldnames=headers)
            #Step6(P)Write header defined in headers
            writer.writeheader()
            #Step7(P)Use for loop to iterate data in sepecific rows and write those data in Area file
            for row in csv_reader:
                #Step8(P)Variable cage,strain,animalname,parameter,width,length,sex are the values assigned to the row values of -
                #Cage, Strain, AnimalName,Parameter,Width,Length,Sex.
                #Width and length string values are converted to float for area calculation.
                cage = row['Cage']
                strain = row['Strain']
                animalname = row['AnimalName']
                parameter = row['Parameter']
                width = float(row['Width'])
                length = float(row['Length'])
                sex = row['Sex']
                #Step9(P)After getting the num5 and num6 and converting them into float values, calculate area
                area = width * length
                #Step10(P)If condition to see the area is greater then or less then 500
                if area >= 500:
                    #Step11(O)Write rows to the area file where the area is greater then 500 and add an additional column name status and write Ready
                    writer.writerow({'Cage':cage,'Strain':strain,'AnimalName':animalname, 'Parameter':parameter,'Width':width,'Length':length,'Sex':sex,\
                                     'Area':format(area, '.2f') ,'Status':'Ready'})
                else:
                    #Step12(O)Write rows to the area file where the area is lesser then 500 and add an additional column name status and write Not Ready
                    writer.writerow({'Cage':cage,'Strain':strain,'AnimalName':animalname, 'Parameter':parameter,'Width':width,'Length':length,'Sex':sex,\
                                     'Area':format(area, '.2f') ,'Status':'Not Ready'})
   
    #Step13(P)close the file
    csv_file.close()
#call open_area_file()
open_area_file()
