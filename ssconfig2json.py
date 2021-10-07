import base64


class config2json:
    def __init__(self, uri=None, mark=None):
        if uri = None or mark = None:
            return 'Missing requi'
        self.main_dict = {'configs': [], 'localPort': 1080, 'shareOverLan': False}
        self.iplist = []
        self.sscounter = 0
        self.ss = uri
        self.json = open("/".join(self.ss.split('/')[:-1]) + '/gui-config.json', mode='w')
        self.ss = open(self.ss, mode='r')
        self.ssconfig = self.ss.read()
        self.ss.close()
        self.remark = mark
        self.model = {'method': '',
                      'password': '',
                      'remarks': self.remark,
                      'server': '',
                      'server_port': 0
                      }
        self.parts = None
        self.debased = None
        

    def conversation(self):
        self.ssconfig = self.ssconfig.replace('\r\n', '\n')
        self.ssconfig = self.ssconfig.replace('ss://', '')
        self.ssconfig = self.ssconfig.split('\n')
        for uri in self.ssconfig:
            if '#' in uri:
                uri = uri.split('#')[0]
            self.parts = uri.split('@')
            if self.parts[1].split(':')[0] in self.iplist:
                continue
            else:
                self.model['server'] = self.parts[1].split(':')[0]
            try:
                self.debased = base64.b64decode(self.parts[0]).decode('utf-8')
            except:
                self.debased = base64.b64decode(self.parts[0] + '==').decode('utf-8')
            self.model['method'] = self.debased.split(':')[0]
            self.model['password'] = self.debased.split(':')[1]
            self.model['server_port'] = int(self.parts[1].split(':')[1])
            self.main_dict['configs'].append(self.model)
            self.model = {'method': '',
                          'password': '',
                          'remarks': self.remark,
                          'server': '',
                          'server_port': 0
                          }
            self.sscounter = self.sscounter + 1
        self.json.write(str(self.main_dict))
        self.json.close()
        print(f'Converted {self.sscounter} shadowsocks uris!!!')
        return 0

if __name__ == '__main__':
    conversationer = config2json(input('Input the position of list file of shadowsocks uris: '), input('Input their remarks: '))
    conversationer.conversation()

