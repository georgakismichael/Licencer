import sys
import netifaces
import hashlib
import time
import base64
from Crypto import Random
from Crypto.Cipher import AES
import math
import string
import fileinput
from datetime import datetime

licence_expiration = '2017-07-22 21:00:00'  # Format YYYY-MM-DD HOUR:MIN:SEC (HOUR in 24h format)
licence_usage = '10'                        # Always positive
licence_usage_start = '0'                   # Always ZERO!!

default_licfile = 'cfg.dat'
default_logfile = 'log.log'

BLOCK_SZ = 16
pad = lambda s: s + (BLOCK_SZ - len(s) % BLOCK_SZ) * chr(BLOCK_SZ - len(s) % BLOCK_SZ)
unpad = lambda s : s[0:-ord(s[-1])]

def range_bytes (): return range(256)
def range_printable(): return (ord(c) for c in string.printable)
def entropy(data, iterator=range_bytes):
    if not data:
        return 0
    entropy = 0
    for x in iterator():
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

def get_macs(exhaustive = True):
    mac_lst = []
    iface_lst = netifaces.interfaces()
    for entry in iface_lst:
        info = netifaces.ifaddresses(entry)[netifaces.AF_LINK]
        info_str = str(info)
        mac = info_str.split('\'')[3]
        if exhaustive:
            mac_lst.append(mac) # do not skip empty or invalid macs if exhaustive
        else:
            if not ((mac == '00:00:00:00:00:00:00:e0') or (len(mac) == 0)):
                mac_lst.append(mac)
    return mac_lst
    
def get_key(seed):
    hash_object = hashlib.sha256(seed)  # generate SHA256 checksum - Validate it here http://www.xorbin.com/tools/sha256-hash-calculator
    hex_dig_64 = hash_object.hexdigest()
    hex_dig_32 = ''.join([chr(int(hex_dig_64[i:i+2], 16)) for i in range(0, len(hex_dig_64), 2)])
    return hex_dig_32    
    
def encrypt(key, raw):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)          #AES CBC selected
    return base64.b64encode(iv + cipher.encrypt(raw))

def decrypt(key, enc):
    enc = base64.b64decode(enc)
    iv = enc[:BLOCK_SZ]
    cipher = AES.new(key, AES.MODE_CBC, iv)          #AES CBC selected
    return unpad(cipher.decrypt( enc[BLOCK_SZ:]))
    
def get_best_key(lst):
    curr_entropy = 0        # invalid value    
    max_entropy = 0         # invalid value    
    seed_str = ''

    for mac in lst:
        seed_str += str(mac)
        key_tmp = get_key(seed_str)
        curr_entropy = float(entropy(key_tmp, range_printable))
        if (curr_entropy > max_entropy):
            ret_key = key_tmp
            max_entropy = curr_entropy
            #print max_entropy
    return ret_key
    
def log_to_file(logline, echo = True, filename = default_logfile):
    try:
        fp = open(filename, 'a+')
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        return False
    except:
        print "Unexpected error:", sys.exc_info()[0]
        return False
    entry = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': ' + str(logline)
    fp.write(entry + '\n')
    if echo:
        print entry
    fp.close()
    return True

def write_to_file(line, filename):
    try:
        fp = open(filename, 'a+')
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        return False
    except:
        print "Unexpected error:", sys.exc_info()[0]
        return False
    entry = str(line)
    fp.write(entry + '\n')
    fp.close()
    return True
    
def file_erase(filename):
    try:
        fp = open(filename, 'w+')
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        return False
    except:
        print "Unexpected error:", sys.exc_info()[0]
        return False
    fp.close()
    return True
    
def file_read(filename):
    ret = []
    try:
        fp = open(filename, 'r+')
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        return False
    except:
        print "Unexpected error:", sys.exc_info()[0]
        return False
    ret = fp.readlines()
    ret = [line.strip() for line in ret]
    fp.close()
    return ret
    
def wrapup_up(fail=False):
    if fail:
        sys.exit(1)
    else:
        sys.exit(0)
        
#---Start---

if(file_erase(default_licfile)):
    log_to_file('File ' + str(default_licfile) + ' deleted OK.')
else:
    log_to_file('Failed to delete ' + str(default_licfile) + '!')    

mac_lst = get_macs()

log_to_file('Got MAC Addresses:' + str(mac_lst) + '.')
        
key = get_best_key(mac_lst)
            
log_to_file('Calculated ' + str(len(key)) + ' byte key.')

try:
    licence_expiration_unixtime = str(int(time.mktime(time.strptime(licence_expiration, '%Y-%m-%d %H:%M:%S'))))
except ValueError:
    log_to_file('Could not convert ' + str(licence_expiration) + ' to an integer.')

log_to_file('Setting expiration time to: ' + str(licence_expiration) + '. Unixtime: ' + str(licence_expiration_unixtime) + '.')

encrypted_licence_expiration = encrypt(key, licence_expiration_unixtime)

if write_to_file(encrypted_licence_expiration, default_licfile):
    log_to_file('File ' + str(default_licfile) + ' updated OK.')
else:
    log_to_file('Failed to update ' + str(default_licfile) + '!')    
    
encrypted_licence_usage = encrypt(key, licence_usage)

if write_to_file(encrypted_licence_usage, default_licfile):
    log_to_file('File ' + str(default_licfile) + ' updated OK.')
else:
    log_to_file('Failed to update ' + str(default_licfile) + '!')    

encrypted_licence_usage_start = encrypt(key, licence_usage_start)

if write_to_file(encrypted_licence_usage_start, default_licfile):
    log_to_file('File ' + str(default_licfile) + ' updated OK.')
else:
    log_to_file('Failed to update ' + str(default_licfile) + '!')    

readback = file_read(default_licfile)

if(len(readback)):
    log_to_file('File ' + str(default_licfile) + ' readback OK.')
else:
    log_to_file('Failed to read from ' + str(default_licfile) + '!')    
    
decrypted_licence_expiration = decrypt(key, readback[0])
decrypted_licence_usage = decrypt(key, readback[1])
decrypted_licence_usage_start = decrypt(key, readback[2])

if(decrypted_licence_expiration == licence_expiration_unixtime):
    log_to_file('Expiration licence encryption successful.')
else:
    log_to_file('Expiration licence encryption failed.')

if(decrypted_licence_usage == licence_usage):
    log_to_file('Usage licence encryption successful.')
else:
    log_to_file('Usage licence encryption failed.')
    
if(decrypted_licence_usage_start == licence_usage_start):
    log_to_file('Usage licence start encryption successful.')
else:
    log_to_file('Usage licence start encryption failed.')
    

#----End----
