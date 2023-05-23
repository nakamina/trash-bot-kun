import argparse
import datetime
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
    today = datetime.date.today()
    day_of_week = today.weekday()

    if day_of_week == 0:
        print(args.monday)
    elif day_of_week == 1:
        print(args.tuesday)
    elif day_of_week == 2:
        print(args.wednesday)
    elif day_of_week == 3:
        print(args.thursday)
    elif day_of_week == 4:
        print(args.friday)
    elif day_of_week == 5:
        print(args.saturday)
    elif day_of_week == 6:
        print(args.sunday)


if __name__ == "__main__":
    main()
