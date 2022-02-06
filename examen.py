def anadirPar(hoyo, golpes, hoyos):
    hoyos[hoyo] = (int(golpes), '')


def anadirResultado(hoyo, golpes, hoyos):
    hoyos[hoyo] = ('', int(golpes))

def anadirParResultado(hoyo, par, resultado, hoyos):
    hoyos[hoyo] = (int(par), int(resultado))


def listado(hoyos):
    for hoyo, golpes in hoyos.items():
        print(f'Hoyo {hoyo}: {golpes}')


def termino_golf(hoyo, hoyos):
    par, golpes = hoyos[hoyo]
    resultado = golpes - par
    puntuaciones = {'0':'Par', '-1':'Birdie', '1':'Bogey', '-2':'Eagle', '2':'Doble bogey'}
    return puntuaciones[str(resultado)]


def resultado_actual(hoyos):
    resultado_total = 0
    for hoyo in hoyos.keys():
        if hoyos[hoyo]!='':
            par, golpes = hoyos[hoyo]
            if par!='' and golpes!='':
                resultado = golpes - par
                resultado_total += resultado

    return resultado_total



if __name__ == '__main__':

    hoyos = {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':'', '9':'', '10':'', 
                    '11':'', '12':'', '13':'', '14':'', '15':'', '16':'', '17':'', '18':''}

    

    while True:

        comando = input('¿Qué quieres hacer?\n')
        comando = comando.lower()


        if comando[:3]=='par':
            par, hoyo, golpes = comando.split(' ')
            if 18>=int(hoyo)>0:
                if hoyos[hoyo]!='':
                    par, resultado = hoyos[hoyo]
                    if par!='':
                        confirmacion=input('Ya existen datos para ese hoyo. ¿Estás seguro?\n')
                        if confirmacion.lower()=='si':
                            if resultado=='':
                                anadirPar(hoyo, golpes, hoyos)
                            else:
                                anadirParResultado(hoyo, golpes, resultado, hoyos)
                    elif par=='' and resultado!='':
                        anadirParResultado(hoyo, golpes, resultado, hoyos)
                        print(termino_golf(hoyo, hoyos))

                elif hoyos[hoyo]=='':
                    anadirPar(hoyo, golpes, hoyos)

            else:
                print('Debes introducir un hoyo válido.')

        elif comando[0].isnumeric():
            hoyo, golpes = comando.split(' ')

            if 18>=int(hoyo)>0:
                if hoyos[hoyo]!='':
                    par, resultado = hoyos[hoyo]
                    if resultado!='':
                        confirmacion=input('Ya existen datos para ese hoyo. ¿Estás seguro?\n')
                        if confirmacion.lower()=='si':
                            if par=='':
                                anadirResultado(hoyo, golpes, hoyos)
                            else:
                                anadirParResultado(hoyo, par, golpes, hoyos)
                    elif resultado=='' and par!='':
                        anadirParResultado(hoyo, par, golpes, hoyos)
                        print(termino_golf(hoyo, hoyos))

                elif hoyos[hoyo]=='':
                    anadirResultado(hoyo, golpes, hoyos)

            else:
                print('Debes introducir un hoyo válido.')

        elif comando=='listado':
            listado(hoyos)

        elif comando=='resultado':
            print('El resultado actual es:', resultado_actual(hoyos))

        elif comando=='adios':
            print('Adiós :)')
            break
            

        else:
            print('Debes introducir una acción válida.')
        
