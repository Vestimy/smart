import configparser

NAME = 'config.ini'


class Config(configparser.ConfigParser):
    def __init__(self):
        super(Config, self).__init__()
        self.read(NAME)

    def setparams(self):
        with open(NAME, 'w') as configfile:
            self.write(configfile)

    def set_windowsize(self, a, b):
        a = str(a)
        b = str(b)
        if not 'WINDOWSIZE' in self:
            self['WINDOWSIZE'] = {}

        self['WINDOWSIZE']['width'] = a
        self['WINDOWSIZE']['height'] = b
        #
        self.setparams()

    def get_windowsize(self):
        return int(self['WINDOWSIZE']['width']), int((self['WINDOWSIZE']['height']))

    def get_Maximized(self):
        return self.getboolean('WINDOWSIZE', 'maximized')

    def set_Maximized(self, bool):
        bool = str(bool)
        self['WINDOWSIZE']['maximized'] = bool
        self.setparams()

    def setUrl(self, url):
        self['DBCONF']['host'] = url
        self.setparams()
