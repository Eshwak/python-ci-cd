import pytest
from app import main

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from DevOps CI/CD demo!" in captured.out
