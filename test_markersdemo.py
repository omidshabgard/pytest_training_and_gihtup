import pytest


@pytest.mark.smoke
def test_login():
    print("login done")

@pytest.mark.smoke
def test_login1():
    print("login done")

@pytest.mark.smoke
def test_login2():
    print("login done")

@pytest.mark.smoke
def test_login3():
    print("login done")

@pytest.mark.smoke
def test_login4():
    print("login done")


@pytest.mark.regression
def test_addProducts():
    print("Add products")

@pytest.mark.regression
def test_logout():
    print("logout done")

@pytest.mark.regression
def test_logout1():
    print("logout done")

@pytest.mark.regression
def test_logout2():
    print("logout done")

@pytest.mark.regression
def test_logout3():
    print("logout done")
