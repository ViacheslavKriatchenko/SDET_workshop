from config.ConfigProvider import ConfigProvider


class Data:
    HOST = ConfigProvider().get(section='ui', prop='HOST')
    URL = f'{HOST}angularJs-protractor/BankingProject/#/manager'
    N = 10
    lname = "Siblicus"
    API_HOST = ConfigProvider().get(section='api', prop='HOST')
