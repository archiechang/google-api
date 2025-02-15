import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import zipfile
import pyAesCrypt

bufferSize = 64 * 1024  # バッファサイズをグローバル変数として定義
def send_slack_message_with_file(channel, file_path, initial_comment):
    """
    Slackにファイルを添付してメッセージを送信する関数

    Args:
        channel (str): 送信先のチャンネル名またはID
        file_path (str): 添付するファイルのパス
        initial_comment (str): メッセージの初期コメント
    """
    client = WebClient(token="")

    try:
        response = client.files_upload_v2(
            channel=channel,
            initial_comment=initial_comment,
            file=file_path,
        )
        print(f"ファイルアップロード成功: {response['file']['name']}")
    except SlackApiError as e:
        print(f"ファイルアップロード失敗: {e}")

def encrypt_zip_file(file_path, encrypted_file_path, password):
    """
    ZipファイルをpyAesCryptで暗号化する関数

    Args:
        file_path (str): 暗号化対象のZipファイルのパス
        encrypted_file_path (str): 暗号化後のZipファイルの保存パス
        password (str): 暗号化パスワード
    """
    try:
        pyAesCrypt.encryptFile(file_path, encrypted_file_path, password, bufferSize)
        print(f"ファイル暗号化成功: {encrypted_file_path}")
    except Exception as e:
        print(f"ファイル暗号化失敗: {e}")

def decrypt_zip_file(encrypted_file_path, decrypted_file_path, password):
    """
    pyAesCryptで暗号化されたZipファイルを複合化する関数

    Args:
        encrypted_file_path (str): 暗号化されたZipファイルのパス
        decrypted_file_path (str): 複合化後のZipファイルの保存パス
        password (str): 複合化パスワード
    """
    try:
        pyAesCrypt.decryptFile(encrypted_file_path, decrypted_file_path, password, bufferSize)
        print(f"ファイル複合化成功: {decrypted_file_path}")
    except Exception as e:
        print(f"ファイル複合化失敗: {e}")



if __name__ == "__main__":
    # 設定
    channel = "C087KSH186L"
    file_path = "/workspaces/google-api/work/google-api.zip"  # 添付するzipファイルのパスを設定
    initial_comment = "zipファイルを添付します。" # メッセージの初期コメントを設定
    password = "ch@ngru0b1n" # ZIP暗号化パスワード
    encrypted_file_path = "/workspaces/google-api/work/google-api_encrypted.zip" # 暗号化後zipファイルパス
    decrypted_file_path = "/workspaces/google-api/work/google-api_decrypted.zip" # 複合化後zipファイルパス
    # # ファイルの存在確認
    # if not os.path.exists(file_path):
    #     print(f"エラー: ファイルが見つかりません: {file_path}")
    # else:
    #     # ZIP暗号化
    #     encrypt_zip_file(file_path, encrypted_file_path, password)

    #     send_slack_message_with_file(channel, encrypted_file_path, initial_comment)



    # ZIP複合化 (必要に応じて)
    decrypt_zip_file(encrypted_file_path, decrypted_file_path, password)