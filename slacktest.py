import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

def send_slack_message_with_file(channel, file_path, initial_comment):
    """
    Slackにファイルを添付してメッセージを送信する関数

    Args:
        channel (str): 送信先のチャンネル名またはID
        file_path (str): 添付するファイルのパス
        initial_comment (str): メッセージの初期コメント
    """
    client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

    try:
        response = client.files_upload_v2(
            channel=channel,
            initial_comment=initial_comment,
            file=file_path,
        )
        print(f"ファイルアップロード成功: {response['file']['name']}")
    except SlackApiError as e:
        print(f"ファイルアップロード失敗: {e}")

if __name__ == "__main__":
    # 設定
    channel = os.getenv("SLACK_CHANNEL_ID")
    file_path = "/workspaces/langchain/work/google-api.zip"  # 添付するzipファイルのパスを設定
    initial_comment = "zipファイルを添付します。" # メッセージの初期コメントを設定

    # ファイルの存在確認
    if not os.path.exists(file_path):
        print(f"エラー: ファイルが見つかりません: {file_path}")
    else:
        send_slack_message_with_file(channel, file_path, initial_comment, slack_token)