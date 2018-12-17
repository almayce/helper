#!/usr/bin/env python3
import os
import subprocess
import time
from pathlib import Path
home = str(Path.home())


def vpn():
    print("Helper: Connecting to VPN...")
    subprocess.Popen(['sudo', 'killall', 'openvpn'],
                     cwd=home,
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)
    time.sleep(4)
    subprocess.Popen(['sudo', 'openvpn', '--config', 'client.ovpn'],
                     cwd=home,
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def selenoid(project):
    print("Helper: Running Selenoid...")
    subprocess.Popen(['./selenoid -container-network bridge1'],
                     shell=True,
                     cwd=home + "/IdeaProjects/%s" % project,
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
    subprocess.Popen(["xdg-open http://jenkins-01.baexperiment.com/job/BPM%20UI%20Test%20Automation/"],
                     shell=True,
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def open_idea():
    print("Helper: Opening Idea...")
    subprocess.Popen(["./idea.sh"],
                     shell=True,
                     cwd=home + "/ideaIC-2018.1.3/idea-IC-181.4892.42/bin",
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


# todo filefinder


def hubstaff():
    print("Helper: Opening Hubstaff...")
    subprocess.Popen(["./HubstaffClient.bin.x86_64"],
                     shell=True,
                     cwd=home + "/Hubstaff/1.4.2/Hubstaff",
                     stdin=None,
                     stdout=open(os.devnull, 'wb'),
                     stderr=open(os.devnull, 'wb'),
                     close_fds=True)


def welcome():
    print("Welcome to helper\n")


welcome()
input_string = input("Enter the characters corresponding to the items:\n"
                     "Example: 'vsi'\n\n"
                     "v - Connect to VPN\n"
                     "s - Run Selenoid\n"
                     "b - Open Browser\n"
                     "i - Open Idea\n"
                     "h - Hubstaff\n\n")

if 'v' in input_string:
    vpn()

if 's' in input_string:
    selenoid("bpm-automation-testing-master")

if 'b' in input_string:
    open_browser()

if 'i' in input_string:
    open_idea()

if 'h' in input_string:
    hubstaff()
