__author__ = 'mertsalik'
import biplist
import tempfile
import shutil
import os
import zipfile
import traceback


class IpaReader:
    def __init__(self, ipa_path, app_name):
        self.ipa_path = ipa_path
        self.app_name = app_name
        self.plist_path = "Payload/{}/Info.plist".format(app_name)
        self.info_plist = self.__read()

    def __unzip(self, source, destination):
        print "unzipping ..."
        with zipfile.ZipFile(source, "r") as z:
            z.extractall(destination)

    def __read_binary_plist(self, source):
        print "reading plist ..."
        return biplist.readPlist(source)

    def __read(self):
        temporary_path = tempfile.mkdtemp()
        pl = None
        try:
            self.__unzip(self.ipa_path, temporary_path)
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
            "name": self.info_plist['CFBundleIdentifier']
        }


if __name__ == "__main__":
    reader = IpaReader(
        "/Users/mertsalik/Documents/SofyoDigital/ipa-store/ipastorewebsite/static/2A977A.ipa",
        "Kutumubu.app")
    print reader.get_ipa_properties()
