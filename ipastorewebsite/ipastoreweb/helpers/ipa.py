__author__ = 'mertsalik'
import biplist
import plistlib
import tempfile
import shutil
import os
import zipfile
import traceback

IPA_FOLDER = os.path.join(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "static")


class IpaReader:
    def __init__(self, ipa_path):
        self.ipa_path = ipa_path
        self.plist_path = "Payload/{}/Info.plist"
        self.info_plist = self.__read()

    def __find_app_name(self, ipa_payload_path):
        app_name = ""
        for filename in os.listdir(os.path.join(ipa_payload_path, "Payload")):
            if filename.endswith(".app"):
                app_name = filename
        if app_name == "":
            raise Exception("Can't find app folder in extracted ipa folder!")
        return app_name

    def __unzip(self, source, destination):
        with zipfile.ZipFile(source, "r") as z:
            z.extractall(destination)

    def __read_binary_plist(self, source):
        return biplist.readPlist(source)

    def __read(self):
        temporary_path = tempfile.mkdtemp()
        pl = None
        try:
            self.__unzip(self.ipa_path, temporary_path)
            self.plist_path = self.plist_path.format(
                self.__find_app_name(temporary_path))
            pl = biplist.readPlist(
                os.path.join(temporary_path, self.plist_path))
        except Exception as e:
            print e.message
            traceback.print_exc()
        shutil.rmtree(temporary_path)
        return pl

    def get_ipa_properties(self):
        return {
            "app_version": self.info_plist['CFBundleShortVersionString'],
            "name": self.info_plist['CFBundleIdentifier'],
            "CFBundleIdentifier": self.info_plist['CFBundleIdentifier'],
            "CFBundleVersion": self.info_plist['CFBundleVersion'],
            "CFBundleName": self.info_plist['CFBundleName']
        }


class PlistWriter:
    """
    ipa_path : original ipa path
    """

    def __init__(self, ipa_path, plist_obj, download_url):
        self.ipa_path = ipa_path
        head, ipa_filename = os.path.split(ipa_path)
        self.ipa_filename = ipa_filename
        self.plist_obj = plist_obj
        self.download_url = download_url

    def write(self):
        upload_info = {
            "kind": "software-package",
            "url": "{}/{}".format(self.download_url, self.ipa_filename)
        }
        assets = [upload_info]
        ipa_info = {
            "bundle-identifier": self.plist_obj["CFBundleIdentifier"],
            "bundle-version": self.plist_obj["CFBundleVersion"],
            "kind": "software",
            "title": self.plist_obj["CFBundleName"]
        }
        items_array = [{'assets': assets, 'metadata': ipa_info}]
        plist_dict = {'items': items_array}
        plist_path = os.path.join(IPA_FOLDER,
                                  "{}.plist".format(self.ipa_filename))
        plistlib.writePlist(plist_dict, plist_path)


if __name__ == "__main__":
    uploaded_ipa_path = "/Users/mertsalik/Documents/SofyoDigital/ipa-store/ipastorewebsite/static/2A977A.ipa"
    reader = IpaReader(uploaded_ipa_path)
    prop = reader.get_ipa_properties()
    try:
        pw = PlistWriter(uploaded_ipa_path, prop)
        pw.write()
    except Exception as e:
        print e.message
        traceback.print_exc()
