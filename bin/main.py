#!/usr/bin/env python3
import os
import subprocess
import time
from pathlib import Path

home = str(Path.home())


def find_directory_by_end_of_file_path(end_of_path):
    separated_end_of_path = os.path.join(end_of_path)

    for root, dirs, files in os.walk(home):
        if "/." in root:
            continue
        for f in files:
            file_path = root + "/" + f
            try:
                if file_path.endswith(separated_end_of_path):
                    return replace_separator(os.path.join(root))
            except UnicodeEncodeError:
                encoded_file_path = file_path.encode('utf-8', 'surrogateescape').decode('ISO-8859-1')
                if encoded_file_path.endswith(separated_end_of_path):
                    return replace_separator(os.path.join(root))

    raise FileNotFoundError


def replace_separator(path):
    return path.replace("/", os.sep)


def connect_to_vpn():
    subprocess.Popen(['sudo', 'killall', 'openvpn'],
                     cwd=home,
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True).wait(3.0)

    print("Helper: Connecting to VPN...")
    subprocess.Popen(['sudo', 'openvpn', '--config', 'client.ovpn'],
                     cwd=home,
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def run_selenoid():
    print("Helper: Running Selenoid...")
    subprocess.Popen(['./selenoid -container-network bridge1'],
                     shell=True,
                     cwd=find_directory_by_end_of_file_path("selenoid"),
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def open_browser():
    print("Helper: Opening Browser...")
    subprocess.Popen(["xdg-open https://bpm-qa-01.baexperiment.com/"],
                     shell=True,
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)
    subprocess.Popen(["xdg-open https://jenkins-01.baexperiment.com/"],
                     shell=True,
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def open_idea():
    print("Helper: Opening Idea...")
    subprocess.Popen(["./idea.sh"],
                     shell=True,
                     cwd=find_directory_by_end_of_file_path("/bin/idea.sh"),
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def open_hubstaff():
    print("Helper: Opening Hubstaff...")
    subprocess.Popen(["./HubstaffClient.bin.x86_64"],
                     shell=True,
                     cwd=find_directory_by_end_of_file_path("HubstaffClient.bin.x86_64"),
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def open_slack():
    print("Helper: Opening Slack...")
    subprocess.Popen(["slack"],
                     shell=True,
                     cwd=home,
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def open_file_manager():
    print("Helper: Opening File Manager...")
    subprocess.Popen(["nautilus %s" % home],
                     shell=True,
                     cwd=home,
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def welcome():
    print("\nWelcome to helper!\n")


welcome()
input_string = input("Enter the numbers corresponding to the items:\n"
                     "Example: '341'\n\n"
                     "1 - Connect to VPN\n"
                     "2 - Run Selenoid\n"
                     "3 - Open Browser\n"
                     "4 - Open Idea\n"
                     "5 - Open Hubstaff\n"
                     "6 - Open Slack\n"
                     "7 - Open File Manager\n\n")

if '1' in input_string:
    connect_to_vpn()

if '2' in input_string:
    run_selenoid()

if '3' in input_string:
    open_browser()

if '4' in input_string:
    open_idea()

if '5' in input_string:
    open_hubstaff()

if '6' in input_string:
    open_slack()

if '7' in input_string:
    open_file_manager()
