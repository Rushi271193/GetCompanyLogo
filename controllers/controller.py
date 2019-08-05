"""
Author      : Rushikesh Kulkarni
Created At  : 27 June 2019
Last modified by : Rushikesh Kulkarni
Last modified dat: 29 June 2019
Description : App that will return the company logo based on most common characters
Dependancies: Data file "data/data.json" which contain company details.
"""


from flask import Flask, request, jsonify,send_from_directory,render_template
import json,ast
import os
import utils as util


app = Flask(__name__)
app.config["DEBUG"]=True

# Reads the data.json file
data_source = os.path.join(os.path.dirname(os.path.realpath(__file__)),
    "model/data.json")
view = os.path.join(os.path.dirname(os.path.realpath(__file__)),
    "views/mainview.html")


# To handle all the errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({ "status": "404","data" : "Page Not Found!" })


@app.route('/api/view', methods=['GET'])
def get_company_logo_view():
    return render_template('mainview.html') 

# Api to return company logo
@app.route('/api/getcompanylogo', methods=['GET'])
def get_company_logo():
    
    match_found = []

    # To handle if user does not specify company id
    if 'id' in request.args:
        id = request.args['id']
    else:
        return jsonify({ "status": "200","data" : "Please specify company id!" })

    raw_company_details = read_json_data(data_source)
    finalLogoString = ""
    for company in raw_company_details['companyList']:
        if company['CompanyId'] == id:
           
            match_found.append(company)
            
            finalLogoString = get_most_characters(company)
            companyId = company['CompanyId']
            companyName = company["Company Name"]




    # If no company is found with the given id
    if not match_found:
        result = {
            "status" : "200",
            "data" : "No companies found with the given id!"
        }
    else:
        result = { 
            "status" : "200",
            "companyId":companyId,
            "companyName" : companyName,
            "logoCharacters": finalLogoString

        }
    return jsonify(result)
   

# Parses all the data from json and returns json
def read_json_data(data_source):
    raw_json_data = open(data_source,'r')
    data = ast.literal_eval(json.dumps(json.loads(raw_json_data.read())))
    return data

#Logic for finding most characters
def get_most_characters(company): 
    repeatedCharacters = util.checkMultipleValuesPresentInString(company["Company Name"])
    logoString=""
    if len(repeatedCharacters)>2:
        logoString = util.prepareFinalOutputString(repeatedCharacters)
    else:
        sortedString = util.checkAsciForOrder( company["Company Name"],repeatedCharacters)
        logoString = util.prepareFinalOutputString(sortedString)

    return logoString
