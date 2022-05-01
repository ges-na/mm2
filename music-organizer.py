import datetime
import ipdb
import os
from shutil import copy2

class MusicMachine:

    def __init__(self):
        self.input_directory = None
        self.output_directory = None
        self.settings = {}
        self.keep_going = True

    @property
    def current_datetime_formatted(self):
        return datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")

    def start(self):
        input('''
            \n
            Welcome to Music Machine! Please press Enter to begin.
            \n''')
        self.set_input_directory()
        print("\n")
        self.set_output_directory()

    def render_menu(self):
        menu_choice = input(f'''\n
        _________________________________________________________\n
        Please choose a number.
            1. Change input directory. Current input directory = {self.input_directory}
            2. Change output directory. Current output directory = {self.output_directory}
            3. Set additional optional settings. Selections: {self.settings}
            4. Dry run.
            5. Start!
            6. Quit.
        Choice: ''')
        print('''        ________________________________________________________\n
        ''')
        if menu_choice == "1":
            self.set_input_directory()
        elif menu_choice == "2":
            self.set_output_directory()
        elif menu_choice == "3":
            print("  not implemented yet sorry")
        elif menu_choice == "4":
            print(f"Starting Music Machine dry run at {self.current_datetime_formatted}.")
            self.start_music_machine(dry_run=True)
        elif menu_choice == "5":
            print(f"Starting Music Machine run at {self.current_datetime_formatted}.")
            self.start_music_machine(dry_run=False)
        elif menu_choice == "6":
            self.keep_going = False

    def set_input_directory(self):
        print("  Music Machine assumes that your top-level directory generally contains artist sub-directories containing album subdirectories containing tracks.\n")
        self.input_directory = input("  Please choose your input directory--this is where you want to copy files from: ")
        self.check_input_dir(self.input_directory)

    def set_output_directory(self):
        self.output_directory = input("  Please choose your output directory. This is where you want to copy files to: ")
        self.check_output_dir(self.output_directory)

    def check_input_dir(self, directory):
        if os.path.isdir(self.input_directory):
            print(f"  Directory {self.input_directory} set as input directory.")
        else:
            print(f"  Directory {self.input_directory} does not exist, please try again.")
            self.set_input_directory()

    def check_output_dir(self, directory):
        if os.path.isdir(self.output_directory):
            print(f"  Directory {self.output_directory} set as output directory.")
        else:
            dir_creation_choice = input(f"  Directory {self.output_directory} does not exist. Create [y] or go back [N]? ").lower()
            if dir_creation_choice not in ["y", "yes"]:
                self.output_directory = None
                print(f"Output directory not set.")
            else:
                self.create_dir(self.output_directory)

    def create_dir(self, path):
        try:
            # This needs a sanity check
            os.makedirs(path, exist_ok=False)
            print(f"  Directory {self.output_directory} created and set as output directory.")
        except FileExistsError:
            print(f"  Specified output directory {self.output_directory} already exists!")

    def select_settings(self):
        # TODO: possible settings
        ## bespoke filename formatting
        ## filetypes to bother with
        ## what to do with VA albums?
        ## logging/verbosity
        ## settings for diffing
        pass

    def start_music_machine(self, dry_run=True):
        # TODO: this will traverse directory structure and instantiate File/Track
        folder_contents = [x for x in os.walk(self.input_directory)]
        print(folder_contents)
            # root = os.path.relpath(top_folder, self.input_directory)
            # split_root = root.split(os.sep)
            # array_length = len(split_root)
            # # This deals with presumable artist/album formatted stuff; this is very hacky
            # if array_length == 2:
            #     print(f"working on {top_folder}")
            #     for filename in tracks:
            #         file_instance = File()
            #         file_instance.handle_file(filename)

            # # Plenty of artist folders just have tracks in them. Need to figure out how to get album name, if possible, or at least copy and flag.
        # # Need to account for dry_run True/False
        # print("Music Machine would start if it were written.")

    def logging(self):
        # idk how logging works
        pass


class File:

    def handle_file(self, filename):
        print(f"handling {filename}")

    def check_filetype(self):
        pass

    def diff_file(self):
        pass

    def check_parent_dir(self):
        pass

    def copy_file(self):
        pass


class Track(File):

    def diff_file(self):
        # track-specific diff logic?
        pass


music_machine = MusicMachine()
music_machine.start()
while music_machine.keep_going:
    music_machine.render_menu()
