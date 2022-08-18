import requests
import hashlib
import sys
from getpass import getpass

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}, check the api and try again')
    return res

def get_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if hash_to_check == h:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_count(response,tail)

def main(password):
    count = pwned_api_check(password)
    if count:
        print(f'Your password was found {count} times! You should probably change it...')
    else:
        print(f'Your password was not found! Carry on...')

passw = getpass()
main(passw)