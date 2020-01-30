#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import dropbox
import sys


class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(access_token)

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        with open(file_from, 'rb') as f:
            self.dbx.files_upload(f.read(), file_to)

    def get_shared_link(self, file_to):
        """return link of uploaded file by path
        """
        link = self.dbx.sharing_create_shared_link(file_to, short_url=True)
        return parse_response_string(str(link))


def parse_response_string(string):
    import re
    _str = re.search("(https:[a-zA-Z./0-9-_]*)", string)
    return _str.group()

def get_image_name():
    _image_name = sys.argv[1]
    return str(_image_name)

def main():
    _access_token = 'drop_box access token'
    transferData = TransferData(_access_token)

    _image_name = get_image_name()
    file_from = '/home/username/whole_path_to_the_directory/screen_shooter/screenshots/{}'.format(_image_name)
    file_to = '/screenshots/{}'.format(_image_name)  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print(transferData.get_shared_link(file_to))


if __name__ == '__main__':
    main()
