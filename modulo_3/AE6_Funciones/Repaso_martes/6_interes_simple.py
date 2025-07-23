""" Cree una función de interés simple, entregando una excepción 
si la tasa es superior a 100.
a. El programa debe recibir: monto, año y tasa.
b. El cálculo de interés será: (monto * año * tasa) / 100
c. Agregue mensajes adecuados al contexto, para la interacción 
del programa. """

def interes_simple():
  try:
    #primero definimos las variables
      monto = float(input('ingrese monto '))
      if monto<=0:
        raise ValueError('monto no puede ser negativo')
      ano = float(input('ingrese años '))
      if ano<=0:
        raise ValueError('el año no puede ser negativo')
      tasa = int(input('ingrese la tasa entre 0 y 100 '))
      if (tasa>100) or (tasa<=0):
        raise ValueError('la tasa debe ser entre 0 y 100')

      #calculamos interes simple
      h = (monto*ano*tasa)/100
      #entregamos resultado
      print('su calculo de interes es de', h )

  except ValueError:
    print('el valor ingresado es erroneo')
  finally:
    print('gracias por operar con nosotros')

interes_simple()