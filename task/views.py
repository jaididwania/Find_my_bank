from django.shortcuts import render,HttpResponse
import csv


def home_view(request):
    return render(request,'base.html')

def bankByIFSC(request):
    
    csvfile = csv.reader(open('csv_file/bank_branches.csv',"r",encoding="utf-8"))
    ifsc_check = request.POST.get('IFSCcode')  #Fetching the I/P IFSC Code by User

    ifsc_code=""
    branchId=""
    branch=""
    branch_address=""
    city=""
    district=""
    state=""
    bank_name=""

    ifsc_check = str(ifsc_check.upper())

    found_status = 0
    for row in csvfile:
        if ifsc_check == row[0]:
            ifsc_code = row[0]
            branchId = row[1]
            branch = row[2]
            branch_address = row[3]
            city = row[4]
            district = row[5]
            state = row[6]
            bank_name = row[7]
            found_status = 1
            break
    context = {
        "ifsc_code" : ifsc_code,
        "branchId" : branchId,
        "branch" : branch,
        "branch_address" : branch_address,
        "city" : city,
        "district" : district,
        "state" : state,
        "bank_name" : bank_name,
        "found_status" : found_status
    }

    return render(request,'newsearch.html',context)


def bankByNameandCity(request):
    
    csvfile = csv.reader(open('csv_file/bank_branches.csv',"r",encoding="utf-8"))
    bank_name =  request.POST.get('BankName')
    bank_city = request.POST.get('City')    
    list_of_banks = []
    bank_name = str(bank_name.upper())
    bank_city = str(bank_city.upper())
    found_status = 0
    for row in csvfile:
        if bank_city == row[4] and bank_name == row[7] :
            list_of_banks.append({"ifsc_code":row[0],"branchId":row[1],"branch":row[2],"branch_address":row[3],"city":row[4],"district":row[5],"state":row[6],"bank_name":row[7]})
            found_status = 1    

    context = {
        'list_of_banks' : list_of_banks,
        'found_status' : found_status,
    }

    return render(request,'newsearch2.html',context)