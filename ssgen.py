import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl


class ShadowsocksConfigGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shadowsocks Config Generator")
        self.layout = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.server_label = QLabel("Server:")
        self.server_edit = QLineEdit()
        self.layout.addWidget(self.server_label)
        self.layout.addWidget(self.server_edit)

        self.port_label = QLabel("Server Port:")
        self.port_edit = QLineEdit()
        self.layout.addWidget(self.port_label)
        self.layout.addWidget(self.port_edit)

        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_edit)

        self.timeout_label = QLabel("Timeout:")
        self.timeout_edit = QLineEdit()
        self.timeout_edit.setText("300")  # Default value
        self.layout.addWidget(self.timeout_label)
        self.layout.addWidget(self.timeout_edit)

        self.method_label = QLabel("Method:")
        self.method_edit = QLineEdit()
        self.method_edit.setText("chacha20-ietf-poly1305")  # Default value
        self.layout.addWidget(self.method_label)
        self.layout.addWidget(self.method_edit)

        self.mode_label = QLabel("Mode:")
        self.mode_edit = QLineEdit()
        self.mode_edit.setText("tcp_only")  # Default value
        self.layout.addWidget(self.mode_label)
        self.layout.addWidget(self.mode_edit)

        self.dns_label = QLabel("DNS:")
        self.dns_edit = QLineEdit()
        self.dns_edit.setText("1.1.1.1")  # Default value
        self.layout.addWidget(self.dns_label)
        self.layout.addWidget(self.dns_edit)

        self.plugin_label = QLabel("Plugin:")
        self.plugin_edit = QLineEdit()
        self.plugin_edit.setText("obfs-server")  # Default value
        self.layout.addWidget(self.plugin_label)
        self.layout.addWidget(self.plugin_edit)

        self.plugin_opts_label = QLabel("Plugin Options:")
        self.plugin_opts_edit = QLineEdit()
        self.plugin_opts_edit.setText("obfs=http;obfs-host=cloudfront.net")  # Default value
        self.layout.addWidget(self.plugin_opts_label)
        self.layout.addWidget(self.plugin_opts_edit)

        self.fast_open_label = QLabel("Fast Open:")
        self.fast_open_edit = QLineEdit()
        self.fast_open_edit.setText("false")  # Default value
        self.layout.addWidget(self.fast_open_label)
        self.layout.addWidget(self.fast_open_edit)

        self.create_button = QPushButton("Create Config")
        self.create_button.clicked.connect(self.create_config)
        self.layout.addWidget(self.create_button)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.open_github_repo)
        self.layout.addWidget(self.about_button)

        self.setLayout(self.layout)

    def create_config(self):
        data = {
            "server": self.server_edit.text(),
            "server_port": int(self.port_edit.text()),
            "password": self.password_edit.text(),
            "timeout": int(self.timeout_edit.text()),
            "method": self.method_edit.text(),
            "mode": self.mode_edit.text(),
            "dns": self.dns_edit.text(),
            "plugin": self.plugin_edit.text(),
            "plugin_opts": self.plugin_opts_edit.text(),
            "fast_open": self.fast_open_edit.text().lower() == "true",
        }

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save Config File", "", "JSON Files (*.json)")

        if file_path:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)

            success_message = f"Config file created successfully!\n\nFile Location: {file_path}"
            QMessageBox.information(self, "Success", success_message, QMessageBox.Ok)

            open_button = QMessageBox.addButton(QMessageBox.Open)
            open_button.clicked.connect(lambda: self.open_file(file_path))

    def open_file(self, file_path):
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

    def open_github_repo(self):
        url = QUrl("https://github.com/mfat/ssgen")
        QDesktopServices.openUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShadowsocksConfigGenerator()
    window.show()
    sys.exit(app.exec_())
