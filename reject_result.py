import zeep


client = zeep.Client(
    wsdl='http://localhost:8080/webservices/chelyabinsk_household_info.wsdl'
)

ticket_id = '73589'

result = client.service.getResultRequest(
    Message={
        'Sender': {
            'Code': 'testcode',
            'Name': 'testname',
        },
        'Recipient': {
            'Code': 'ISMV01001',
            'Name': 'test',
        },
        'Originator': {
            'Code': 'RRTR01001',
            'Name': 'test',
        },
        'ServiceName': 'test_service_name',
        'TypeCode': 'test_type',
        'Status': 'REQUEST',
        'Date': '2017-11-27T06:21:51.063+03:00',
        'ExchangeType': 2,
        'CaseNumber': '74/011/201/2017-2689',
    },
    MessageData={
        'AppData': {
            'ApplicationData': {
                'getResultRequest': {
                    'ticketId': ticket_id
                },
            },
        },
    },
)

print(
    result.AppData.ApplicationData.getResultResponse.requestStatus,
    result.AppData.ApplicationData.getResultResponse.errorText
)
