import unittest
import ejemplo01
import ejemplo02
import ejemplo03
import ejemplo04
import math
import ejemplo05

number1=0
class TestEjemplo01(unittest.TestCase):
    def test_ejemplo01(prog):
        prog.assertEqual(ejemplo01.calcular_promedio(4,6), 5)
    def test_ejemplo02(prog):
        prog.assertEqual(ejemplo02.clasificar_numero(5), 'Positivo')
        prog.assertEqual(ejemplo02.clasificar_numero(-3), 'Negativo')
        prog.assertEqual(ejemplo02.clasificar_numero(0), 'Cero')
    def test_ejemplo03(prog):
        prog.assertEqual(ejemplo03.imprimir_numeros(), 11)
    def test_ejemplo04(prog):
        prog.assertEqual(ejemplo04.calcular_area_circulo(1), math.pi)
    def test_ejemplo05(prog):
        arreglo = [1, 2, 3, 4, 5]
        prog.assertTrue(ejemplo05.buscar_elemento(arreglo,3),"El elemento no fue encontrado cuando debería.") 
        prog.assertIsNot(ejemplo05.buscar_elemento(arreglo,6),"El elemento fue encontrado cuando no debería.") 