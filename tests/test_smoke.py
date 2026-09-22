def test_import_package():
    import opp_radar
    assert opp_radar.__version__


def test_cli_help():
    from opp_radar.cli import main
    import sys
    argv = sys.argv
    try:
        sys.argv = ["opp-radar", "--help"]
        try:
            main()
        except SystemExit as e:
            assert e.code == 0
    finally:
        sys.argv = argv
