from compass import Compass
import pytest


def test_compass_creation():
    compass = Compass(40)
    assert compass.heading == 40
    compass = Compass(230)
    assert compass.heading == 230

    with pytest.raises(TypeError):
        compass = Compass(400)

    with pytest.raises(TypeError):
        compass = Compass(-1)


def test_get_direction():
    compass = Compass(40)
    assert compass.get_direction() == 'NE'
    compass = Compass(250)
    assert compass.get_direction() == 'W'
    compass = Compass(140)
    assert compass.get_direction() == 'SE'
    compass = Compass(355)
    assert compass.get_direction() == 'N'


def test_turn():
    compass = Compass(40)
    compass.turn(40, 'left')
    assert compass.heading == 0

    compass.turn(100, 'right')
    assert compass.heading == 100

    compass.turn(1, 'left')
    assert compass.heading == 99

    compass.turn(100, 'left')
    assert compass.heading == 359

    compass.turn(50, 'right')
    assert compass.heading == 49

    compass.turn(400, 'right')
    assert compass.heading == 89

    compass.turn(700, 'right')
    assert compass.heading == 69

    compass.turn(620, 'left')
    assert compass.heading == 169

    compass.turn(0, 'right')
    assert compass.heading == 169


def test_add():
    compass = Compass(40)
    assert compass + 40 == 80
    assert compass + 100 == 140
    assert compass + 350 == 30
    assert compass + 700 == 20
    assert compass + 0 == 40


def test_sub():
    compass = Compass(40)
    assert compass - 40 == 0
    assert compass - 10 == 30
    assert compass - 50 == 350
    assert compass - 700 == 60
    assert compass - 0 == 40


def test_eq():
    compass1 = Compass(25)
    compass2 = Compass(25)
    compass3 = Compass(40)

    assert compass1 == compass2
    assert compass2 != compass3

    compass2.turn(15, 'right')
    assert compass1 != compass2
    assert compass2 == compass3


def test_gt():
    with pytest.raises(TypeError):
        compass = Compass(1)
        compass > compass


def test_lt():
    with pytest.raises(TypeError):
        compass = Compass(1)
        compass < compass
