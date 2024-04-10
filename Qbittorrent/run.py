from qbittorrentapi import Client


class QbDownloader:
    def __init__(self):
        print("qbittorrent start run")
        self._client: Client = Client(
            host='localhost',
            port=9000,
            username='admin',
            password='adminadmin',
        )

    def logout(self):
        print("qbittorrent logout")
        self._client.auth_log_out()

