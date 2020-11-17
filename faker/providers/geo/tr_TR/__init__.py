from .. import Provider as GeoProvider


class Provider(GeoProvider):
    # Source: https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_illeri
    land_coords = (
        ('37.003277000000004', '35.3261219', 'Adana',  'TR', 'Europe/Istanbul'),
        ('37.7640008', '38.2764355', 'Adıyaman', 'TR', 'Europe/Istanbul'),
        ('38.756850899999996', '30.538694399999997', 'Afyonkarahisar', 'TR', 'Europe/Istanbul'),
        ('38.3705416', '34.026907', 'Aksaray', 'TR', 'Europe/Istanbul'),
        ('40.6569451', '35.7727169', 'Amasya', 'TR', 'Europe/Istanbul'),
        ('39.921521899999995', '32.8537929', 'Ankara', 'TR', 'Europe/Istanbul'),
        ('36.9009641', '30.6954846', 'Antalya', 'TR', 'Europe/Istanbul'),
        ('41.1102966', '42.7035585', 'Ardahan', 'TR', 'Europe/Istanbul'),
        ('41.160506', '41.839862700000005', 'Artvin', 'TR', 'Europe/Istanbul'),
        ('37.841300700000005', '27.832837400000003', 'Aydın', 'TR', 'Europe/Istanbul'),
        ('39.7201318', '43.050038799999996', 'Ağrı', 'TR', 'Europe/Istanbul'),
        ('39.6473917', '27.8879787', 'Balıkesir', 'TR', 'Europe/Istanbul'),
        ('41.6338394', '32.3384354', 'Bartın', 'TR', 'Europe/Istanbul'),
        ('37.7874104', '41.2573924', 'Batman', 'TR', 'Europe/Istanbul'),
        ('40.25569', '40.224099', 'Bayburt', 'TR', 'Europe/Istanbul'),
        ('40.1435101', '29.975291100000003', 'Bilecik', 'TR', 'Europe/Istanbul'),
        ('38.8851831', '40.4965998', 'Bingöl', 'TR', 'Europe/Istanbul'),
        ('38.4002185', '42.1081317', 'Bitlis', 'TR', 'Europe/Istanbul'),
        ('40.733295299999995', '31.6110479', 'Bolu', 'TR', 'Europe/Istanbul'),
        ('37.7248394', '30.288728600000002', 'Burdur', 'TR', 'Europe/Istanbul'),
        ('40.1826036', '29.067565500000004', 'Bursa', 'TR', 'Europe/Istanbul'),
        ('37.773483299999995', '29.087389399999996', 'Denizli', 'TR', 'Europe/Istanbul'),
        ('37.9167321', '40.2225658', 'Diyarbakır', 'TR', 'Europe/Istanbul'),
        ('40.8458611', '31.164851000000002', 'Düzce', 'TR', 'Europe/Istanbul'),
        ('41.675932700000004', '26.5587225', 'Edirne', 'TR', 'Europe/Istanbul'),
        ('38.5824771', '39.396179', 'Elazığ', 'TR', 'Europe/Istanbul'),
        ('39.749605200000005', '39.4941023', 'Erzincan', 'TR', 'Europe/Istanbul'),
        ('39.7581897', '41.4032241', 'Erzurum', 'TR', 'Europe/Istanbul'),
        ('39.766681299999995', '30.5255947', 'Eskişehir', 'TR', 'Europe/Istanbul'),
        ('37.0611756', '37.3793085', 'Gaziantep', 'TR', 'Europe/Istanbul'),
        ('40.9148702', '38.3879289', 'Giresun', 'TR', 'Europe/Istanbul'),
        ('40.4617844', '39.475733899999994', 'Gümüşhane', 'TR', 'Europe/Istanbul'),
        ('37.574898', '43.73766', 'Hakkari', 'TR', 'Europe/Istanbul'),
        ('36.202593900000004', '36.1603945', 'Hatay', 'TR', 'Europe/Istanbul'),
        ('37.77035', '30.5556933', 'Isparta', 'TR', 'Europe/Istanbul'),
        ('39.921566799999994', '44.0467724', 'Iğdır', 'TR', 'Europe/Istanbul'),
        ('37.5812744', '36.927509', 'Kahramanmaraş', 'TR', 'Europe/Istanbul'),
        ('41.1110349', '32.619390100000004', 'Karabük', 'TR', 'Europe/Istanbul'),
        ('37.179244700000005', '33.222478100000004', 'Karaman', 'TR', 'Europe/Istanbul'),
        ('40.605158', '43.0961734', 'Kars', 'TR', 'Europe/Istanbul'),
        ('41.3765359', '33.7770087', 'Kastamonu', 'TR', 'Europe/Istanbul'),
        ('38.7225274', '35.4874516', 'Kayseri', 'TR', 'Europe/Istanbul'),
        ('36.718045000000004', '37.11688', 'Kilis', 'TR', 'Europe/Istanbul'),
        ('40.765382', '29.9406983', 'Kocaeli', 'TR', 'Europe/Istanbul'),
        ('37.8719963', '32.484401500000004', 'Konya', 'TR', 'Europe/Istanbul'),
        ('39.4191505', '29.987292800000002', 'Kütahya', 'TR', 'Europe/Istanbul'),
        ('41.7370223', '27.223552299999998', 'Kırklareli', 'TR', 'Europe/Istanbul'),
        ('39.8485708', '33.5276222', 'Kırıkkale', 'TR', 'Europe/Istanbul'),
        ('39.14611420000001', '34.1605587', 'Kırşehir', 'TR', 'Europe/Istanbul'),
        ('38.3483098', '38.3178715', 'Malatya', 'TR', 'Europe/Istanbul'),
        ('38.615502899999996', '27.4255716', 'Manisa', 'TR', 'Europe/Istanbul'),
        ('37.341485399999996', '40.7476249', 'Mardin', 'TR', 'Europe/Istanbul'),
        ('36.8117583', '34.6292679', 'Mersin', 'TR', 'Europe/Istanbul'),
        ('37.1642053', '28.2624288', 'Muğla', 'TR', 'Europe/Istanbul'),
        ('38.740370299999995', '41.4967451', 'Muş', 'TR', 'Europe/Istanbul'),
        ('38.6223688', '34.713602200000004', 'Nevşehir', 'TR', 'Europe/Istanbul'),
        ('37.971207899999996', '34.6775534', 'Niğde', 'TR', 'Europe/Istanbul'),
        ('40.8292569', '37.4082764', 'Ordu', 'TR', 'Europe/Istanbul'),
        ('37.073671000000004', '36.255941', 'Osmaniye', 'TR', 'Europe/Istanbul'),
        ('41.022809', '40.519612', 'Rize', 'TR', 'Europe/Istanbul'),
        ('40.7731834', '30.481606', 'Sakarya', 'TR', 'Europe/Istanbul'),
        ('41.2889924', '36.329445899999996', 'Samsun', 'TR', 'Europe/Istanbul'),
        ('37.931282', '41.939840000000004', 'Siirt', 'TR', 'Europe/Istanbul'),
        ('42.0266698', '35.1506765', 'Sinop', 'TR', 'Europe/Istanbul'),
        ('39.7503572', '37.0145185', 'Sivas', 'TR', 'Europe/Istanbul'),
        ('40.986222999999995', '27.513944', 'Tekirdağ', 'TR', 'Europe/Istanbul'),
        ('40.327746999999995', '36.5539494', 'Tokat', 'TR', 'Europe/Istanbul'),
        ('41.0058605', '39.718092799999994', 'Trabzon', 'TR', 'Europe/Istanbul'),
        ('39.1080631', '39.548196999999995', 'Tunceli', 'TR', 'Europe/Istanbul'),
        ('38.6710838', '29.407250899999998', 'Uşak', 'TR', 'Europe/Istanbul'),
        ('38.508360100000004', '43.374532200000004', 'Van', 'TR', 'Europe/Istanbul'),
        ('40.6556669', '29.272909100000003', 'Yalova', 'TR', 'Europe/Istanbul'),
        ('39.8205571', '34.8094917', 'Yozgat', 'TR', 'Europe/Istanbul'),
        ('41.250324', '31.8389738', 'Zonguldak', 'TR', 'Europe/Istanbul'),
        ('40.1534952', '26.4140933', 'Çanakkale', 'TR', 'Europe/Istanbul'),
        ('40.5971947', '33.6212704', 'Çankırı', 'TR', 'Europe/Istanbul'),
        ('40.54914960000001', '34.9602453', 'Çorum', 'TR', 'Europe/Istanbul'),
        ('41.0096334', '28.9651646', 'İstanbul', 'TR', 'Europe/Istanbul'),
        ('38.415342100000004', '27.144474', 'İzmir', 'TR', 'Europe/Istanbul'),
        ('37.2595198', '39.0408174', 'Şanlıurfa', 'TR', 'Europe/Istanbul'),
        ('37.455253000000006', '42.5212049', 'Şırnak', 'TR', 'Europe/Istanbul'),
        )