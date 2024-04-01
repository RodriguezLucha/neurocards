def test_simple(request):
    print(request.config.getoption("--name"))
