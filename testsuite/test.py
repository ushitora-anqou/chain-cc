
import os
import subprocess


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def run_resulting_binary(executable_path: str, stdin: str = None, stdout_path: str = "tmp_run_stdout.txt"):
    f = open(stdout_path, "w")
    if stdin == None:
        return subprocess.call([executable_path], stdout=f)
    else:
        return subprocess.call([executable_path, stdin], stdout=f)


class Checker:
    def __init__(self, script: str = None):
        if script is None:
            script = os.getenv("SCRIPT")
            if script is None:
                raise RuntimeError("Environmental variable SCRIPT is not set")
        self.script = script

        self.r = {
            "check": {
                "correct": 0,
                "wrong": 0,
                "compile error": 0,
            },
            "check_and_link_with": {
                "correct": 0,
                "wrong": 0,
                "compile error": 0,
            },
            "should_not_compile": {
                "wrong": 0,
                "correct": 0,
            },
        }
        
    def dump_result(self):
        l = [
            self.r["check"]["correct"],
            self.r["check"]["wrong"],
            self.r["check"]["compile error"],
            self.r["check_and_link_with"]["correct"],
            self.r["check_and_link_with"]["wrong"],
            self.r["check_and_link_with"]["compile error"],
            self.r["should_not_compile"]["wrong"],
            self.r["should_not_compile"]["correct"],
        ]
        print(",".join(map(lambda x: str(x), l)))


    def _compile(self, input: str):
        with open("tmp.c", "w") as f:
            f.write(input)

        ret = subprocess.call([f"./{self.script}", "tmp.c", "tmp.s"])
        return ret

    def check(self, input: str, expected: int, stdin: str = None, expected_stdout: str = None):
        if self._compile(input) != 0:
            self.r["check"]["compile error"] += 1
            self.dump_result()
            return

        os.system("cc -o tmp tmp.s -static")
        returned_value = run_resulting_binary("./tmp", stdin)
        actual_stdout = open("tmp_run_stdout.txt", "r").read()

        if expected == returned_value and (expected_stdout is None or actual_stdout == expected_stdout):
            self.r["check"]["correct"] += 1
        else:
            self.r["check"]["wrong"] += 1
        self.dump_result()

    def check_and_link_with(self, input: str, linked_lib: str, expected: int, expected_stdout: str = None):
        if self._compile(input) != 0:
            self.r["check_and_link_with"]["compile error"] += 1
            self.dump_result()
            return

        lib_file = open("libtest.c", "w")
        lib_file.write(linked_lib)
        lib_file.close()
        os.system("cc -S -o libtest.s libtest.c")
        os.system("cc -o tmp tmp.s libtest.s -static")
        os.system("rm libtest.c libtest.s")
        returned_value = run_resulting_binary("./tmp")
        actual_stdout = open("tmp_run_stdout.txt", "r").read()

        if expected == returned_value and (expected_stdout is None or actual_stdout == expected_stdout):
            self.r["check_and_link_with"]["correct"] += 1
        else:
            self.r["check_and_link_with"]["wrong"] += 1
        self.dump_result()

    def should_not_compile(self, input: str, expected_errmsg: str = None):
        if self._compile(input) == 0:
            self.r["should_not_compile"]["wrong"] += 1
            return
        else:
            self.r["should_not_compile"]["correct"] += 1
            return
        self.dump_result()