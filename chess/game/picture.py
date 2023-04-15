from . import colors
class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in colors.inverter:
            return color
        return colors.inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        invVertical = []
        n = len(self.img)
        for i in range (0, n):
            line = ""
            aux = self.img[i]
            for u in reversed(aux):
                line += u
            invVertical.append(line)
        return Picture(invVertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        invHorizontal = []
        for i in reversed(self.img):
            invHorizontal.append(i)
        return Picture(invHorizontal)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        # devuelve negativo cambiando el string
        nega = []
        n = len(self.img)

        for i in range(0, n):
            line = ""
            for u in self.img[i]:
                line += self._invColor(u)
            nega.append(line)
        return Picture(nega)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento
        al lado derecho de la figura actual """
        #la metodologia sera unir en un solo array cada fila de los dos arrays
        juntos = []
        for i in range (0, len(self.img)):
            juntos.append(self.img[i] + p.img[i])

        return Picture(juntos)

    def up(self, p):
        #pondra 'arriba' de la figura actual una figura
        juntos = []

        for i in range(0, len(self.img) + len(p.img)):
        #primero coloco a la otra figura

            if(i < len(p.img)):
                juntos.append(p.img[i])
            else:
                juntos.append(self.img[i - len(p.img)])

        return Picture(juntos)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
        sq = self.img[0][0] #para square negativo
        if(sq == " "):
            sq = "_"

        su = []
        for i in range(0, len(p.img)):
            linea = ""
            for u in p.img[i]:
                if(u == " "):
                    linea += sq
                else:
                    linea += u
            su.append(linea)

        return Picture(su)

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """

        pAux = Picture(self.img)
        #se reutilizara join()
        for i in range (n - 1):
            pAux = pAux.join(self)
        return pAux

    def verticalRepeat(self, n):

        pAux = Picture(self.img)
        #se reutilizara la funcion up()
        for i in range(n - 1):
            pAux = pAux.up(self)
        return pAux

    #Extra: Sólo para realmente viciosos
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""

        fil = len(self.img)
        col = len(self.img[0])
        result = []

        for i in range(col):
            line = ""
            for j in range(fil):
                line += self.img[fil-1-j][i]
            result.append(line)

        return Picture(result)
