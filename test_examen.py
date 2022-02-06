import pytest
from examen import termino_golf, resultado_actual

def test_termino_golf():
    hoyos = {'1':(3, 3), '2':(3, 2), '3':(3, 4), '4':(5, 3), '5':(5, 7), '6':'', '7':'', '8':'', '9':'', '10':'', 
                    '11':'', '12':'', '13':'', '14':'', '15':'', '16':'', '17':'', '18':''}
    
    assert termino_golf('1', hoyos) == 'Par'
    assert termino_golf('2', hoyos) == 'Birdie'
    assert termino_golf('3', hoyos) == 'Bogey'
    assert termino_golf('4', hoyos) == 'Eagle'
    assert termino_golf('5', hoyos) == 'Doble bogey'

def test_resultado_actual():
    hoyos = {'1':(3, 3), '2':(3, 2), '3':(3, 4), '4':(5, 3), '5':(5, 7), '6':'', '7':'', '8':'', '9':'', '10':'', 
                    '11':'', '12':'', '13':'', '14':'', '15':'', '16':'', '17':'', '18':''}

    assert resultado_actual(hoyos) == 0    

    hoyos2 = {'1':(3, 3), '2':(3, 2), '3':(3, 4), '4':(5, 3), '5':(5, 7), '6':(3, 5), '7':'', '8':'', '9':'', '10':'', 
                    '11':'', '12':'', '13':'', '14':'', '15':'', '16':'', '17':'', '18':''}

    assert resultado_actual(hoyos2) == 2

    hoyos3 = {'1':(3, 3), '2':(3, 2), '3':(3, 4), '4':(5, 3), '5':(5, 7), '6':(5, 3), '7':'', '8':'', '9':'', '10':'', 
                    '11':'', '12':'', '13':'', '14':'', '15':'', '16':'', '17':'', '18':''}

    assert resultado_actual(hoyos3) == -2

