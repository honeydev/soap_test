import zeep


client = zeep.Client(
    wsdl='http://localhost:8080/webservices/chelyabinsk_household_info.wsdl'
)

response = client.service.getInfoRequest(
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
            'Name': 'test'
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
                'getInfoRequest': {
                    'usznName': 'Управление социальной защиты населения Челябинской области',
                    'omsuName': 'Орган местного самоуправления Челябинской области',
                    'serviceName': 'Предоставление сведений о личном подсобном хозяйстве и гражданах проживающих в нем',
                    'sourceName': 'Реквизиты и ссылки на НПА',
                    'requestAuthor': 'Тестовый автор запроса',
                    'authorPost': 'Должность автора запроса',
                    'authorPhone': '89141111111',
                    'authorEmail': 'testauthor@email.com',
                    'requestDate': '2012-12-13',
                    'requestPersonInfo': {
                        'firstname': 'Игорь',
                        'lastname': 'Плохой',
                        'patronymic': 'Петрович',
                        'birthDate': '1979-01-01',
                        'personAddress': {
                            'postIndex': '457000',
                            'regionName': 'Челябинская область',
                            'districtName': 'Агаповский район',
                            'place': 'Буранное',
                            'placeType': 'г',
                            'street': 'Бабушкина',
                            'streetType': 'ул',
                            'house': '15',
                            'flat': '0',
                            'building': '0'
                        },
                        'personDocument': {
                            'docType': 'Паспорт гражданина РФ',
                            'docSeries': '7509',
                            'docNumber': '725161',
                            'docDate': '2002-03-25',
                            'docSource': 'Красноармейским РОВД Челябинской области'
                        },
                    },
                },
            },
        },
    },
)


ticket_id = response.AppData.ApplicationData.getInfoResponse.ticketID

print(ticket_id)
