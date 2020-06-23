
def html():
    from cloudant.client import Cloudant
    from cloudant.error import CloudantException
    from cloudant.result import Result, ResultByKey
    import time as t
    client = Cloudant("5e42a7d0-ea17-4a3a-bbbf-2cd472931bd0-bluemix", "efe6af61c9872c02b29eb078f9ac872e5fcf41afaa1333bdef1f8ff88d9de508", url="https://5e42a7d0-ea17-4a3a-bbbf-2cd472931bd0-bluemix:efe6af61c9872c02b29eb078f9ac872e5fcf41afaa1333bdef1f8ff88d9de508@5e42a7d0-ea17-4a3a-bbbf-2cd472931bd0-bluemix.cloudantnosqldb.appdomain.cloud")
    client.connect()
    my_database = client.create_database("url")
    #dtt=[]
    result_collection = Result(my_database.all_docs, include_docs=True)
    liss=['URL','Property','Domain','Registrar','Organisation','Alexa Rank','Address','City','State','Zipcode','Country','E-mails','time']
    
    
    html_p="""<!DOCTYPE html><html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
    <!-- Google Fonts Roboto -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <!-- Material Design Bootstrap -->
    <link rel="stylesheet" href="static/css/mdb.min.css'">
    <!-- Your custom styles (optional) -->
    <link rel="stylesheet" href="static/css/style.css">
    <!-- MDBootstrap Datatables  -->
    <link href="static/css/addons/datatables2.min.css" rel="stylesheet">
    <title>Malicious URL Detector</title>
    </head>
        
    <body>

    <h2 class='mb-3'>Data Set</h2>
    <table id="dtBasicExample" class="table" width="100%">
    <thead>
        <tr>
        <th>S.no</th>
        <th>URL</th>
        <th>Status</th>
        <th>Domain</th>
        <th>Registrar</th>
        <th>Organisation</th>
        <th>Alexa Rank</th>
        <th>Address</th>
        <th>City</th>
        <th>State</th>
        <th>Zip Code</th>
        <th>Country</th>
        <th>Email</th>
        <th>Time</th>
        </tr>
    </thead>
    <tbody>"""
    
    # for result in result_collection:
    #     url=str(result['doc']['URL'])
    #     status=str(result['doc']['Property'])
    #     name=str(result['doc']['Name'])
    #     org=str(result['doc']['Organisation'])
    #     add=str(result['doc']['Address'])
    #     city=str(result['doc']['City'])
    #     state=str(result['doc']['State'])
    #     ziip=str(result['doc']['Zipcode'])
    #     country=str(result['doc']['Country'])
    #     email=str(result['doc']['E-mails'])
    #     dom=str(result['doc']['Domain'])
    #     rank=str(result['doc']['Alexa Rank'])
    #     reg=str(result['doc']['Registrar'])
    #     time=str(result['doc']['time'])
    #     a=[url,status,name,org,add,city,state,ziip,country,email,dom,rank,reg,time]
    #     dtt.append(a)
    #     t.sleep(0.0001)
    ii=0
    import csv
    with open("static/cloudant_count2.csv", "r") as f:
        for row in f:
            cot=int(row)
    cott=cot-2000
    res=result_collection[cott:]
    for result in res:
        ii=ii+1
        html_p=html_p+"<tr>"
        html_p=html_p+"<td>"+str(ii)+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['URL'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Property'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Domain'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Registrar'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Organisation'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Alexa Rank'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Address'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['City'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['State'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Zipcode'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['Country'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['E-mails'])+"</td>"
        html_p=html_p+"<td>"+str(result['doc']['time'])+"</td>"
        html_p=html_p+"</tr>"
        t.sleep(0.0000001)

    html_p=html_p+"""</tbody></table>
    <!-- End your project here-->

    <!-- jQuery -->
    <script type="text/javascript" src="static/js/jquery.min.js"></script>
    <!-- Bootstrap tooltips -->
    <script type="text/javascript" src="static/js/popper.min.js"></script>
    <!-- Bootstrap core JavaScript -->
    <script type="text/javascript" src="static/js/bootstrap.min.js"></script>
    <!-- MDB core JavaScript -->
    <script type="text/javascript" src="static/js/mdb.min.js"></script>
    <!-- MDBootstrap Datatables  -->
    <script type="text/javascript" src="static/js/addons/datatables2.min.js"></script>
    <script>
    $(document).ready(function () {
    $('#dtBasicExample').DataTable();
    $('.dataTables_length').addClass('bs-select');
    });
    </script>

    </body>
    </html>"""
    return html_p