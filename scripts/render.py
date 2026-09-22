#!/usr/bin/env python3
"""兼容入口：python3 scripts/render.py "<主名>" -> opp-radar render <主名>。
逻辑在 opp_radar/render.py，本文件只做参数转发，无需 pip install。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.argv = ["opp-radar", "render"] + sys.argv[1:]

from opp_radar.cli import main  # noqa: E402

raise SystemExit(main())
