class Pessoa:
    def __init__(self,nome):
        self.nome=nome
class InscricaoDeAluno:
    def __init__(self,universidade):
        self.valor=50
        self.universidade=universidade
class InscricaoDeProfessor:
    def __init__(self,universidade):
        self.valor=80
        self.universidade=universidade
class InscricaoDeProfissionais:
    def __init__(self,universidade):
        self.valor=120
        self.universidade=universidade
class Encoinfo:
    def __init__(self):
        self.inscritos=[]
class Inscrito:
    def __init__(self,pessoa,inscricao):
        self.pessoa=pessoa
        self.inscricao=inscricao
class Atendente(Pessoa):
    def __init__(self,nome,encoinfo):
        super().__init__(nome)
        self.contAluno=0
        self.contProf=0
        self.contProfi=0
        self.qtAtendimetos=0
        self.encoinfo=encoinfo
    def atender(self, pessoa, inscricao):
        if len(self.encoinfo.inscritos)<100:
            self.encoinfo.inscritos.append(Inscrito(pessoa,inscricao))
            self.qtAtendimetos+=1                       #Insere atendimento no contador do atendente 
            if type(inscricao)==InscricaoDeAluno:
                self.contAluno+=1
            elif type(inscricao)==InscricaoDeProfessor:
                self.contProf+=1
            elif type(inscricao)==InscricaoDeProfissionais:
                self.contProfi+=1
        else:
            self.emitirRelatorio()
    def emitirRelatorio(self):
        ca=0
        cProfe=0
        cProfi=0
        for i in self.encoinfo.inscritos:
            if type(i.inscricao)==InscricaoDeAluno:
                ca+=1
            elif type (i.inscricao)==InscricaoDeProfessor:
                cProfe+=1
            elif type(i.inscricao)==InscricaoDeProfissionais:
                cProfi+=1
        arq = open('DADOS DO ENCOINFO 2018.txt','w')
        largura = 80
        largura_CNPJ = int(.2*largura)
        largura_nome = int(.2*largura)
        largura_qt = int(.2*largura)
        largura1 = int(.2*largura)
        largura2 = int(.2*largura)
        largura3 = int(.2*largura)
        largura4 = int(.2*largura)
        largura5 = int(.3*largura)

        #Tabela relatorio dos tipos de inscriçoes
        arq.write('+{}+{}+{}+\n'.format('_'*largura_CNPJ,'_'*largura_nome,'_'*largura_qt))
        arq.write('|{:^{lc}}|{:^{ln}}|{:^{lq}}|\n'.format('Tipo','Quantidade','Total pago',lc=largura_CNPJ,ln=largura_nome,lq=largura_qt))
        arq.write('+{}+{}+{}+\n'.format('_'*largura_CNPJ,'_'*largura_nome,'_'*largura_qt))
        arq.write('|{:<{lc}}|{:<{ln}}|{:<{lq}}|\n'.format(("Alunos"),ca,"R$:"+(str(self.contAluno*50)),lc=largura_CNPJ,ln=largura_nome,lq=largura_qt))
        arq.write('|{:<{lc}}|{:<{ln}}|{:<{lq}}|\n'.format(("Professores"),cProfe,"R$:"+(str(self.contProf*80)),lc=largura_CNPJ,ln=largura_nome,lq=largura_qt))
        arq.write('|{:<{lc}}|{:<{ln}}|{:<{lq}}|\n'.format(("Profissionais"),cProfi,"R$:"+(str(self.contProfi*120)),lc=largura_CNPJ,ln=largura_nome,lq=largura_qt))
        arq.write('|{:<{lc}}|{:<{ln}}|{:<{lq}}|\n'.format(("VALORES TOTAIS"),cProfi+ca+cProfe,"R$:"+(str(self.contProfi*120+self.contProf*80+self.contAluno*50)),lc=largura_CNPJ,ln=largura_nome,lq=largura_qt))
        arq.write('+{}+{}+{}+\n'.format('_'*largura_CNPJ,'_'*largura_nome,'_'*largura_qt)) 

        #Tabela relatorio dos atendentes
        arq.write('\n'+'** Relatorio de funcionarios **'+"\n")
        arq.write('+{}+{}+{}+{}+{}+\n'.format('_'*largura1,'_'*largura2,'_'*largura3,'_'*largura4,'_'*largura5))
        arq.write('|{:^{lc}}|{:^{ln}}|{:^{lq}}|{:^{lq}}|{:^{lo}}|\n'.format('Nome','Quantidade','Tipo Aluno','Tipo Professor','Tipo Profissional',lc=largura1,ln=largura2,lq=largura3,lp=largura4,lo=largura5))
        arq.write('+{}+{}+{}+{}+{}+\n'.format('_'*largura1,'_'*largura2,'_'*largura3,'_'*largura4,'_'*largura5))
        arq.write('|{:^{lc}}|{:^{ln}}|{:^{lq}}|{:^{lq}}|{:^{lo}}|\n'.format(a1.nome,a1.qtAtendimetos,a1.contAluno,a1.contProf,a1.contProfi,lc=largura1,ln=largura2,lq=largura3,lp=largura4,lo=largura5))
        arq.write('|{:^{lc}}|{:^{ln}}|{:^{lq}}|{:^{lq}}|{:^{lo}}|\n'.format(a2.nome,a2.qtAtendimetos,a2.contAluno,a2.contProf,a2.contProfi,lc=largura1,ln=largura2,lq=largura3,lp=largura4,lo=largura5))
        arq.write('|{:^{lc}}|{:^{ln}}|{:^{lq}}|{:^{lq}}|{:^{lo}}|\n'.format(a3.nome,a3.qtAtendimetos,a3.contAluno,a3.contProf,a3.contProfi,lc=largura1,ln=largura2,lq=largura3,lp=largura4,lo=largura5))
        arq.write('|{:^{lc}}|{:^{ln}}|{:^{lq}}|{:^{lq}}|{:^{lo}}|\n'.format("VALORES TOTAIS",a3.qtAtendimetos+a2.qtAtendimetos+a1.qtAtendimetos,a3.contAluno+a2.contAluno+a1.contAluno,a1.contProf+a2.contProf+a3.contProf,a3.contProfi+a2.contProfi+a1.contProfi
        ,lc=largura1,ln=largura2,lq=largura3,lp=largura4,lo=largura5))
        arq.write('+{}+{}+{}+{}+{}+\n'.format('_'*largura1,'_'*largura2,'_'*largura3,'_'*largura4,'_'*largura5))
        arq.close()
