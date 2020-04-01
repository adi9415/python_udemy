import requests
import hashlib
import sys
# response 400  -> Not good with the api


def request_api_data(query_char):

    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        print(f'Error fetching {res.status_code}')
    else:
        return res


def get_pass_match(response, password):
    response = (line.split(':') for line in response.text.splitlines())
    for res, count in response:
        if res == password:
           # print(res, count, password)
            return count
    return 0


def pawned_api_check(password):
    # check if it is present in the API response
    # hesdigest -> converts the object in the hexadecimal string
    sha1pass = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    first5char, tail = sha1pass[:5], sha1pass[5:]
    #print (first5char)
    response = request_api_data(first5char)
    # print(first5char,tail,response)
    return get_pass_match(response, tail)


def main(args):

    with open(args, 'r') as file:

        for password in file:
            #password = file.readline()
            if password :
                #print(password)
                count = pawned_api_check(password.strip())
                if count:
                    print(f'Hey your passowrd -- {password.strip()} -- is hacked {count} times')
                else:
                    print(f'Nice passowrd -- {password.rstrip()} -- It is Hacked {count} times')
            else :
                continue

    return 'Thankyou!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
