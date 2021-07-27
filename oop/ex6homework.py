class Pc:
    def __init__(self, memory = 1024, disc=None, model="helwet Paccard", cpu=4):
        self.memory = memory
        self.disc = disc
        self.model = model
        self.cpu = cpu

    def __str__(self):
        return f"{self.memory}, {self.disc},{self.model}, {self.cpu}"

class PersonPc(Pc):
    def __init__(self, *args, monitor=None, klav=None, mouse=None, width=0, length=0):

        super().__init__(*args)
        self.monitor = monitor
        self.klav = klav
        self.mouse = mouse
        self.width = width
        self.length = length

    def infoPc(self):
        print('Настольный пк:'
              'Монитор: {},'
              'Клавиатура: {},'
              'Мышь: {},'
              'Ширина: {},'
              'Длина: {},'
              'Память: {},'
              'Дсковод: {},'
              'Модель: {},'
              'CPU: {}'.format(
                  self.monitor,
                  self.klav,
                  self.mouse,
                  self.width,
                  self.length,
                  self.memory,
                  self.disc,
                  self.model,
                  self.cpu))


class NoteBook(Pc):
    def __init__(self,width=0, length=0,  *args ):
        super().__init__(*args)
        self.width = width
        self.length = length

    def infoPC(self):
        print('Ширина: {},'
              'Длина: {},'
              'Память: {},'
              'Дсковод: {},'
              'Модель: {},'
              'CPU: {}'.format(self.width,
        self.length,
        self.memory,
        self.disc,
        self.model,
        self.cpu))


#p = PersonPc(monitor='LG', klav='ATECH', mouse='ATECH', width=1000, length=2000)
#p.infoPc()


n = NoteBook(800, 1500)
n.infoPC()
