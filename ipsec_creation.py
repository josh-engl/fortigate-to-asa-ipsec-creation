def get_user_input():
    user_input = {"phase1name": input("Interface name\n"),
                  "proposal": input("Proposal(s) - if more than one, separate with spaces\n").lower(),
                  "pfs": input("Is PFS enabled? (Y)es or (N)o\n").lower(),
                  "dhgrp": input("DH group(s) - if more than one, separate with spaces\n"),
                  "keylifeseconds": input("Key life in seconds\n"),
                  "src-name": input("Source IP name(s) - if more than one, separate with spaces\n").split(),
                  "dst-name": input("Destination IP name(s) - if more than one, separate with spaces\n").split()}
    return user_input


def create_phase2_selectors(user_input):

    def generate_config():
        if num_of_src_subnets > 1:
            print(f"edit {dst_name}-{counter}")
        else:
            print(f"edit {dst_name}")
        print(f"set phase1name {user_input.get('phase1name')}")
        print(f"set proposal {user_input.get('proposal')}")
        if user_input.get("pfs") == "y" or "yes":
            print(f"set pfs enable")
            print(f"set dhgrp {user_input.get('dhgrp')}")
        else:
            print(f"set pfs disable")
        print(f"set src-addr-type name")
        print(f"set dst-addr-type name")
        print(f"set src-name {src_name}")
        print(f"set dst-name {dst_name}")
        print("next")

    num_of_src_subnets = len(user_input.get("src-name"))

    print("config vpn ipsec phase2-interface")

    for dst_name in user_input.get("dst-name"):
        counter = 1
        for src_name in user_input.get("src-name"):
            generate_config()
            counter += 1

    print("end")


create_phase2_selectors(get_user_input())
