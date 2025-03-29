from config.ConfigProvider import ConfigProvider

HOST = ConfigProvider().get(section='ui', prop='HOST')
URL = f'{HOST}angularJs-protractor/BankingProject/#/manager'
