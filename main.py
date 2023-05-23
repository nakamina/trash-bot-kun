import argparse
import datetime
import os
from typing import Optional

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


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
        word = args.monday
    elif day_of_week == 1:
        word = args.tuesday
    elif day_of_week == 2:
        word = args.wednesday
    elif day_of_week == 3:
        word = args.thursday
    elif day_of_week == 4:
        word = args.friday
    elif day_of_week == 5:
        word = args.saturday
    elif day_of_week == 6:
        word = args.sunday
    else:
        raise ValueError("存在しない曜日が指定されています")

    client = WebClient(token=os.environ["TRASH_BOT_KUN_SLACK_API"])

    try:
        response = client.chat_postMessage(channel="#test-trash-bot-kun", text=word)
        assert response["message"]["text"] == word
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error:{e.response['error']}")


if __name__ == "__main__":
    main()
