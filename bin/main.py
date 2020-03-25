#!/usr/bin/env python3
import asyncio
import os
from pathlib import Path
import scandir

home = str(Path.home())


async def find_directory_by_end_of_file_path(end_of_path):
    separated_end_of_path = os.path.join(end_of_path)
    for root, dirs, files in scandir.walk(home):
        if "/." in root:
            continue
        for f in files:
            file_path = (root + "/" + f).replace("/", os.sep)
            try:
                if file_path.endswith(separated_end_of_path):
                    return (os.path.join(root)).replace("/", os.sep)
            except UnicodeEncodeError:
                continue
                # encoded_file_path = file_path.encode('utf-8', 'surrogateescape').decode('ISO-8859-1')
                # if encoded_file_path.endswith(separated_end_of_path):
                #     return replace_separator(os.path.join(root))

    raise FileNotFoundError


async def connect_to_vpn():
    # await asyncio.create_subprocess_shell("sudo killall openvpn",
    #                                       cwd=home,
    #                                       stdin=None,
    #                                       stdout=open(os.devnull, 'wb'),
    #                                       stderr=open(os.devnull, 'wb'),
    #                                       close_fds=True)

    print("Helper: Connecting to VPN...")
    await asyncio.create_subprocess_shell("sudo openvpn --config client.ovpn",
                                          cwd=home,
                                          stdin=None,
                                          stdout=open(os.devnull, 'wb'),
                                          stderr=open(os.devnull, 'wb'),
                                          close_fds=True)


async def run_selenoid():
    print("Helper: Running Selenoid...")
    await asyncio.create_subprocess_shell('./selenoid -container-network bridge1',
                                          shell=True,
                                          cwd=await find_directory_by_end_of_file_path("selenoid"),
                                          stdin=None,
                                          stdout=open(os.devnull, 'wb'),
                                          stderr=open(os.devnull, 'wb'),
                                          close_fds=True)


async def open_browser():
    print("Helper: Opening Browser...")
    await asyncio.create_subprocess_shell("xdg-open https://bpm-qa-01.baexperiment.com/",
                                          shell=True,
                                          stdin=None,
                                          stdout=open(os.devnull, 'wb'),
                                          stderr=open(os.devnull, 'wb'),
                                          close_fds=True)

    await asyncio.create_subprocess_shell("xdg-open https://jenkins-01.baexperiment.com/",
                                          shell=True,
                                          stdin=None,
                                          stdout=open(os.devnull, 'wb'),
                                          stderr=open(os.devnull, 'wb'),
                                          close_fds=True)


async def open_idea():
    print("Helper: Opening Idea...")
    await asyncio.create_subprocess_shell("./idea.sh",
                                          shell=True,
                                          cwd=await find_directory_by_end_of_file_path("/bin/idea.sh"),
                                          stdin=None,
                                          stdout=open(os.devnull, 'wb'),
                                          stderr=open(os.devnull, 'wb'),
                                          close_fds=True)


async def open_hubstaff():
    print("Helper: Opening Hubstaff...")
    await asyncio.create_subprocess_shell("./HubstaffClient.bin.x86_64",
                                          shell=True,
                                          cwd=await find_directory_by_end_of_file_path(
                                              "HubstaffClient.bin.x86_64"),
                                          stdin=None,
                                          stdout=open(os.devnull, 'wb'),
                                          stderr=open(os.devnull, 'wb'),
                                          close_fds=True)


async def open_slack():
    print("Helper: Opening Slack...")
    await asyncio.create_subprocess_shell("slack",
                                          shell=True,
                                          cwd=home,
                                          stdin=None,
                                          stdout=open(os.devnull, 'wb'),
                                          stderr=open(os.devnull, 'wb'),
                                          close_fds=True)


async def open_file_manager():
    print("Helper: Opening File Manager...")
    await asyncio.create_subprocess_shell("nautilus %s" % home,
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

loop = asyncio.get_event_loop()
tasks = []

if '1' in input_string:
    tasks.append(asyncio.ensure_future(connect_to_vpn()))

if '2' in input_string:
    tasks.append(asyncio.ensure_future(run_selenoid()))

if '3' in input_string:
    tasks.append(asyncio.ensure_future(open_browser()))

if '4' in input_string:
    tasks.append(asyncio.ensure_future(open_idea()))

if '5' in input_string:
    tasks.append(asyncio.ensure_future(open_hubstaff()))

if '6' in input_string:
    tasks.append(asyncio.ensure_future(open_slack()))

if '7' in input_string:
    tasks.append(asyncio.ensure_future(open_file_manager()))

loop.run_until_complete(asyncio.wait(tasks))
