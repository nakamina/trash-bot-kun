import argparse
import os
import pathlib
from typing import Optional


def parse_args(prog: Optional[str] = None) -> argparse.Namespace:
    # パーサの作成
    parser = argparse.ArgumentParser(
        prog=prog,
        description="Trash bot app",
    )

    # オプションを追加
    parser.add_argument(
        "--monday",
        required=True,
        type=str,
        help="月曜日のゴミ収集種別",
    )
    parser.add_argument(
        "--tuesday",
        required=True,
        type=str,
        help="火曜日のゴミ収集種別",
    )
    parser.add_argument(
        "--wednesday",
        required=True,
        type=str,
        help="水曜日のゴミ収集種別",
    )
    parser.add_argument(
        "--thursday",
        required=True,
        type=str,
        help="木曜日のゴミ収集種別",
    )
    parser.add_argument(
        "--friday",
        required=True,
        type=str,
        help="金曜日のゴミ収集種別",
    )
    parser.add_argument(
        "--saturday",
        type=str,
        default="ゴミ収集の予定なし",
        help="土曜日のゴミ収集種別",
    )
    parser.add_argument(
        "--sunday",
        type=str,
        default="ゴミ収集の予定なし",
        help="日曜日のゴミ収集種別",
    )

    return parser.parse_args()


def main(prog: Optional[str] = None):
    args = parse_args(prog=prog)
    print(
        args.monday,
        args.tuesday,
        args.wednesday,
        args.thursday,
        args.friday,
        args.saturday,
        args.sunday,
    )


if __name__ == "__main__":
    main()