#********* PROGRAMA DE TESTE *********
e=Encoinfo()                               #cria objeto encoinfo

a1=Atendente("Crisley",e)                   #cria objetos atendentes
a2=Atendente("Rone",e)
a3=Atendente("Sergio",e)
listaDeAtendentes=[a1,a2,a3]

aluno=InscricaoDeAluno("Ceulp Ulbra")                   #cria objetos instituições
professor=InscricaoDeProfessor("FAPAL")
profissional= InscricaoDeProfissionais("Bitz info") 
listaDeTipo=[aluno,professor,profissional]

arq1=open("LISTA DE NOMES.csv","r")                          #abri um arquivo para pegar nomes de pessoas
nomes=arq1.read().split("\n")
import random

for i in range(101):
    sorteio1=random.randint(0,2)               #Gerar numeros aleatorios 
    sorteio2=None
    sorteio3=random.randint(1,100)
    if sorteio3 <=70:
        sorteio2=0
    elif sorteio3 >70 and sorteio3 <=90:
        sorteio2=1
    else:
        sorteio2=2
    i=Pessoa(nomes[sorteio3])              #Cria um objeto pessoa com nome da pessoa e do objeto aleatorio      
    atendeteLivre=listaDeAtendentes[sorteio1]  #Escolhe o atendente aleatoriamente
    atendeteLivre.atender(sorteio3,listaDeTipo[sorteio2]) #Atendente credencia uma pessoa á um evento.